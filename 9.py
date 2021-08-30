#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import pandas as pd


# In[2]:


#conexion con mongodb
client = MongoClient('mongodb+srv://esfot:esfot@cluster0.xf99e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
try:
    client.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

    
#Base de datos a seleccionar en nuestro MongoDB Local
DBS = ['Canciones']

Canciones=[]

for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = client[db].list_collection_names()
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in client[db][col].find():  
                try:
                    
                    documents=json.loads(json_util.dumps(x))

                    print(documents)
                    
                    Canciones.append(documents)
                   

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e 


# In[3]:


Canciones


# In[4]:


#Trasladar la lista a un dateframe
bd1=pd.DataFrame(Canciones)


# In[5]:


#Generar un archivo csv (abrir con excel)
bd1.to_csv('cancionesTokio2021.csv')


# In[ ]:




