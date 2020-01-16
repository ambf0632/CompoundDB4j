#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


### find common based on name between compounds  DB and chembl  and write to csv 
import pandas as pd
dfdb2 =pd.read_csv('drugbank_drug.tsv',delimiter='\t',encoding='utf-8')

print(dfdb2.columns[2]) #2=name
print(len(dfdb2.columns))

listNames_compoundDB=[]
listExactMatchNames_compoundDB=[]
listChemblNames=[]
dictExactMatchNames_compoundDB={}

#listNames_compoundDB.append(dfdb2[dfdb2.columns[2].lower()])
listNames_compoundDB=[x.lower() for x in dfdb2[dfdb2.columns[2].lower()]]

print("total",len(dfdb2[dfdb2.columns[2]]))                    
print(len(listNames_compoundDB))
#print(listNames_compoundDB)

dfChemblNames =pd.read_csv('chembl24prefnames_ids.csv',delimiter=',',encoding='utf-8') #chembl24prefnames.csv
print(dfChemblNames.shape)

#add to list only contains names
listChemblNames= [str(x).lower() for x in dfChemblNames[dfChemblNames.columns[0]]]

print(len(listChemblNames))

print(type(listChemblNames))
#print(listChemblNames)

#print(listChemblNames[1801523])

count=0
for item in listNames_compoundDB:     
    count=count+1   
    #name=str(item).lower()
    if item in listChemblNames :
        listExactMatchNames_compoundDB.append(item)
        
print(len(listExactMatchNames_compoundDB))
#print(listExactMatchNames_compoundDB)



#add to dict chembl id as value and name as key
listChemblNames= [str(x).lower() for x in dfChemblNames[dfChemblNames.columns[0]]]
listChemblIds=[str(x) for x in dfChemblNames[dfChemblNames.columns[1]]]
dictChemblNamesIds=dict(zip(listChemblNames,listChemblIds))

#consider checking names in drugbank to synonmys in chembl
dfChemblSynonyms =pd.read_csv('chembl24_synonyms_ids.csv',delimiter=',',encoding='utf-8')#chembl24_synonyms
listChemblSNames= [str(x).lower() for x in dfChemblSynonyms[dfChemblSynonyms.columns[0]]]
listChemblSIds=[str(x) for x in dfChemblSynonyms[dfChemblSynonyms.columns[1]]]
dictChemblSIds=dict(zip(listChemblSNames,listChemblSIds))


for key, value in dictChemblNamesIds.items() :
    print(key, value)
    break
    

        
for item in listNames_compoundDB:   
    if item in dictChemblNamesIds:
        dictExactMatchNames_compoundDB[item]= dictChemblNamesIds[item]  
    if item in dictChemblSIds:
        dictExactMatchNames_compoundDB[item]= dictChemblSIds[item] 
      
       
print(len(dictExactMatchNames_compoundDB))


# In[3]:


for key, value in dictExactMatchNames_compoundDB.items() :
    print(key, value)
    break
print(listExactMatchNames_compoundDB[0])


# In[4]:


print(listChemblNames[1801523])
print(listNames_compoundDB[0])
print(type(listChemblNames))

#s = str(listChemblNames[1801523])
#print(s.lower())

    


# In[7]:


import csv

count=0
dataArr=dfdb2.values
for idx in range(len(dfdb2.values)):
    print("ss")
    #print(dataArr[idx])
    break

'''            
with open("outmatches_names.csv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdb2.values)):        
        if str(dataArr[idd][2]).lower() in listExactMatchNames_compoundDB:
            item=dataArr[idd]            
            writer.writerow([item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
            

with open("outmatches_names_drugnames.csv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter=';',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdb2.values)):
        if str(dataArr[idd][2]).lower() in listExactMatchNames_compoundDB:
            item=dataArr[idd]            
            writer.writerow([item[0], item[2]])  
'''

