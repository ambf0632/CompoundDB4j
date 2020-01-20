# CompoundDB4j

This project contains the sources for integration of bio databases - ChEMBL and DrugBank.

neo4j_Chembl_DrugBank.db is an integrated database file for CompoundDB4j. (available for download from )



# Installation & Setup

* Unzip the file from the above share
* Install neo4j community edition from neo4j download center :https://neo4j.com/download-center/#community
  (We used Version 3.2.14 )
* In neo4j Community folder change the configuration file : neo4j_community/conf/neo4j.conf as follows:
    *  Comment this line "dbms.directories.import=import"
    *  Change the value of this line "dbms.security.auth_enabled=true" to false.
    *  Change the value of this line "dbms.memory.heap.max_size=1G" to 10G
    *  Add this line "dbms.security.allow_csv_import_from_file_urls=true"
    *  Uncomment  and change the value as "dbms.active_database=neo4j_Chembl_Drugbank.db" 
    
* Save the file
* Open the terminal and run the command ./bin/neo4j console
* When the command is executed, it provides a url where the database runs.
* Redirect to the url. 
* CompoundDb4j is now ready for operations (i.e Required data from ChEMBL and DrugBank are populated in neoj)
