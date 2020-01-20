# DrugBank_to_Neo4j
This integrates all open source data of DrugBank into Neo4j.

This integrated DrugBank (https://www.drugbank.ca/releases/latest) into Neo4j, but first the DrugBank data are formed into tsv file with use of https://github.com/dhimmel/drugbank/blob/gh-pages/parse.ipynb
with some changes, so that also more properties and relationships are extracted. The results are multiple tsv files and not only one.

After extract the information of the XML file the information must be combined with the information from the other DrugBank files. Also, the targets are validated with the UniProt identifier (https://github.com/ckoenigs/UniProt_to_Neo4j). The program need as information where the other DrugBank files are. Also, the generated csv files from the other program are in a dictionary drugbank.

The prepared program generates csv/tsv files to integrate the DrugBank information into neo4j. However, there are two possibilities:
1. if already an neo4j database exists then use the script : script_to_start_program_and_integrate_into_neo4j.sh 
2. no neo4j database is existing then with the neo4j-admin import tool the data can be integrated very fast. Use the script: script_with_import_tool.sh

This should have the form:

![er_diagram](https://github.com/ckoenigs/DrugBank_to_Neo4j/blob/master/drugbank_er.png)

The Compound has so many properties:

![er_diagram](https://github.com/ckoenigs/DrugBank_to_Neo4j/blob/master/drugbank_compound.png)

The Relationships have also some properties:

![er_diagram](https://github.com/ckoenigs/DrugBank_to_Neo4j/blob/master/drugbank_er_rela.png)



Link: https://github.com/ckoenigs/DrugBank_to_Neo4j
