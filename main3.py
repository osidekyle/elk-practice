import elasticsearch
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host' : 'localhost', 'port' : 9200, 'scheme' : 'http'}])

Settings = {
    'settings': {
        'number_of_shards':1,
        'number_of_replicas':0
    },
    'mappings':{
    'properties':{
        'myloc':{
            'type':'geo_point'
        }
    }
    }
}


my = es.indices.create(index="hawkins", ignore=400, body=Settings)

sample = {
    'myloc':{
        'lat':48.75,
        'lon':-122.48
    }
}

res1 = es.index(index="hawkins", body=sample, id=1)