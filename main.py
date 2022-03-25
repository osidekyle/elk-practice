import os
import sys

import elasticsearch
from elasticsearch import Elasticsearch
import pandas as pd


es = Elasticsearch([{'host' : 'localhost', 'port' : 9200, 'scheme' : 'http'}])
es.ping()


#es.indices.create(index = 'my-foo', ignore=400)
# res = es.indices.get(index="*")
# for index in res:
#     print(index)
#es.indices.delete(index="my-foo",ignore=[400,404])

# el = {
#     "first_name":"Kyle",
#     "last_name":"Hawkins",
#     "age":24,
#     "about": "Student",
#     "interests" : ["guitar", "computer science"]
# }
# es.indices.create(index = 'testperson', ignore=400)

# res1 = es.index(index="testperson", body=el, id=1)

