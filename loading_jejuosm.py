
from pymongo import MongoClient
from data import *
import pprint

client = MongoClient('localhost:27017')
db= client.examples
data = process_map('jeju_south-korea.osm')

[db.jejufile.insert(e) for e in data]


    
