#! /usr/bin/env python
# coding=utf-8

import pymongo

dbname = "pymongo"
collection_name = "info"
dbclient = pymongo.MongoClient("mongodb://localhost:27017/") #连接数据库服务端
db = dbclient[dbname] 					#创建或选择数据库: use pydb

print('\n----------------list_database_names----------------')
dblist = dbclient.list_database_names()	#列出所有的数据库 show dbs
for name in dblist:
	print(name)

print('\n----------------list_collection_names----------------')
collection_list = db.list_collection_names() #列出当前数据库中所有的集合 show collections
for name in collection_list:
	print(name)

info = db[collection_name] 		#创建或选择集合 #db.info db.createCollection("info")
def show_collections():
	for document in info.find():	#查找集合中所有的数据 db.info.find()
		print("name:{name}\t_id:{_id}\n"
			"id:{id}, age:{age}, male:{male}, height:{height}, weight:{weight}\n"
			.format(name=document["name"], _id=document["_id"]
				, id=document["id"], age=document["age"], male=document["male"]
				, height=document["height"], weight=document["weight"]))
	
print('\n----------------find:show_collections----------------')
show_collections()
	
info.drop() #删除所有记录
print('\n----------------insert_one---------------')
Jack = {"id":1, "name":"Jack", "age":31, "male":True, "height":1.90, "weight":89}
print(info.insert_one(Jack))

print('\n----------------insert_many---------------')
Lucy = {"id":2, "name":"Lucy", "age":23, "male":False, "height":1.65, "weight":50}
Lily = {"id":3, "name":"Lily", "age":29, "male":False, "height":1.69, "weight":62}
Justin = {"id":4, "name":"Justin", "age":21, "male":True, "height":1.75, "weight":70}
Tom = {"id":5, "name":"Tom", "age":18, "male":True, "height":1.55, "weight":58}
person_list = [Lucy, Lily, Justin, Tom]
print(info.insert_many(person_list))

print('\n----------------insert the "_id" ---------------')
Jim = {"_id":6, "id":6, "name":"Jim", "age":40, "male":True, "height":1.71, "weight":73}
print(info.insert_one(Jim))

print('\n----------------find_one----------------')
print(info.find_one())

print('\n----------------find 1----------------')
#_id为0时不返回
for document in info.find({}, {"_id":0, "name":1, "male":1}): 
	print(document)

print('\n----------------find 0----------------')	
#_id为0时不返回
for document in info.find({}, {"_id":0, "age":0, "weight":0}): #_id 不能指定为1
	print(document)
	
print('\n----------------sort ASC ---------------')
ASC = 1
for document in info.find({}, {"_id":0, "name":1, "height":1}).sort("height", ASC):
	print(document)
	
print('\n----------------sort DESC ---------------')
DESC = -1
for document in info.find({}, {"_id":0, "name":1, "height":1}).sort("height", DESC):
	print(document)
	
print('\n----------------find equal(==)----------------')
for document in info.find({"male":False}):
	print(document)
	
print('\n----------------find greate than($gt >) 首字母在“L”之后的----------------')
for document in info.find({"name":{"$gte":"L"}}):
	print(document)

print('\n----------------find $regex----------------')
for document in info.find({"name":{"$regex":"^L"}}):
	print(document)
	
print('\n----------------find limit----------------')
for document in info.find({"name":{"$regex":"^.u.*"}}).limit(1): #查找第二个字母是u的记录
	print(document)

print('\n----------------update_one----------------')
query = {"name":"Lucy"}
newvalues = {"$set":{"height":1.66}}
print(info.update_one(query, newvalues))

print('\n----------------update_many----------------')
query = {"male":True}
newvalues = {"$set":{"height":1.99}}
print(info.update_many(query, newvalues))

'''	
#invalid syntax
print('\n----------------aggregate avg----------------')
for document in info.aggregate([{$group:{"_id":"$male", "average_height":{"$avg":"$height"}}}]):
	print(document)
'''


print('\n----------------show_collections----------------')
show_collections()

print('\n----------------delete_one ---------------')
print(info.delete_one({"name":"Lucy"}))

print('\n----------------show_collections----------------')
show_collections()

print('\n----------------delete_many ---------------')
print(info.delete_many({"weight":{"$gte":60, "$lte":70}}))

print('\n----------------show_collections----------------')
show_collections()

print('\n----------------delete_many {} delete all document---------------')
print(info.delete_many({})) #ok

print('\n----------------show_collections----------------')
show_collections()