#! /usr/bin/env python
# coding=utf-8

import pymongo

#dbclient = pymongo.MongoClient("mongodb://localhost:27017/pymongo?wtimeoutMS=1000&socketTimeoutMS=1000&connectTimeoutMS=1000") #连接数据库服务端
dbclient = pymongo.MongoClient("mongodb://localhost:40000/pymongo?wtimeoutMS=1000&socketTimeoutMS=1000&connectTimeoutMS=1000") #连接分片集群route
#print(dbclient) #关键信息为上述信息

dbs = dbclient.list_database_names()	#连接数据库并获取数据库列表 show dbs
print("list_database_names:", dbs) 		

dbname = "pymongo"
db = dbclient[dbname]
#print(db) #关键信息为上述信息
collections = db.list_collection_names() # show collections
print("list_collection_names:", collections)


collection_name = "personal_info"
personal_info = db[collection_name]
if collection_name in collections:
	print(personal_info.drop())

print('\n----------------insert_one----------------')
Jack = {"id":1, "name":"Jack", "age":31, "male":True, "height":1.90, "weight":89}
print(personal_info.insert_one(Jack))

print('\n----------------insert_many----------------')
Lucy = {"id":2, "name":"Lucy", "age":23, "male":False, "height":1.65, "weight":50}
Lily = {"id":3, "name":"Lily", "age":29, "male":False, "height":1.69, "weight":62}
Justin = {"id":4, "name":"Justin", "age":21, "male":True, "height":1.75, "weight":70}
Tom = {"id":5, "name":"Tom", "age":18, "male":True, "height":1.55, "weight":58}
personal_list = [Lucy, Lily, Justin, Tom]
print(personal_info.insert_many(personal_list))

print('\n----------------insert_one the _id----------------')
Jim = {"_id":6, "id":6, "name":"Jim", "age":40, "male":True, "height":1.71, "weight":73}
print(personal_info.insert_one(Jim))

