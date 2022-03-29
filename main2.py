import elasticsearch
from elasticsearch import Elasticsearch

import pandas as pd
import json
from ast import literal_eval
from tqdm import tqdm
import datetime
import os
import sys

import numpy as np
from elasticsearch import helpers

df = pd.read_csv("netflix_titles.csv")

es = Elasticsearch([{'host' : 'localhost', 'port' : 9200, 'scheme' : 'http'}])


df = df.dropna()

df2 = df.to_dict('records')

def generator(df2):
    for c,line in enumerate(df2):
        yield{
            "_index" : "myelkfirst",
            "_type" : "_doc",
            "_id" : line.get("show_id", None),
            "_source" : {
                "title": line.get("title",""),
                "director": line.get("director", ""),
                "description": line.get("description", ""),
                "duration": line.get("duration", None),
                "cast": line.get("cast", None)
            }
        }
    raise StopIteration


Settings = {
    "settings":{
        "number_of_shards":1,
        "number_of_replicas": 0
    },
    "mappings":{
        "properties":{
            "director":{
                "type":"text"
            }, "duration": {
                "type":"text"
            }
        }
    }
}

my =es.indices.create(index="myelkfirst", ignore=[400,404], body=Settings)


try:
    res = helpers.bulk(es, generator(df2))
    print("working")
except Exception as e:
    print(e)
    pass




