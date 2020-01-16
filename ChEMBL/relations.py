from py2neo import Graph, Node, Relationship
import csv

def chembl_drugbank_relations():
    with open('/home/susmitha/V/outputExactMatches/exact_outallmatches_unique_salt_chemblid_drugnames.tsv', 'r') as rf:
        data = [row for row in csv.reader(rf)]
        cnt=0
        for i in range(0, len(data)):
            query = '''match (n:Compound), (m:Salt_DrugBank) where n.chembl_id = "''' + data[i][0].split()[0] +'''" and m.identifier = "''' + data[i][0].split()[1] + '''" create (n)-[r:is_salt_exists]->(m) return count(r) as count'''
            #print(query)
            q = graph.run(query)
            cnt = cnt + q.data()[0]["count"]
            print(cnt)

graph = Graph()
chembl_drugbank_relations()
