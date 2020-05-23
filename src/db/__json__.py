#! /usr/bin/env python
# coding=utf-8

import json
Jack = {"name":"Jack", "age":24, "is_male":False, "amount":2345.3, "other":None}
Lucy = {"name":"Lucy", "age":22, "is_male":True, "amount":1223.3, "other:":"Long hair"}
Justin = {"name":"Justin", "age":23, "is_male":False, "amount":98564.3, "other":"C++"}
students = [Jack, Lucy, Justin]

print('\n----------------python to json----------------')
json_str = json.dumps(students)
print("python to json:\t", json_str)

with open("students.json", "w") as f:
	json.dump(students, f)
	
print('\n----------------json file to python----------------')
with open("students.json") as f:
	data = json.load(f)
print("json file to pythyon:\t", data)
print("json str to python:\t", json.loads(json_str))