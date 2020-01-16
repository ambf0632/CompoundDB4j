# -*- coding: utf-8 -*-
"""
@author: ckoenigs
"""

from py2neo import Graph
import sys
import datetime

# connect with the neo4j database
def database_connection():

    # the second is the user name for neo4j
    #the third is the password
    #authenticate("localhost:7474", "neo4j", "test")
    global g
    g = Graph()

'''
gather all information of a node into a dictionary and return this dictionary
'''
def gather_node_information(node_label):
    query = '''Match (s:%s) Return s Limit 1'''
    query = query % (node_label)
    results = g.run(query)
    for node, in results:
        return dict(node)

'''
check out how many new relationships from the merge node to another node or the other way around
then to reduce the integration time integrate only a limte number of relationships and this multiple times
'''
def generate_cypher_query_for_rela(query_counter,query_new_rela):
    results=g.run(query_counter)
    number_of_rela_to_another_node=0
    if results:
        for result, in results:
            number_of_rela_to_another_node=int(result)
    number_of_steps= int(number_of_rela_to_another_node/commit_number)+1

    counter=0
    while counter< number_of_steps:
        #cypher_file.write('begin \n')
        cypher_file.write(query_new_rela)
        #cypher_file.write('commit \n')
        counter+=1

# file with the different cypher queries to merge two nodes together and take over the relationships
cypher_file=open('cypher_file.cypher','w')

# queries per commit
commit_number=10000

'''
gather all information from one node and integrate them into the new node
this also check if one property already exists in the other node
'''


def merge_information_from_one_node_to_another_node(delete_node_label, merged_node_label, string_with_consider_rela_to_combined_node,string_relationship_direction, add_label=None):
   # relationships from the merge node
    query_count='''Match p=(merge_node:%s)'''+string_relationship_direction+'''(deleted_node:%s)-[]->(t) Return count(p)'''
    query_count=query_count %(merged_node_label,delete_node_label)
    query='''Match (merge_node:%s)'''+string_relationship_direction+'''(deleted_node:%s)-[r]->(t) '''+string_with_consider_rela_to_combined_node+''' With merge_node,r,t Limit %s Create (merge_node)-[g:child_of]->(t) Set g=r Delete r;\n'''
    query=query%(merged_node_label,delete_node_label,str(commit_number))
    generate_cypher_query_for_rela(query_count,query)


    #relationships to the merge node
    query_count='''Match p=(merge_node:%s)'''+string_relationship_direction+'''(deleted_node:%s)<-[]-(t) Return count(p)'''
    query_count=query_count %(merged_node_label,delete_node_label)
    query='''Match (merge_node:%s)'''+string_relationship_direction+'''(deleted_node:%s)<-[r]-(t) '''+string_with_consider_rela_to_combined_node+''' With merge_node,r,t Limit %s Create (merge_node)<-[g:child_of]-(t) Set g=r Delete r;\n'''
    query=query%(merged_node_label,delete_node_label,str(commit_number))
    generate_cypher_query_for_rela(query_count,query)


    # get all information of the deleted node
    dict_delete_node= gather_node_information(delete_node_label)
    if dict_delete_node is None:
        sys.exit('The first label '+delete_node_label+' is not existing')

    # get all information of the new node
    dict_combined_node= gather_node_information(merged_node_label)
    if dict_combined_node is None:
        sys.exit('The second label '+delete_node_label+' is not existing')

    #
    query='''Match (merge_node:%s)-[]-(deleted_node:%s) With merge_node, deleted_node Limit %s  Set ''' %(merged_node_label, delete_node_label,str(commit_number))

    for neo4j_property, value in dict_delete_node.items():
        if not neo4j_property in dict_combined_node:
            query+= 'merge_node.'+neo4j_property+'="'+str(value)+'", '
        else:
            print('property in both nodes:'+neo4j_property)

    if add_label:
        query=query+'merge_node:%s Detach Delete deleted_node;\n' %(add_label)
    else:
        query=query[:-2]+' Detach Delete deleted_node;\n'

    counter_query='''Match p=(merge_node:%s)-[]-(deleted_node:%s) Return count(p) '''
    counter_query=counter_query %(merged_node_label,delete_node_label)
    generate_cypher_query_for_rela(counter_query,query)


def main():
    # check if all arguments are there
    if len(sys.argv)>=5:
        delete_node_label=sys.argv[1]
        merge_node_label=sys.argv[2]
        self_loop_not_existing=True if sys.argv[3]=='True' or sys.argv[3]=='true' else False
        is_rela_from_merge_node_to_into=True if sys.argv[4]=='True' or sys.argv[4]=='true' else False
        print(self_loop_not_existing)
        print(is_rela_from_merge_node_to_into)
        if len(sys.argv)>4:
            new_node_label=sys.argv[5]
        else:
            new_node_label=None
    else:
        sys.exit('''Need at least 4 arguments:
            1: label for the node which should be merged into another
            2: label of the into node
            3: boolean if self loops sould be delete or not
            4: boolean if the relationship goes from node 1 to node 2
            5: new label if the merged node should get another label''')


    print(datetime.datetime.utcnow())

    print('##########################################################################')

    print(datetime.datetime.utcnow())
    print('connection to db')

    database_connection()

    print('##########################################################################')

    print(datetime.datetime.utcnow())
    print('generate cypher file for merging the nodes')

    # depending on is the relationship from the node which will be merge into
    # another or the other way around the relationship mus be define different
    string_direction_relationship=''
    if is_rela_from_merge_node_to_into:
        string_direction_relationship='<-[]-'
    else:
        string_direction_relationship='-[]->'
    #
    string_with_consider_rela_to_combined_node=''
    if self_loop_not_existing:
        string_with_consider_rela_to_combined_node='Where ID(t)<>ID(merge_node)'

    merge_information_from_one_node_to_another_node(delete_node_label,merge_node_label,string_with_consider_rela_to_combined_node,string_direction_relationship,new_node_label)

    print('##########################################################################')

    print(datetime.datetime.utcnow())



if __name__ == "__main__":
    # execute only if run as a script
    main()
