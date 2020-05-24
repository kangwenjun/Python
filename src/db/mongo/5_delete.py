#! /usr/bin/env python
# coding=utf-8

import pymongo
import random

dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = dbclient["pymongo"]
personal_info = db["personal_info"]

print('\n----------------delete_one ---------------')
id = random.randrange(1, 6)
print(id)
personal_info.delete_one({"id":id})

print('\n----------------delete_many ---------------')
print(personal_info.delete_many({"id":{"$lt":id}}))