from py2neo import Graph, Node, Relationship

def exportCSV(file):
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            i = 0
            query = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM \"file:///home/susmitha/Documents/neo4j_chembl/neo4j-community-3.2.14/import/Csv_files/'''
            for word in line.split():
                if i==0:
                    query = query + word + ".csv\" AS row FIELDTERMINATOR '\t' CREATE (:"+word+"{"
                    i=i+1
                else:
                    query = query + word + ":row." + word + ", "
            query = query[:-2]
            query = query + "})"
            i=0
            #print query
            graph.run(query)

def combine_nodes(merge_node, delete_node, primary_key):
    q1 = '''match (n:''' + delete_node + ''') return keys(n) as keys limit 1'''
    dict = graph.run(q1)
    list = dict.data()[0]["keys"]
    query = '''match (x:''' + merge_node + '''), (y:''' + delete_node + ''') where x.''' + primary_key + ''' = y.''' + primary_key + ''' set '''
    for i in list:
        if i != primary_key:
            query = query + '''x.''' + i + ''' = y.''' + i + ''', '''
    query = query[:-2]
    query = query + ''' detach delete y return x limit 100000'''
    print(query)
    q2 = '''MATCH (n:''' + delete_node+ ''') RETURN count(n)'''
    value = graph.run(q2).data()
    value = value[0]["count(n)"]
    temp = -1
    while(value != 0 and temp != value):
        graph.run(query)
        temp = value
        value = graph.run(q2).data()
        value = value[0]["count(n)"]
        print(value)


def write_to_csv():
    q1 = '''match (n) return distinct labels(n)'''
    list = graph.run(q1)
    for i in list:
		print(i[0][0])
		q2 = '''match (n:''' + i[0][0] + ''') return keys(n) as keys limit 1'''
		dict = graph.run(q2)
		list2 = dict.data()[0]["keys"]
		q3 = '''call apoc.export.csv.query(\"match (n:''' + i[0][0] + ''') return '''
		for j in list2:
			q3 = q3 + '''n.''' + j + ''' as ''' + j + ''', '''
		q3 = q3[:-2]
		q3 = q3 + '''\", \"/tmp/''' + i[0][0] +'''.csv\", {batchSize:100000})'''
		print(q3)


def deleteProcessed():
    query = "match (n:processed) with n limit 100000 remove n:processed return count(*) as processed"
    if query != "":
        values = graph.run(query).data()
        value = values[0]["processed"]
        while(value==100000):
            values = graph.run(query).data()
            value = values[0]["processed"]

def relationships():
    csv = []
    keys = []
    with open("primarykey.txt") as f:
        lines = f.readlines()
        for line in lines:
            i=0
            for word in line.split():
                if i==0:
                    csv.append(word)
                    i=i+1
                else:
                    keys.append(word)
    with open("sch.txt") as f:
        lines = f.readlines()
        for line in lines:
            i=0
            query = ""
            for word in line.split():
                if i==0:
                    file = word
                    i=i+1
                else:
                    for key in range(0, len(keys)):
                        if keys[key] == word and csv[key]!=file:
                            query = "MATCH (a:"+csv[key] + ") WITH a MATCH (p:" + file + "{" + word + ": a." + word +"} ) WHERE NOT p:processed WITH a, p LIMIT 10000 MERGE (p) - [:child_of] -> (a) SET p:processed RETURN COUNT(*) AS processed"
                            #print(query)
                            values = graph.run(query).data()
                            value = values[0]["processed"]
                            print(value)
                            while(value==100000):
                                print(value)
                                values = graph.run(query).data()
                                value = values[0]["processed"]
                            #print value
                            deleteProcessed()
                            #print "Deleted processed"
                            #print csv[key] + word

def delete():
    query = "MATCH ()-[r:child_of]-() with r limit 100000 DELETE r return count(r) as deletedrelations"
    if query != "":
        values = graph.run(query).data()
        value = values[0]["deletedrelations"]
        while(value==100000):
            values = graph.run(query).data()
            value = values[0]["deletedrelations"]
            #print value

