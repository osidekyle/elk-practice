import elasticsearch
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host' : 'localhost', 'port' : 9200, 'scheme' : 'http'}])

