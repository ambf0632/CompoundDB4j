# ChEMBL
**Pre-requisites**: 

1. MySQL installed in your local system. 
2. Neo4J-Community edition Application installed in your system. (refer https://neo4j.com/ if you have any queries)
3. Install py2neo using the command (sudo pip install py2neo).

**Step-1**: Download the Chembl_24 database and load the dump file into MySQL in your local system.

**Step-2**: Run convertToCSV.py file in the terminal. You can skip the step1 by directly downloading the CSV files from [here](https://drive.google.com/open?id=1NrFi96gQ_8VB8cHya86VxAwtralAA6IN).

(This will create the CSV files with required columns. The required columns list should be in schema_select_tables.txt file)

**Note**: Change the user, password and db according to your MySQL information.

**Step-3**: Open neo4j_community/conf/neo4j.conf and change the following lines.

1. Comment this line "dbms.directories.import=import"
2. Change the value of this line "dbms.security.auth_enabled=true" to false.
3. Change the value of this line "dbms.memory.heap.max_size=1G" to 10G
4. Add this line "dbms.security.allow_csv_import_from_file_urls=true"

Now,to start the graph, open terminal and go to neo4j community folder and run the following command : ./bin/neo4j console 

**Step-4**: Make changes in exportCSV function of graphs.py file, change the directory of csv files accordingly. Also make required changes user and password which are mentioned at the end of file. 

**Step-5**: graphs.py files contains different function exportCSV - for exporting CSV data into neo4j ,combine_nodes() - for merging two different types of nodes into a single node based on their primary keys, relationships() for creating relations between different nodes. Run graphs.py file in your desktop in another terminal. After the execution of that file, the data we require is loaded into Neo4J as per the schema. exportCSV function can be used to export all the tables of chembl as nodes (eventhough they are not mentioned in the below schema diagram)

This is how we merged the nodes and how we formed relations among different nodes:
![alt text](https://github.com/ambf0632/compoundDB4j/blob/master/ChEMBL/chembl_diagram_with_Chembl_er_schema.png)

**Note**: running graphs.py file may take some time. This is because of huge number of records of ChEMBL and the imports happen with periodic execution of cypher queries
