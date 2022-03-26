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
print(df.head(5))

es = Elasticsearch([{'host' : 'localhost', 'port' : 9200, 'scheme' : 'http'}])

print(es.ping())

print(df.isna().sum())

df = df.dropna()

print(df.isna().sum())

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
                "duration": line.get("duration", None)
            }
        }
        raise StopIteration

mycustom = generator(df2)
print(next(mycustom))


