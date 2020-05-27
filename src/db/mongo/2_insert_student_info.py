#! /usr/bin/env python
# coding=utf-8

import pymongo
import random

#dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
dbclient = pymongo.MongoClient("mongodb://localhost:40000/pymongo?wtimeoutMS=1000&socketTimeoutMS=1000&connectTimeoutMS=1000") #连接分片集群route
dbs = dbclient.list_database_names()
print("show dbs:", dbs)

dbname = "pymongo"
db = dbclient[dbname]
collections = db.list_collection_names()
print("show collections:", collections)

personal_info_name = "personal_info" 
personal_info = db[personal_info_name]
if personal_info_name not in collections:
	print("{0} was not existed!".format(personal_info_name))
	exit()
	
student_info_name = "student_info"
student_info = db[student_info_name]
if student_info_name in collections:
	print(student_info.drop())

ASC = 1
DESC = -1
def getLastStudentId():
	cursor = student_info.find({}, {"_id":0, "id":1}).sort("id", DESC).limit(1)
	ls = list(cursor)
	if len(ls):
		return ls[0]["id"] + 1
	return 2005235101
	
def InsertOne(id, math, cn, en):
	global personal_info
	cursor = personal_info.find({"id":id}, {"_id":1}).limit(1)
	ls = list(cursor)
	if len(ls):
		theinfo = ls[0]
		somebody = {"ref":personal_info_name, "id":theinfo["_id"], "db":dbname} #$ref $_id $db
		student = {"id":getLastStudentId(), "personal_info":somebody
						, "mathematics":math, "chinese":cn, "english":en}
		print(student)
		return student_info.insert_one(student)				
	
print('\n----------------insert_one----------------')
cursor = personal_info.find({}, {"_id":0, "id":1})
for info in cursor:
	print(InsertOne(info["id"]
			, random.randrange(59,101)
			, random.randrange(59,101)
			, random.randrange(59,101)))