def relationships_with_names(from_node, to_node, property_node, pk_relation, pk_property, relation_name):
    query = '''match (a:''' + from_node + '''), (b:''' + to_node + '''), (c:''' + property_node + ''') where b.''' + pk_property + ''' = c.''' + pk_property + ''' and a.''' + pk_relation + ''' = b.''' + pk_relation + ''' and NOT a:processed with a,b,c limit 10000 merge (a)-[r:''' + relation_name + '''{'''
    q1 = '''match (n:''' + property_node + ''') return keys(n) as keys limit 1'''
    dict = graph.run(q1)
    list = dict.data()[0]["keys"]
    for i in list:
        query = query + i + ''': c.''' + i + ''', '''
    query = query[:-2]
    query = query + '''}]->(b) set a:processed return count(*) as processed'''
    values = graph.run(query).data()
    value = values[0]["processed"]
    while(value==100000):
        print(value)
        values = graph.run(query).data()
        value = values[0]["processed"]
    print(value)
    deleteProcessed()
    print("Deleted processed")

def relations(from_node, to_node, property_node, pk_from, pk_to, relation_name):
    query = '''match (a:''' + from_node + '''), (b:''' + to_node + '''), (c:''' + property_node + ''') where a.''' + pk_from + ''' = c.''' + pk_from + ''' and b.''' + pk_to + ''' = c.''' + pk_to + ''' and NOT c:processed with a,b,c limit 100000 merge (a)-[r:''' + relation_name + '''{'''
    q1 = '''match (n:''' + property_node + ''') return keys(n) as keys limit 1'''
    dict = graph.run(q1)
    list = dict.data()[0]["keys"]
    for i in list:
        query = query + i + ''': c.''' + i + ''', '''
    query = query[:-2]
    query = query + '''}]->(b) set c:processed return count(*) as processed'''
    print(query)
    values = graph.run(query).data()
    value = values[0]["processed"]
    while(value==100000):
        print(value)
        values = graph.run(query).data()
        value = values[0]["processed"]
    print(value)
    deleteProcessed()
    print("Deleted processed")
    
def relationships_without_property(from_node, to_node, pk, relation_name):
    query = '''match (a:''' + from_node + '''), (b:''' + to_node + ''') where b.''' + pk + ''' = a.''' + pk +  ''' and NOT a:processed with a,b limit 10000 merge (a)-[r:''' + relation_name 
    query = query + ''']->(b) set a:processed return count(*) as processed'''
    print(query)
    values = graph.run(query).data()
    value = values[0]["processed"]
    while(value==10000):
        print(value)
        values = graph.run(query).data()
        value = values[0]["processed"]
    print(value)
    deleteProcessed()
    print("Deleted processed")
    

uri = "bolt://localhost:7687"
user = "neo4j"
password = "chembl"
graph = Graph(uri=uri, user=user, password=password)
"""
exportCSV("sch.txt")

relationships_without_property("Compound","Compound_records","molregno","Compound_Compound_records")
relationships_without_property("Compound","Induces","molregno","Compound_Induces")
relationships_without_property("Compound","activates","molregno","Compound_activates")
relationships_without_property("Compound","associates","molregno","Compound_associates")
relationships_without_property("Compound","binds","molregno","Compound_binds")
relationships_without_property("Compound","deactivates","molregno","Compound_deactivates")
relationships_without_property("Compound","inhibits","molregno","Compound_inhibits")
relationships_without_property("Compound_records","Induces","record_id","Compound_records__Induces")
relationships_without_property("Induces","Disease","mesh_id","Disease_Induces")
relationships_without_property("activates","Compound_records","record_id","activates_Compound_records")
relationships_without_property("associates","Compound_records","record_id","associates_Compound_records")
relationships_without_property("binds","Compound_records","record_id","binds_Compound_records")
relationships_without_property("deactivates","Compound_records","record_id","deactivates_Compound_records")
relationships_without_property("inhibits","Compound_records","record_id","inhibits_Compound_records")
relationships_without_property("activates","Target","tid","activates_Target")
relationships_without_property("deactivates","Target","tid","deactivates_Target")
relationships_without_property("associates","Target","tid","associates_Target")
relationships_without_property("binds","Target","tid","binds_Target")
relationships_without_property("inhibits","Target","tid","inhibits_Target")
relationships_without_property("Target","Assay","tid","assays")
relations("Compound","Assay","activities","molregno","assay_id","inhibits_activates")
relations("Compound","Structure_Alert","compound_structural_alert","molregno","alert_id","has")
relations("Component","Target","target_components","component_id","tid","part_f")
"""
