from pymongo import MongoClient
from data import *
import pprint

client = MongoClient('localhost:27017')
db= client.examples
data = process_map('jeju_south-korea.osm')

[db.jejufile.insert(e) for e in data]


                     
pipeline = [ { "$project" : { "amenity" : "$amenity" }},
                    { "$group" : { "_id" : "$amenity",
                                   "count" : { "$sum" : 1 }}},
                    { "$sort" : { "count" : 1}}]
            
result  = db.jejufile.aggregate(pipeline)['result']
pprint.pprint(result)
