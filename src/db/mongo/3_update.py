#! /usr/bin/env python
# coding=utf-8

import pymongo
import random

dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = dbclient["pymongo"]

person_info = db["personal_info"]
student_info = db["student_info"]

print('\n----------------update_one----------------')
query = {"mathematics":{"$lte":random.randrange(59,101)}}
query = {"mathematics":{"$lt":random.randrange(59,101)}}
newvalue = {"$set":{"mathematics":random.randrange(59, 101)}}
print(student_info.update_one(query, newvalue))

print('\n----------------update_many----------------')
print(person_info.update_many({},{"$set":{"best_friend":random.randrange(1, 6)}})) 