#add chembl id also to csv matches file 
with open("outmatches_names_drugnames_chemblids.tsv",'w') as outcsv2: 
    writer2=csv.writer(outcsv2,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')  
    with open("outmatches_names_chemblids.tsv",'w') as outcsv: 
        writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        for idd in range(len(dfdb2.values)):
            dbname=str(dataArr[idd][2]).lower()
            if dbname in dictExactMatchNames_compoundDB.keys():
                for name, idval in dictExactMatchNames_compoundDB.items():   
                    if dbname == name:                    
                        item=dataArr[idd]  
                        chemblid=idval
                        writer.writerow([ chemblid,item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                        writer2.writerow([chemblid, item[0], item[2]]) 
            


# In[8]:


### find common based on synonmys  between compounds  DB and chembl  and write to csv 
import pandas as pd
dfdb2 =pd.read_csv('drugbank_drug.tsv',delimiter='\t',encoding='utf-8')

print(dfdb2.columns[28]) #2=name
print(len(dfdb2.columns))

listsynonyms_compoundDB=[]
listsynonyms_compoundDB_all=[]
listExactMatchSynonyms_compoundDB=[]
listChemblSynonyms=[]
dictExactMatchSynonyms_compoundDB={}


#listNames_compoundDB.append(dfdb2[dfdb2.columns[2].lower()])
listsynonyms_compoundDB=[str(x).lower() for x in dfdb2[dfdb2.columns[28]]]

print("total",len(dfdb2[dfdb2.columns[28]]))                    
print(len(listsynonyms_compoundDB))
print(listsynonyms_compoundDB[0])


dfChemblSynonyms =pd.read_csv('chembl24_synonyms_ids.csv',delimiter=',',encoding='utf-8')#chembl24_synonyms
print(dfChemblSynonyms.shape)
#listChemblNames=dfChemblNames.values.tolist()
listChemblSynonyms= [str(x).lower() for x in dfChemblSynonyms[dfChemblSynonyms.columns[0]]]

print(len(listChemblSynonyms))

print(type(listChemblSynonyms))
#print(listChemblNames)

#print(listChemblNames[1801523])

count=0
for item in listChemblSynonyms:     
    count=count+1   
    #name=str(item).lower()
    if item in listsynonyms_compoundDB :
        listExactMatchSynonyms_compoundDB.append(item)
        
print(len(listExactMatchSynonyms_compoundDB))

#add to dict chembl id as value and synonyms as key
listChemblSNames= [str(x).lower() for x in dfChemblSynonyms[dfChemblSynonyms.columns[0]]]
listChemblSIds=[str(x) for x in dfChemblSynonyms[dfChemblSynonyms.columns[1]]]
dictChemblSIds=dict(zip(listChemblSNames,listChemblSIds))

#consider checking drugbank synonyms to names in chembl
dfChemblNames =pd.read_csv('chembl24prefnames_ids.csv',delimiter=',',encoding='utf-8') #chembl24prefnames.csv
listChemblNames= [str(x).lower() for x in dfChemblNames[dfChemblNames.columns[0]]]
listChemblIds=[str(x) for x in dfChemblNames[dfChemblNames.columns[1]]]
dictChemblNamesIds=dict(zip(listChemblNames,listChemblIds))


for key, value in dictChemblSIds.items() :
    print(key, value)
    break
    
#db synonmys contains  formate |a||||aa||||bb||||b|
for x in listsynonyms_compoundDB:
    x=str(x)
    if '|' in x:
        xall = x.replace('||||','|')
        xarr = xall.split("|")
        for m in xarr:
            if m!= '':
                listsynonyms_compoundDB_all.append(m)
    else:
        if x!= '':
            m=x
            listsynonyms_compoundDB_all.append(m)

for item in listsynonyms_compoundDB_all:   
    if item in dictChemblSIds:
        dictExactMatchSynonyms_compoundDB[item]= dictChemblSIds[item] 
    if item in dictChemblNamesIds:
        dictExactMatchSynonyms_compoundDB[item]= dictChemblNamesIds[item] 

        
print(len(dictExactMatchSynonyms_compoundDB))


# In[9]:


import csv

count=0
dataArr=dfdb2.values
for idx in range(len(dfdb2.values)):
    print("ss")
    #print(dataArr[idx])
    break

'''           
with open("outmatches_synonyms.csv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdb2.values)):        
        if str(dataArr[idd][28]).lower() in listExactMatchNames_compoundDB:
            item=dataArr[idd]            
            writer.writerow([item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
            

with open("outmatches_synonyms_drugnames.csv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter=';',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdb2.values)):
        if str(dataArr[idd][28]).lower() in listExactMatchNames_compoundDB:
            item=dataArr[idd]            
            writer.writerow([item[0], item[2]]) 
 '''           
            
            

#add chembl id also to csv synonym matches file 
with open("outmatches_synonyms_drugnames_chemblids.tsv",'w') as outcsv2: 
    writer2=csv.writer(outcsv2,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')  
    with open("outmatches_synonyms_chemblids.tsv",'w') as outcsv: 
        writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        for idd in range(len(dfdb2.values)):
            synonyms=str(dataArr[idd][28]).lower()
            if '|' in synonyms:
                xall = synonyms.replace('||||','|')
                xarr = xall.split("|")              
                for arr in xarr:                
                    if arr in dictExactMatchSynonyms_compoundDB.keys():
                        chemblid=dictExactMatchSynonyms_compoundDB[arr]                               
                        item=dataArr[idd]  
            else:
                arr=synonyms
                if arr in dictExactMatchSynonyms_compoundDB.keys():
                        chemblid=dictExactMatchSynonyms_compoundDB[arr]                               
                        item=dataArr[idd]  
                        
                
            writer.writerow([ chemblid,item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
            writer2.writerow([chemblid, item[0], item[2]]) 


# In[276]:


### ### ### ### #not in use###  ### ### ### ### 

#find if partial match exists between overall non matches and chembl for name and synonmys 
import pandas as pd #outnonmatches_allfields
dfdbs = pd.read_csv('outnonmatches_allfields__.tsv', header=None, delimiter='\t',encoding='utf-8')

print(dfdbs.columns[2]) #2=name
print(dfdbs.columns[28]) 
print(len(dfdbs.columns))

listPartialMatchSynonyms_dfdbs=[]
listPartialMatchSynonyms2_dfdbs=[]
listSynonyms_dfdbs=[]
listChemblSynonyms=[]
listNames_dfdbs=[]

#listNames_compoundDB.append(dfdb2[dfdb2.columns[2].lower()])
listNames_dfdbs=[str(x).lower() for x in dfdbs[dfdbs.columns[2]]]

print("total",len(dfdbs[dfdbs.columns[2]]))                    
print(len(listNames_dfdbs))
print(listNames_dfdbs[0])


dfChemblSynonyms =pd.read_csv('chembl24_synonyms.csv',delimiter='\t',encoding='utf-8')
print(dfChemblSynonyms.shape)
#listChemblNames=dfChemblNames.values.tolist()
listChemblSynonyms= [str(x).lower() for x in dfChemblSynonyms[dfChemblSynonyms.columns[0]]]

print(len(listChemblSynonyms))

print(type(listChemblSynonyms))
#print(listChemblNames)

#print(listChemblNames[1801523])

count=0
for item in listChemblSynonyms:  
    if item in listNames_dfdbs :        
        listPartialMatchSynonyms_dfdbs.append(item)
    else:
        arrAll = item.split(' ')
        for i in arrAll:            
            if i in listNames_dfdbs :                
                listPartialMatchSynonyms_dfdbs.append(i)
    
        
print(len(listPartialMatchSynonyms_dfdbs))
print(listPartialMatchSynonyms_dfdbs)

#synonmys contains  formate |a||||aa||||bb||||b|
for x in dfdbs[dfdbs.columns[28]]:
    x=str(x)
    if '|' in x:
        xall = x.replace('||||','|')
        xarr = xall.split("|")
        for m in xarr:
            if m!= '':
                listSynonyms_dfdbs.append(m.lower())
    else:
        if x!= '':
            m=x
            listSynonyms_dfdbs.append(m.lower())

#print("listSynonyms_dfdbs",listSynonyms_dfdbs)

for item in listChemblSynonyms:    
    if item in listSynonyms_dfdbs :        
        listPartialMatchSynonyms2_dfdbs.append(item)
    else:
        arrAll = item.split(' ')
        for i in arrAll:            
            if i in listSynonyms_dfdbs :                
                listPartialMatchSynonyms2_dfdbs.append(i)
        
print(len(listPartialMatchSynonyms2_dfdbs))
print(listPartialMatchSynonyms2_dfdbs)



# In[277]:


### ### ### ### #not in use###  ### ### ### ### 
#partial matches based on synonyms between non matched and chembl in a separate csv
import csv

count=0
dataArr2=dfdbs.values
for idx in range(len(dfdbs.values)):
    print("ss")
    #print(dataArr[idx])
    break
print(dfdbs.values[0][2])
            
with open("outmatches_names_nonmatches_chembl_3.tsv",'w') as outcsv: 
    with open("outmatches_names_nonmatches_chembl_drugnames_3.csv",'w') as outcsv2: 
        writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        writer2=csv.writer(outcsv2,delimiter=';',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

        for idd in range(len(dfdbs.values)): 
            namedb=dfdbs.values[idd][2].lower()            
            if namedb in listPartialMatchSynonyms_dfdbs:                       
                item=dataArr2[idd]            
                writer.writerow([item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                writer2.writerow([item[0], item[2]]) 
            
            
with open("outmatches_synonyms_nonmatches_chembl_3.tsv",'w') as outcsv: 
    with open("outmatches_synonyms_nonmatches_chembl_drugnames_3.csv",'w') as outcsv2: 
        writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        writer2=csv.writer(outcsv2,delimiter=';',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

        for idd in range(len(dfdbs.values)):            
            bExists=False
            synonyms=str(dfdbs.values[idd][28]).lower()  
            if '|' in synonyms:
                xall = synonyms.replace('||||','|')
                xarr = xall.split("|")
                
                print(xarr)
                for arr in xarr:                    
                    if arr!= '':
                        if 'ergoloid' in arr:
                            print("arr",arr)
                            print("listPartialMatchSynonyms2_dfdbs",listPartialMatchSynonyms2_dfdbs)
                        if str(arr) in listPartialMatchSynonyms2_dfdbs:
                            print("adding",arr)
                            #bExists=True
                            #break
                #if(bExists):
                            item=dataArr2[idd]            
                            writer.writerow([item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                            writer2.writerow([item[0], item[2]])
            else:
                if synonyms in listPartialMatchSynonyms2_dfdbs:                   
                    item=dataArr2[idd]            
                    writer.writerow([item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                    writer2.writerow([item[0], item[2]])
                        
                
         


# In[208]:


print(listPartialMatchSynonyms_compoundDB)


# In[10]:


### find common based on inchikey between compounds DB and chembl  and write to csv 
import pandas as pd
dfdb2 =pd.read_csv('drugbank_drug.tsv',delimiter='\t',encoding='utf-8')


print(dfdb2.columns[52]) #44=calculated properties
listInchiKey_CompoundDB=[]
listInchiKeyOnly_CompoundDB=[]
listInchiKey_CompoundDB.append(dfdb2[dfdb2.columns[52]])
#print("total",len(dfdb2.columns['inchikey']))
count=0

for item in dfdb2[dfdb2.columns[52]]:
    count = count+1
    item=str(item)
    listInchiKeyOnly_CompoundDB.append(item) 
    
    '''
    if item != 'nan':        
        arr = item.split('||')
        arr2=[]
        for item in arr:
            if 'InChIKey' in item:
                #val = samplesmi.split('::')
                #arr2.append(val[1])
                arr2.append(item)
                #
                for item in arr2:
                    val = item.split('::')
                    listInchiKeyOnly_CompoundDB.append(val[1]) 
       '''             
                  
                         


# In[299]:


print(len(listInchiKeyOnly_CompoundDB))


# In[302]:


print(listInchiKeyOnly_CompoundDB[0])


# In[11]:


print(len(listInchiKeyOnly_CompoundDB))
dfChembl =pd.read_csv('chembl24inchikey.csv',delimiter=',',encoding='utf-8') #.chembl24inchikey
listChemblInchiKey=dfChembl.values.tolist()
print(len(listChemblInchiKey))
print(type(listChemblInchiKey))
#exact matches inchikey against compound db
listExactMatch_CompoundDB=[]
dictExactMatchInchi_compoundDB={}

for item in listChemblInchiKey:    
    if item[0] in listInchiKeyOnly_CompoundDB:        
        listExactMatch_CompoundDB.append(item[0])

print(len(listExactMatch_CompoundDB))

dfChemblInchi =pd.read_csv('chembl24inchikey_chemblids.csv',delimiter=',',encoding='utf-8') #.chembl24inchikey
#add to dict chembl id as value and synonyms as key
listChemblInchi= [str(x) for x in dfChemblInchi[dfChemblInchi.columns[0]]]
listChemblIds=[str(x) for x in dfChemblInchi[dfChemblInchi.columns[1]]]


dictChemblInchiIds=dict(zip(listChemblInchi,listChemblIds))

for key, value in dictChemblInchiIds.items() :
    print(key, value)
    break
    


# In[12]:


for item in listInchiKeyOnly_CompoundDB:   
    if item in dictChemblInchiIds:
        dictExactMatchInchi_compoundDB[item]= dictChemblInchiIds[item] 
           

        
'''
for item in listInchiKeyOnly_CompoundDB:
    if item != 'nan':
        if item in dictChemblInchiIds.keys():
            for i, idval in dictChemblInchiIds.items():   
                if i == item:
                    count=count+1
                    print("adding==",count)
                    dictExactMatchInchi_compoundDB[i]=idval
'''        
print(len(dictExactMatchInchi_compoundDB))


# In[13]:


import csv

count=0
dataArr=dfdb2.values
for idx in range(len(dfdb2.values)):
    print("ss")
    #print(dataArr[idx])
    break
'''
            
with open("outmatches_inchikey.csv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdb2.values)):
        if dataArr[idd][52] in listExactMatch_CompoundDB:
            item=dataArr[idd]
            
            writer.writerow([item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                             item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
            

with open("outmatches_inchikey_drugnames.csv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter=';',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdb2.values)):
        if dataArr[idd][52] in listExactMatch_CompoundDB:
            item=dataArr[idd]            
            writer.writerow([item[0], item[2]]) 
            
'''           
#add chembl id also to csv synonym matches file 
with open("outmatches_inchikey_drugnames_chemblids.tsv",'w') as outcsv2: 
    writer2=csv.writer(outcsv2,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')  
    with open("outmatches_inchikey_chemblids.tsv",'w') as outcsv: 
        writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        for idd in range(len(dfdb2.values)):
            dbname=dataArr[idd][52]
            if dbname in dictExactMatchInchi_compoundDB.keys():
                for name, idval in dictExactMatchInchi_compoundDB.items():   
                    if dbname == name:                    
                        item=dataArr[idd]  
                        chemblid=idval
                        writer.writerow([ chemblid,item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                        writer2.writerow([chemblid, item[0], item[2]]) 


# In[14]:


### find common based on smiles between compounds DB and chembl  and write to csv 
import pandas as pd
dfdb2 =pd.read_csv('drugbank_drug.tsv',delimiter='\t',encoding='utf-8')


print(dfdb2.columns[44]) #44=calculated properties
listSMILES_CompoundDB=[]
listSMILES_CompoundDBOnly_CompoundDB=[]
listSMILES_CompoundDB.append(dfdb2[dfdb2.columns[44]])
#print("total",len(dfdb2.columns['inchikey']))
count=0

for item in dfdb2[dfdb2.columns[44]]:
    count = count+1   
    if item != 'nan': 
        item=str(item)
        arr = item.split('||')
        arr2=[]
        for item in arr:
            if 'SMILES' in item:
                #val = samplesmi.split('::')
                #arr2.append(val[1])
                arr2.append(item)
                #
                for item in arr2:
                    val = item.split('::')
                    listSMILES_CompoundDBOnly_CompoundDB.append(val[1]) 
                    
print(len(listSMILES_CompoundDBOnly_CompoundDB))  
dfChembl =pd.read_csv('chembl24smiles.csv',delimiter='\t',encoding='utf-8')
listChemblsmiles=dfChembl.values.tolist()
print(len(listChemblsmiles))
print(type(listChemblsmiles))
listExactMatchsmiles_CompoundDB=[]

dictExactMatchSmi_compoundDB={}
for item in listChemblsmiles:    
    if item[0] in listSMILES_CompoundDBOnly_CompoundDB:        
        listExactMatchsmiles_CompoundDB.append(item[0])

print(len(listExactMatchsmiles_CompoundDB))


dfChemblSMI =pd.read_csv('chembl24smiles_chemblids.csv',delimiter=',',encoding='utf-8') #.chembl24smiles
#add to dict chembl id as value and synonyms as key
listChemblSMI= [str(x) for x in dfChemblSMI[dfChemblSMI.columns[0]]]
listChemblIds=[str(x) for x in dfChemblSMI[dfChemblSMI.columns[1]]]


dictChemblSmiIds=dict(zip(listChemblSMI,listChemblIds))

for key, value in dictChemblSmiIds.items() :
    print(key, value)
    break


# In[15]:


for item in listSMILES_CompoundDBOnly_CompoundDB:   
    if item in dictChemblSmiIds:
        dictExactMatchSmi_compoundDB[item]= dictChemblSmiIds[item] 
             
print(len(dictExactMatchSmi_compoundDB)) 


# In[16]:


import csv

count=0
dataArr=dfdb2.values
for idx in range(len(dfdb2.values)):
    print("ss")
    #print(dataArr[idx])
    break
'''
with open("outmatches_smiles_drugnames.csv",'w') as outcsv2:             
    with open("outmatches_smiles.csv",'w') as outcsv: 
        writer=csv.writer(outcsv,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        writer2=csv.writer(outcsv2,delimiter=';',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

        for idd in range(len(dfdb2.values)):
            listIm=[]
            item_ = dataArr[idd][44] 
            
            if item_ != 'nan': 
                #print(item_)
                item_=str(item_)
                arr = item_.split('||')
                arr2=[]
                for item in arr:
                    if 'SMILES' in item:
                        #val = samplesmi.split('::')
                        #arr2.append(val[1])
                        arr2.append(item)
                        #
                        for item in arr2:
                            val = item.split('::')
                            listIm.append(val[1]) 
                    
            if listIm:
                #print("inside",listIm)
                if listIm[0] in listSMILES_CompoundDBOnly_CompoundDB:
                    item=dataArr[idd]            
                    writer.writerow([item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                         item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                    
                    #name=item2
                    writer2.writerow([item[0],item[2]])
'''
#add chembl id also to csv smiles matches file 
with open("outmatches_smiles_drugnames_chemblids.tsv",'w') as outcsv2: 
    writer2=csv.writer(outcsv2,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')  
    with open("outmatches_smiles_chemblids.tsv",'w') as outcsv: 
        writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        
        for idd in range(len(dfdb2.values)):
            listIm=[]
            item_ = dataArr[idd][44]            
            if item_ != 'nan': 
                #print(item_)
                item_=str(item_)
                arr = item_.split('||')
                arr2=[]
                for item in arr:
                    if 'SMILES' in item:
                        #val = samplesmi.split('::')
                        #arr2.append(val[1])
                        arr2.append(item)
                        #
                        for item in arr2:
                            val = item.split('::')
                            listIm.append(val[1]) 
                    
            if listIm:
                if listIm[0] in dictExactMatchSmi_compoundDB.keys():
                    for smi, idval in dictExactMatchSmi_compoundDB.items():   
                        if smi == listIm[0]:                    
                            item=dataArr[idd]  
                            chemblid=idval
                            writer.writerow([ chemblid,item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                                item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                                 item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                                item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                               item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                            writer2.writerow([chemblid, item[0], item[2]])    
    
                        
                   
    


# In[17]:


### find common based on chembl id  between compounds DB and chembl  and write to csv 
import pandas as pd
dfdb2 =pd.read_csv('drugbank_drug.tsv',delimiter='\t',encoding='utf-8')


print(dfdb2.columns[54]) #54=chembl id 
listChemblID_CompoundDB=[]
listChemblIDOnly_CompoundDB=[]

#print("total",len(dfdb2.columns['inchikey']))
count=0

for item in dfdb2[dfdb2.columns[54]]:
    #print(item)
    if str(item) != "nan":
        item=str(item)
        listChemblIDOnly_CompoundDB.append(item) 
            
print("len",len(listChemblIDOnly_CompoundDB))
print(len(listChemblIDOnly_CompoundDB))
dfChemblids =pd.read_csv('chembl24_chemblids.csv',delimiter='\t',encoding='utf-8')
listChemblids=dfChemblids.values.tolist()
print(len(listChemblids))
print(type(listChemblids))
#exact matches inchikey against compound db
listExactMatchChemblid_CompoundDB=[]
for item in listChemblids:    
    if item[0] in listChemblIDOnly_CompoundDB:        
        listExactMatchChemblid_CompoundDB.append(item[0])

print(len(listExactMatchChemblid_CompoundDB))


# In[18]:


import csv

count=0
dataArr=dfdb2.values
for idx in range(len(dfdb2.values)):
    print("ss")
    #print(dataArr[idx])
    break

            
with open("outmatches_chemblid.tsv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdb2.values)):
        if dataArr[idd][54] in listExactMatchChemblid_CompoundDB:
            item=dataArr[idd]
            
            writer.writerow([item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                            item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
            

with open("outmatches_chemblid_drugnames.tsv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdb2.values)):
        if dataArr[idd][54] in listExactMatchChemblid_CompoundDB:
            item=dataArr[idd]            
            writer.writerow([item[54], item[0],item[2]])          


# In[280]:


#### not in use #####
#write consolidated non matches  to csv based smiles out csv , inchi out csv
listCompoundDBMatchedNames=[]
listCompoundDBMatchedIDs=[]

dfid =pd.read_csv('outmatches_chemblid_drugnames.csv', header=None, delimiter=";", encoding='utf-8')
listid=dfid.values

for item in listid:
    #print(item)
    listCompoundDBMatchedIDs.append(item[0])
    listCompoundDBMatchedNames.append(item[1])
    
dfid1 =pd.read_csv('outmatches_names_drugnames.csv', header=None, delimiter=";", encoding='utf-8')
listid1=dfid1.values
print(listid1[0])
for item1 in listid1:
   

    listCompoundDBMatchedIDs.append(item1[0])
    listCompoundDBMatchedNames.append(item1[1])
    
dfid2 =pd.read_csv('outmatches_inchikey_drugnames.csv',header=None,  delimiter=";", encoding='utf-8')
listid2=dfid2.values

for item2 in listid2:
    #print(item)
    listCompoundDBMatchedIDs.append(item2[0])
    listCompoundDBMatchedNames.append(item2[1])
         
dfid3 =pd.read_csv('outmatches_smiles_drugnames.csv',header=None,  delimiter=";", encoding='utf-8')
listid3=dfid3.values

for item3 in listid3:
    #print(item)
    listCompoundDBMatchedIDs.append(item3[0])
    listCompoundDBMatchedNames.append(item3[1])
            
#outmatches_synonyms
dfid4 =pd.read_csv('outmatches_synonyms_drugnames.csv',header=None,  delimiter=";", encoding='utf-8')
listid4=dfid4.values

for item4 in listid4:
    #print(item)
    listCompoundDBMatchedIDs.append(item4[0])
    listCompoundDBMatchedNames.append(item4[1])  
        
print(len(listCompoundDBMatchedIDs))

print(len(listCompoundDBMatchedNames))
#dfmatchInchiKeyDrugs =pd.read_csv('drugbank_salt.tsv',delimiter='\t',encoding='utf-8')

#two new lists for name and synonym
dfid5 =pd.read_csv('outmatches_synonyms_nonmatches_chembl_drugnames.csv',header=None,  delimiter=";", encoding='utf-8')
listid5=dfid5.values

for item5 in listid5:
    #print(item)
    listCompoundDBMatchedIDs.append(item5[0])
    listCompoundDBMatchedNames.append(item5[1])
    
dfid6 =pd.read_csv('outmatches_names_nonmatches_chembl_drugnames.csv',header=None,  delimiter=";", encoding='utf-8')
listid6=dfid6.values

for item6 in listid6:
    #print(item)
    listCompoundDBMatchedIDs.append(item6[0])
    listCompoundDBMatchedNames.append(item6[1])
    
#revised two list obtained after code corrections - check chembl synonym is as is present in name, synonym before going for
#substring with space
#two new lists for name and synonym
dfid7 =pd.read_csv('outmatches_synonyms_nonmatches_chembl_drugnames_2.csv',header=None,  delimiter=";", encoding='utf-8')
listid7=dfid7.values

for item7 in listid7:
    #print(item)
    listCompoundDBMatchedIDs.append(item7[0])
    listCompoundDBMatchedNames.append(item7[1])
    
'''
dfid8 =pd.read_csv('outmatches_names_nonmatches_chembl_drugnames_2.csv',header=None,  delimiter=";", encoding='utf-8')
listid8=dfid8.values

for item8 in listid8:
    #print(item)
    listCompoundDBMatchedIDs.append(item8[0])
    listCompoundDBMatchedNames.append(item8[1])
'''
    
dfid9 =pd.read_csv('outmatches_names_nonmatches_chembl_drugnames_3.csv',header=None,  delimiter=";", encoding='utf-8')
listid9=dfid9.values

for item9 in listid9:
    #print(item)
    listCompoundDBMatchedIDs.append(item9[0])
    listCompoundDBMatchedNames.append(item9[1])
       
    
dfid10 =pd.read_csv('outmatches_names_nonmatches_chembl_drugnames_3.csv',header=None,  delimiter=";", encoding='utf-8')
listid10=dfid10.values

for item10 in listid10:
    #print(item)
    listCompoundDBMatchedIDs.append(item10[0])
    listCompoundDBMatchedNames.append(item10[1])


# In[19]:


#repeat write complete matches with chembl id to write to non matches list + later use for partial match findings
listCompoundDBMatchedNames=[]
listCompoundDBMatchedIDs=[]
listChemblMatchedIDs=[]


dfid =pd.read_csv('outmatches_chemblid_drugnames.tsv', header=None, delimiter="\t", encoding='utf-8')
listid=dfid.values

for item in listid:
    #print(item)
    listChemblMatchedIDs.append(item[0])
    listCompoundDBMatchedIDs.append(item[1])
    listCompoundDBMatchedNames.append(item[2])
    
dfid1 =pd.read_csv('outmatches_names_drugnames_chemblids.tsv', header=None, delimiter="\t", encoding='utf-8')
listid1=dfid1.values
print(listid1[0])
for item1 in listid1: 
    listChemblMatchedIDs.append(item1[0])
    listCompoundDBMatchedIDs.append(item1[1])
    listCompoundDBMatchedNames.append(item1[2])
    
dfid2 =pd.read_csv('outmatches_inchikey_drugnames_chemblids.tsv',header=None,  delimiter="\t", encoding='utf-8')
listid2=dfid2.values

for item2 in listid2:
    #print(item)
    listChemblMatchedIDs.append(item2[0])
    listCompoundDBMatchedIDs.append(item2[1])
    listCompoundDBMatchedNames.append(item2[2])
         
dfid3 =pd.read_csv('outmatches_smiles_drugnames_chemblids.tsv',header=None,  delimiter="\t", encoding='utf-8')
listid3=dfid3.values

for item3 in listid3:
    #print(item)
    listChemblMatchedIDs.append(item3[0])    
    listCompoundDBMatchedIDs.append(item3[1])
    listCompoundDBMatchedNames.append(item3[2])
            
#outmatches_synonyms
dfid4 =pd.read_csv('outmatches_synonyms_drugnames_chemblids.tsv',header=None,  delimiter="\t", encoding='utf-8')
listid4=dfid4.values

for item4 in listid4:
    #print(item)
    listChemblMatchedIDs.append(item4[0])    
    listCompoundDBMatchedIDs.append(item4[1])
    listCompoundDBMatchedNames.append(item4[2])  
        
print(len(listChemblMatchedIDs))

print(len(listCompoundDBMatchedNames))

print(len(listCompoundDBMatchedNames))


# In[193]:


#print(listCompoundDBMatchedNames)
for i in listCompoundDBMatchedNames:
    if i.startswith('Lep'):
        print(i)
        


# In[20]:


#write non matches to csv (compared against list of exact matches of name, smiles, inchi,, syonyms, id)

import csv

count=0
dataArr=dfdb2.values
for idx in range(len(dfdb2.values)):
    print("ss")
    #print(dataArr[idx])
    break

countM=0
countN=0


with open("exact_outnonmatches_dbid_dbnames.tsv",'w') as outcsv2:  
    writer2=csv.writer(outcsv2,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

    with open("exact_outnonmatches_allfields.tsv",'w') as outcsv: 
        writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        for idd in range(len(dfdb2.values)):            
            if dataArr[idd][0] in listCompoundDBMatchedIDs :
                countM =countM+1
            elif dataArr[idd][2] in listCompoundDBMatchedNames:                 
                countN =countN+1
            else:    
                count=count+1
                item=dataArr[idd] 
                writer.writerow([item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                                  item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                            item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                writer2.writerow([item[0],item[2]])
          
                     
                     
                
print("match id",countM) 
                
print("match name",countN)  
                
print("no match",count)  
                
     


# In[27]:


#data fusion part - find ony unique matches from all the individual matches (chembl id, name, synonym, inchi, smiles)
dictDBID_ChemblID={}

df_id =pd.read_csv('outmatches_chemblid_drugnames.tsv', header=None, delimiter="\t", encoding='utf-8')
listids=df_id.values

for item in listids:
    #print(item)
    dictDBID_ChemblID[item[1]]=item[0]   

    
df_name =pd.read_csv('outmatches_names_drugnames_chemblids.tsv', header=None, delimiter="\t", encoding='utf-8')
listnames=df_name.values
for item1 in listnames: 
    dbid=item1[1]
    if dbid not in dictDBID_ChemblID.keys():
        dictDBID_ChemblID[item1[1]]=item1[0]   

df_inchiK =pd.read_csv('outmatches_inchikey_drugnames_chemblids.tsv', header=None, delimiter="\t", encoding='utf-8')
listInchiK=df_inchiK.values
for item2 in listInchiK: 
    dbid=item2[1]
    if dbid not in dictDBID_ChemblID.keys():
        dictDBID_ChemblID[item2[1]]=item2[0]      
    
         
df_smi =pd.read_csv('outmatches_smiles_drugnames_chemblids.tsv',header=None,  delimiter="\t", encoding='utf-8')
listSMI=df_smi.values

for item3 in listSMI:
    dbid=item3[1]
    if dbid not in dictDBID_ChemblID.keys():
        dictDBID_ChemblID[item3[1]]=item3[0]     
            
#outmatches_synonyms
df_synonyms =pd.read_csv('outmatches_synonyms_drugnames_chemblids.tsv',header=None,  delimiter="\t", encoding='utf-8')
listSynonyms=df_synonyms.values
for item4 in listSynonyms:
    dbid=item4[1]
    if dbid not in dictDBID_ChemblID.keys():
        dictDBID_ChemblID[item4[1]]=item4[0] 


print(len(dictDBID_ChemblID))


# In[30]:


#data fusion write all unique matches to new csv - use this for cerating matched relations in neo4j
import csv

count=0
dataArr=dfdb2.values
print(len(dfdb2.values))
for idx in range(len(dfdb2.values)):
    print("ss")
    #print(dataArr[idx])
    break

with open("exact_outallmatches_unique_chemblid_drugnames.tsv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdb2.values)):
        if dataArr[idd][0] in dictDBID_ChemblID.keys():
            item=dataArr[idd]
            cid=dictDBID_ChemblID[dataArr[idd][0]]
            count=count+1
            writer.writerow([cid,item[0],item[2]])       

print("count=",count)


# In[36]:


#find matches based on inchikey - drugbank salts and chembl and write to csv 
import pandas as pd
dfdbsalt =pd.read_csv('drugbank_salt.tsv',delimiter='\t',encoding='utf-8')


print(dfdbsalt.columns[3]) #44=calculated properties
listInchiKey_salt=[]
listInchiKeyOnly_salt=[]
dictExactMatchInchi_saltDB={}
listInchiKey_salt.append(dfdbsalt[dfdbsalt.columns[3]])
#print("total",len(dfdb2.columns['inchikey']))
count=0

for item in dfdbsalt[dfdbsalt.columns[3]]:
    count = count+1
    item=str(item)
    listInchiKeyOnly_salt.append(item) 


dfChemblInchi =pd.read_csv('chembl24inchikey_chemblids.csv',delimiter=',',encoding='utf-8') 
#add to dict chembl id as value and synonyms as key
listChemblInchi= [str(x) for x in dfChemblInchi[dfChemblInchi.columns[0]]]
listChemblIds=[str(x) for x in dfChemblInchi[dfChemblInchi.columns[1]]]


dictChemblInchiIds=dict(zip(listChemblInchi,listChemblIds))

for item in listInchiKeyOnly_salt:   
    if item in dictChemblInchiIds:
        dictExactMatchInchi_saltDB[item]= dictChemblInchiIds[item] 
print(len(dictExactMatchInchi_saltDB))


# In[39]:


#write drugbank salt inchi matches to csv
import csv

count=0
dataArrS=dfdbsalt.values
for idx in range(len(dfdbsalt.values)):
    print("ss")
    print(dataArrS[idx])
    break
    
#add chembl id also to csv matches file 
with open("outmatches_salt_inchikey_drugnames_chemblids.tsv",'w') as outcsv2: 
    writer=csv.writer(outcsv2,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')  
   
    for idd in range(len(dfdbsalt.values)):
        dbinchi=dataArrS[idd][3]
        if dbinchi in dictExactMatchInchi_saltDB.keys():
            count=count+1
            item=dataArrS[idd]  
            chemblid=dictExactMatchInchi_saltDB[dbinchi]
            writer.writerow([chemblid,item[0],item[1]])
print("inchi matches in salt",count)


# In[40]:


#find matches based on name - drugbank salts and chembl and write to csv 
import pandas as pd
dfdbsalt =pd.read_csv('drugbank_salt.tsv',delimiter='\t',encoding='utf-8')


listSaltNames_compoundDB=[]
listSaltExactMatchNames_compoundDB=[]
listChemblNames=[]
dictSaltExactMatchNames_compoundDB={}

#listNames_compoundDB.append(dfdb2[dfdb2.columns[2].lower()])
listSaltNames_compoundDB=[x.lower() for x in dfdbsalt[dfdbsalt.columns[1].lower()]]

print("total",len(dfdbsalt[dfdbsalt.columns[1]]))                    
print(len(listSaltNames_compoundDB))

dfChemblNames =pd.read_csv('chembl24prefnames_ids.csv',delimiter=',',encoding='utf-8') #chembl24prefnames.csv
print(dfChemblNames.shape)

#add to list only contains names
listChemblNames= [str(x).lower() for x in dfChemblNames[dfChemblNames.columns[0]]]

print(len(listChemblNames))

print(type(listChemblNames))
#print(listChemblNames)

#print(listChemblNames[1801523])

for item in listSaltNames_compoundDB:     
    if item in listChemblNames :
        listSaltExactMatchNames_compoundDB.append(item)
        
print(len(listSaltExactMatchNames_compoundDB))
#print(listExactMatchNames_compoundDB)

#add to dict chembl id as value and name as key
listChemblNames= [str(x).lower() for x in dfChemblNames[dfChemblNames.columns[0]]]
listChemblIds=[str(x) for x in dfChemblNames[dfChemblNames.columns[1]]]
dictChemblNamesIds=dict(zip(listChemblNames,listChemblIds))

#consider checking names in drugbank salt to synonmys in chembl
dfChemblSynonyms =pd.read_csv('chembl24_synonyms_ids.csv',delimiter=',',encoding='utf-8')#chembl24_synonyms
listChemblSNames= [str(x).lower() for x in dfChemblSynonyms[dfChemblSynonyms.columns[0]]]
listChemblSIds=[str(x) for x in dfChemblSynonyms[dfChemblSynonyms.columns[1]]]
dictChemblSIds=dict(zip(listChemblSNames,listChemblSIds))
  

        
for item in listSaltNames_compoundDB:   
    if item in dictChemblNamesIds:
        dictSaltExactMatchNames_compoundDB[item]= dictChemblNamesIds[item]  
    if item in dictChemblSIds:
        dictSaltExactMatchNames_compoundDB[item]= dictChemblSIds[item] 
      
       
print(len(dictSaltExactMatchNames_compoundDB))


# In[42]:


#write drugbank salt name matches to csv
import csv

count=0
dataArrS=dfdbsalt.values
for idx in range(len(dfdbsalt.values)):
    print("ss")
    print(dataArrS[idx])
    break
    
#add chembl id also to csv matches file 
with open("outmatches_salt_names_drugnames_chemblids.tsv",'w') as outcsv2: 
    writer=csv.writer(outcsv2,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')  
   
    for idd in range(len(dfdbsalt.values)):
        dbname=str(dataArrS[idd][1]).lower()
        if dbname in dictSaltExactMatchNames_compoundDB.keys():
            count=count+1
            item=dataArrS[idd]  
            chemblid=dictSaltExactMatchNames_compoundDB[dbname]
            writer.writerow([chemblid,item[0],item[1]])
print("name matches in salt",count)


# In[43]:


#data fusion for drugbank salt - find unique out matches 
dictSaltDBID_ChemblID={}

dfsalt_inchi =pd.read_csv('outmatches_salt_inchikey_drugnames_chemblids.tsv', header=None, delimiter="\t", encoding='utf-8')
listSaltInchiids=dfsalt_inchi.values

for item in listSaltInchiids:
    dictSaltDBID_ChemblID[item[1]]=item[0]   

    
dfsalt_name =pd.read_csv('outmatches_salt_names_drugnames_chemblids.tsv', header=None, delimiter="\t", encoding='utf-8')
listSaltNames=dfsalt_name.values
for item1 in listSaltNames: 
    dbid=item1[1]
    if dbid not in dictSaltDBID_ChemblID.keys():
        dictSaltDBID_ChemblID[item1[1]]=item1[0] 
        
print("dict total unique matches in salt",len(dictSaltDBID_ChemblID))


# In[44]:


#data fusion write all unique matches for salt to new csv - use this for creating matched relations in neo4j from salt_drugbank
import csv

count=0
dataArrS=dfdbsalt.values
print(len(dfdbsalt.values))
for idx in range(len(dfdbsalt.values)):
    print("ss")
    #print(dataArr[idx])
    break

with open("exact_outallmatches_unique_salt_chemblid_drugnames.tsv",'w') as outcsv: 
    writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
    for idd in range(len(dfdbsalt.values)):
        if dataArrS[idd][0] in dictSaltDBID_ChemblID.keys():
            item=dataArrS[idd]
            cid=dictSaltDBID_ChemblID[dataArrS[idd][0]]
            count=count+1
            writer.writerow([cid,item[0],item[1]])       

print("count=",count)


# In[354]:


#### not in use #####
### find if partial match exists between overall exact non matches and chembl for name and synonmys 
import pandas as pd #outnonmatches_allfields
dfdbs = pd.read_csv('exact_outnonmatches_allfields.tsv', header=None, delimiter='\t',encoding='utf-8')

print(dfdbs.columns[2]) #2=name
print(dfdbs.columns[28]) 
print(len(dfdbs.columns))

listPartialMatchNames_dfdbs=[]
listPartialMatchSynonyms_dfdbs=[]
listSynonyms_dfdbs=[]
listChemblSynonyms=[]
listNames_dfdbs=[]
dictPartialMatchNames={}
dictPartialMatchSynonyms={}
#listNames_compoundDB.append(dfdb2[dfdb2.columns[2].lower()])
listNames_dfdbs=[str(x).lower() for x in dfdbs[dfdbs.columns[2]]]

print("total",len(dfdbs[dfdbs.columns[2]]))                    
print(len(listNames_dfdbs))
print(listNames_dfdbs[0])

dfChemblSynonyms =pd.read_csv('chembl24_synonyms_ids.csv',delimiter=',',encoding='utf-8')
print(dfChemblSynonyms.shape)
#listChemblNames=dfChemblNames.values.tolist()
#add to dict chembl id as value and synonyms as key
listChemblSNames= [str(x).lower() for x in dfChemblSynonyms[dfChemblSynonyms.columns[0]]]
listChemblSIds=[str(x) for x in dfChemblSynonyms[dfChemblSynonyms.columns[1]]]


dictChemblSIds=dict(zip(listChemblSNames,listChemblSIds))

for key, value in dictChemblSIds.items() :
    print(key, value)
    break  

        
for item in listNames_dfdbs:     
    for name, idval in dictChemblSIds.items(): 
        arrAll = name.split(' ')
        for i in arrAll:            
            if i in item :                
                #listPartialMatchNames_dfdbs.append(i)
                dictPartialMatchNames[item]=idval

                

    
        
print(len(listPartialMatchNames_dfdbs))
#print(listPartialMatchNames_dfdbs)

#synonmys contains  formate |a||||aa||||bb||||b|
for x in dfdbs[dfdbs.columns[28]]:
    x=str(x)
    if '|' in x:
        xall = x.replace('||||','|')
        xarr = xall.split("|")
        for m in xarr:
            if m!= '':
                listSynonyms_dfdbs.append(m.lower())
    else:
        if x!= '':
            m=x
            listSynonyms_dfdbs.append(m.lower())

            
        
for item in listSynonyms_dfdbs:     
    for name, idval in dictChemblSIds.items(): 
        arrAll = name.split(' ')
        for i in arrAll:            
            if i in item :                
                #listPartialMatchSynonyms_dfdbs.append(i)
                dictPartialMatchSynonyms[item]=idval

                

        
print(len(dictPartialMatchSynonyms))
#print(listPartialMatchSynonyms_dfdbs)


# In[353]:


#### not in use #####
#print(listSynonyms_dfdbs)
#print(listPartialMatchSynonyms_dfdbs)
print(len(dictPartialMatchSynonyms))
print(len(dictPartialMatchNames))
for k,v in dictPartialMatchSynonyms.items():
    print(k)


# In[348]:


#### not in use #####
#partial matches based on synonyms between non matched and chembl in a separate csv
import csv

count=0
dataArr2=dfdbs.values
for idx in range(len(dfdbs.values)):
    print("ss")
    #print(dataArr[idx])
    break
print(dfdbs.values[0][2])
            
with open("outmatches_partialnames_nonmatches_chembl.tsv",'w') as outcsv: 
    with open("outmatches_partialnames_nonmatches_chembl_drugnames.tsv",'w') as outcsv2: 
        writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        writer2=csv.writer(outcsv2,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

        for idd in range(len(dfdbs.values)): 
            namedb=dfdbs.values[idd][2].lower()            
            if namedb in dictPartialMatchNames.keys():                       
                for n,val in dictPartialMatchNames.items():
                    if n == namedb:
                        item=dataArr2[idd]            
                        writer.writerow([val, item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                writer2.writerow([val, item[0], item[2]]) 
            
            
with open("outmatches_partialsynonyms_nonmatches_chembl.tsv",'w') as outcsv: 
    with open("outmatches_partialsynonyms_nonmatches_chembl_drugnames.tsv",'w') as outcsv2: 
        writer=csv.writer(outcsv,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        writer2=csv.writer(outcsv2,delimiter='\t',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

        for idd in range(len(dfdbs.values)):            
            bExists=False
            synonyms=str(dfdbs.values[idd][28]).lower()  
            if '|' in synonyms:
                xall = synonyms.replace('||||','|')
                xarr = xall.split("|")
                
                print(xarr)
                for arr in xarr:                    
                    if arr!= '':
                        if 'ergoloid' in arr:
                            print("arr",arr)
                            print("listPartialMatchSynonyms2_dfdbs",listPartialMatchSynonyms2_dfdbs)
                        if str(arr) in dictPartialMatchSynonyms.keys():
                            print("adding",arr)
                            for n,val in dictPartialMatchSynonyms.items():
                                if n == str(arr):                         
                                    item=dataArr2[idd]            
                                    writer.writerow([val, item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                                    writer2.writerow([val, item[0], item[2]])
            else:
                if synonyms in dictPartialMatchSynonyms.keys(): 
                    arr=synonyms
                    for n,val in dictPartialMatchSynonyms.items():
                        if n == str(arr):                         
                            item=dataArr2[idd]            
                            writer.writerow([val, item[0],item[1],item[2],item[3],item[4], item[5],item[6],item[7],item[8],item[9],item[10],
                            item[11],item[12],item[13],item[14], item[15],item[16],item[17],item[18],item[19],item[20],
                             item[21],item[22],item[23],item[24], item[25],item[26],item[27],item[28],item[29],item[30],
                            item[31],item[32],item[33],item[34], item[35],item[36],item[37],item[38],item[39],item[40],
                           item[41],item[42],item[43],item[44], item[45],item[46],item[47],item[48],item[49],item[50],
                               item[51],item[52],item[53],item[54]])
                            writer2.writerow([val, item[0], item[2]])
                                    
               
                            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#below this cell are old code #### not in use #####


# In[2]:


df =pd.read_csv('drugbank_salt.tsv',delimiter='\t',encoding='utf-8')
print(df.shape)


# In[3]:


listSaltsDB=[]
print("total",len(df[df.columns[3]]))

for item in range(len(df[df.columns[3]])):
    if str(df[df.columns[3]][item]) != 'nan':
        listSaltsDB.append(df[df.columns[3]][item])

print('nonempty count',len(listSaltsDB))
print(listSaltsDB)


# In[4]:


dfChembl =pd.read_csv('chembl24inchikey.csv',delimiter='\t',encoding='utf-8')


# In[7]:


print(dfChembl.shape)


# In[8]:


listChemblInchiKey=dfChembl.values.tolist()
print(len(listChemblInchiKey))
#print(listChemblInchiKey)
print(type(listChemblInchiKey))


# In[10]:


#exact matches inchikey
listExactMatch=[]
for item in listChemblInchiKey:
    
    if item[0] in listSaltsDB:
        
        listExactMatch.append(item[0])

print(len(listExactMatch))
        


# In[11]:


dfExactMatchInhcikey = pd.DataFrame(listExactMatch)
dfExactMatchInhcikey.to_csv('ExactMatchesInchiKey.csv', index=False)


# In[15]:


#find match for names
listNamesDB=[]
print("total",len(df[df.columns[1]]))

for item in range(len(df[df.columns[1]])):
    if str(df[df.columns[1]][item]) != 'nan':
        name = str(df[df.columns[1]][item]).lower()
        listNamesDB.append(name)

print('nonempty count',len(listNamesDB))


dfChemblNames =pd.read_csv('chembl24prefnames.csv',delimiter='\t',encoding='utf-8')
print(dfChemblNames.shape)
listChemblNames=dfChemblNames.values.tolist()
print(len(listChemblNames))

print(type(listChemblNames))
listExactMatchNames=[]
for item in listChemblNames: 
    if item[0] != 'NULL' :
        cname=str(item[0]).lower()
        if cname in listNamesDB:        
            listExactMatchNames.append(cname)

print(len(listExactMatchNames))


# In[16]:


')

                #arr2.append(val[1])

                arr2.append(item)

                #

                for item in arr2:

                    val = item.split('::')

                    listSMILESOnlyDB.append(val[1])

      

​

        

             

    print(item)

    if count==10:    

        break;

​

print(len(listSMILESOnlyDB))

print(listSMILESOnlyDB)

calculated_properties_kind_value_source
ctMatchesNames.csv', index=False)


# In[40]:


#check smiles from drugbank drug and compare against chembl
#sample
f = open("samplesmilesinDB.txt", "r")
#print(f.readline())
samplesmi = f.readline()
#samplesmi = str(samplesmi)
#print(samplesmi.split('||'))

arr = samplesmi.split('||')
arr2=[]
for item in arr:
    if 'SMILE' in item:
        #val = samplesmi.split('::')
        #arr2.append(val[1])
        arr2.append(item)

listSMILESDB=[]
for item in arr2:
    val = item.split('::')
    listSMILESDB.append(val[1])
      
print("listSMILESDB",listSMILESDB)


# In[2]:


#get smiles from drugbank-drug
import pandas as pd
dfdb2 =pd.read_csv('drugbank_drug.tsv',delimiter='\t',encoding='utf-8')

print(dfdb2.columns[44])
listSMILESdrugsDB=[]
listSMILESOnlyDB=[]
listSMILESdrugsDB.append(dfdb2[dfdb2.columns[44]])
#print("total",len(dfdb2.columns['inchikey']))
count=0

for item in listSMILESdrugsDB[0]:
    count = count+1
    item=str(item)
    if item != 'nan':
        
        arr = item.split('||')
        arr2=[]
        for item in arr:
            if 'SMILE' in item:
                #val = samplesmi.split('::')
                #arr2.append(val[1])
                arr2.append(item)
                #
                for item in arr2:
                    val = item.split('::')
                    listSMILESOnlyDB.append(val[1])
      

        
             
    #print(item)
    #if count==10:    
     #   break;

print(len(listSMILESOnlyDB))
#print(listSMILESOnlyDB)


# In[3]:


dfChemblsmiles =pd.read_csv('chembl24smiles.csv',delimiter='\t',encoding='utf-8')
print(dfChemblsmiles.shape)


# In[5]:


listChemblSmiles=dfChemblsmiles.values.tolist()
listExactMatchSmiles=[]
for item in listChemblSmiles:
    
    if item[0] in listSMILESOnlyDB:
        
        listExactMatchSmiles.append(item[0])

print(len(listExactMatchSmiles))
        


# In[6]:


dfExactMatchSmiles = pd.DataFrame(listExactMatchSmiles)
dfExactMatchSmiles.to_csv('ExactMatchesSmiles.csv', index=False)


# In[18]:


import pandas as pd
dfdb2 =pd.read_csv('drugbank_drug.tsv',delimiter='\t',encoding='utf-8')


# In[43]:


print(dfdb2.columns)
print(dfdb2.iloc[:3])


# In[27]:


listInchikeydrugsDB=[]
listInchikeydrugsDB.append(dfdb2[dfdb2.columns[52]])
#print("total",len(dfdb2.columns['inchikey']))

#print("total",len(dfdb2[dfdb2.columns['inchikey']]))

'''
for item in range(len(dfdb2[dfdb2.columns[52]])):
    if str(dfdb2[dfdb2.columns[52]][item]) != 'nan':
        listInchikeydrugsDB.append(df[df.columns[52]][item])
'''''
print('nonempty count',len(listInchikeydrugsDB))
print(listInchikeydrugsDB[0])


# In[37]:


#exact matches inchikey
listExactMatch=[]
for item in listInchikeydrugsDB[0]:
    item=str(item)
             
             
    #print(item)
    
    if item != 'nan':
        splitarr = item.split('-')
        if splitarr[0] in listChemblInchiKey:
            listExactMatch.append(item)
        elif splitarr[1] in listChemblInchiKey:
            listExactMatch.append(item)
        else:
            s='do none'
        #break
        

print(len(listExactMatch))


# In[38]:


print(listChemblInchiKey[0])


# In[39]:


#exact matches inchikey
listExactMatch=[]
for item in listChemblInchiKey:
    item=str(item)
             
             
    #print(item)
    
    if item != 'nan':
        splitarr = item.split('-')
        if splitarr[0] in listInchikeydrugsDB[0]:
            listExactMatch.append(item)
        elif splitarr[1] in listInchikeydrugsDB[0]:
            listExactMatch.append(item)
        else:
            s='do none'
        #break
        

print(len(listExactMatch))


# In[41]:


print(listInchikeydrugsDB[0][25])


# In[ ]:




