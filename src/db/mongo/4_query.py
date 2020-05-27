#! /usr/bin/env python
# coding=utf-8

import pymongo

#集群部署
#dbclient = pymongo.MongoClient("mongodb://localhost:27017,localhost:27018/?slaveOk=true")
dbclient = pymongo.MongoClient("mongodb://localhost:40000/pymongo?wtimeoutMS=1000&socketTimeoutMS=1000&connectTimeoutMS=1000") #连接分片集群route

print('\n----------------MongoClient----------------')
print("type(pymongo.MongoClient):", type(dbclient))
print(dbclient)

print('\n----------------show dbs----------------')
dbs = dbclient.list_database_names()
print("type(dbs):", type(dbs))
print(dbs)

dbname = "pymongo"
if dbname not in dbs:
	print("database {0} was not existed!".format(dbname))
	exit()
	
db = dbclient[dbname]
print('\n----------------database info----------------')
print("type(db):", type(db))
print("database info:", db)

collections = db.list_collection_names()
print('\n----------------show collections----------------')
print("type(collections):", type(collections))
print(collections)

student_info_name = "student_info"
if student_info_name not in collections:
	print("collection \"{0}\" was not existed in database \"{1}\"!".format(student_info_name, dbname))
	exit()	
	
def QueryPersonalInfo(info):
	ret = {}
	dbname = info["db"]
	if dbname not in dbs:
		return None
		
	db = dbclient[dbname]
	collection_name = info["ref"]
	if collection_name not in db.list_collection_names():
		return None
	
	personal_info = db[collection_name]
	return personal_info.find({"_id":info["_id"]})	
	
def ShowStudentInfo(student):
	info = student["personal_info"]
	if not isinstance(info, dict):
		return "None"

	CurDbName = info["db"]
	if CurDbName not in dbs:
		return
		
	CurDb = dbclient[CurDbName]
	CurColName = info["ref"]
	if CurColName not in CurDb.list_collection_names():
		return
	
	CurCol = CurDb[CurColName]
	theCursor = CurCol.find({"_id":info["id"]}, {"_id":0})
	lsInfo = list(theCursor)
	someone = {}
	if len(lsInfo):
		someone = lsInfo[0]
	
	print("name:{name} \t id-card:{id}\n" \
			"height:{height}m \t weight:{weight}Kg \t age:{age} \t best friend:{best_friend}\n" \
			"student no:{no} \t mathematics:{math} \t chinese:{chinese} \t english:{english}\n" \
			.format(name=someone["name"], id=someone["id"]
			, height=someone["height"], weight=someone["weight"], age=someone["age"], best_friend=someone["best_friend"]
			, no=student["id"], math=student["mathematics"], chinese=student["chinese"],english=student["english"]
			))
	
ASC = 1
DESC = -1
student_info = db[student_info_name]
print('\n----------------show student_info----------------')
cursor = student_info.find({}, {"_id":0}).sort("id", ASC).limit(5)
ls = list(cursor)
for student in ls:
	ShowStudentInfo(student)

print('\n----------------find_one----------------')
ShowStudentInfo(student_info.find_one()) #find_one:返回dict

print('\n----------------find >----------------')
cursor = student_info.find({"mathematics":{"$gt":80}})
ls = list(cursor)
for student in ls:
	ShowStudentInfo(student)

print('\n----------------find $regex----------------')
personal_info = db["personal_info"]
cursor = personal_info.find({"name":{"$regex":"^.u.*"}}, {"_id":1})
ls = list(cursor)
for info in ls:
	_id = info["_id"]
	cursor = student_info.find({"personal_info":{"ref":"personal_info", "id":_id, "db":dbname}})
	lsStudent = list(cursor)
	for student in lsStudent:
		ShowStudentInfo(student)