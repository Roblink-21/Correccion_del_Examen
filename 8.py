#!/usr/bin/env python
# coding: utf-8

# In[26]:


import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId


# In[50]:


#conexion con mongodb
client = MongoClient('mongodb://localhost:27017')
try:
    client.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

#Base de datos a seleccionar en nuestro MongoDB Local
DBS = ['Canciones']

client2 = MongoClient('mongodb+srv://esfot:esfot@cluster0.xf99e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
try:
    client2.admin.command('ismaster')
    print('MongoDB connection atlas: Success')
except ConnectionFailure as cf:
    print('MongoDB connection atlas: failed', cf)


#Se crea una base
mongoDB = client2.get_database('Canciones')
db2 = mongoDB.Pop

for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = client[db].list_collection_names()
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    
                    documents=json.loads(json_util.dumps(x))

                    documents["_id"]=str(documents["_id"]["$oid"])


                    print(documents)
                    db2.insert_one(documents)

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e  
                    


# In[ ]:




