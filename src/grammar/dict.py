#! /usr/bin/env python
# coding=utf-8
# dictinary:键必须不可变，如字符串，数字，tuple
import copy

print('\n----------------special dictionary----------------')
print("{}:\t", {})
print("().keys():\t", {}.keys())
print("().values():\t", {}.values())
print("type({}.keys()):\t", type({}.keys()))
print("type({}.values()):\t", type({}.values()))

print('\n----------------initialization----------------')
print('dict([("Tom", 23), ("Jack", 22)]):\t', dict([("Tom", 23), ("Jack", 22)])) #键值对元组
print('dict(Tom=23, Jack=22):\t', dict(Tom=23, Jack=22)) #构造函数中传入关键字参数，以关键字作为“字符串键”
print('type({"Tom":"23", "Tim":21, "Jack":"China"}.items()):\t', type({"Tom":"23", "Tim":21, "Jack":"China"}.items()))
print('{"Tom":"23", "Tim":21, "Jack":"China"}.items():\t', {"Tom":"23", "Tim":21, "Jack":"China"}.items())

student = {"Tom":"23", "Tim":21, "Jack":"China"}
print('{"Tom":"23", "Tim":21, "Jack":"China"}.keys():\t', {"Tom":"23", "Tim":21, "Jack":"China"}.keys())
print('{"Tom":"23", "Tim":21, "Jack":"China"}.values():\t', {"Tom":"23", "Tim":21, "Jack":"China"}.values())

print('\n----------------value----------------')
print('{"Tom":"23", "Tim":21, "Jack":"China"}["Tome"]:\t', {"Tom":"23", "Tim":21, "Jack":"China"}["Tom"])
student = {"Tom":"23", "Tim":21, "Jack":"China"}
student["Tom"] = 32
print("dict-modify:\t", student)

print('\n----------------clear----------------')
student = {"Tom":"23", "Tim":21, "Jack":"China"}
del student["Tom"]
print("dict-del:\t", student)
student.clear()
print("dict-clear:\t", student)
student = {"Tom":"23", "Tim":21, "Jack":"China"}
student = {}
print("dict = {}:\t", student)

print('\n----------------append----------------')
student = {}
student["Tom"] = 23
print("setdefault-none(existed):\t", student.setdefault("Tom"))
print("setdefault-not existed-none:\t", student.setdefault("Lucy"))
print("setdefault-not existed-value:\t", student.setdefault("Jack", 33))
print("dict-all:\t", student)
student.update({"Lily":21, "Lucy":22})
print("dict-update:\t", student)

print('\n----------------dict----------------')
#print('type(dict(("Tom", 23))):\t', type(dict(("Tom", 23)))) #must be seq
print('type(dict(("Tom", 23))):\t', type(dict((("Tom", 23),)))) #单元素元组
print('type(dict([("Tom", 23), ("Tim", 21), ("Jack", 22)])):\t', type(dict([("Tom", 23), ("Tim", 21), ("Jack", 22)])))
print('dict({("Tom", 23), ("Tim", 21), ("Jack", 22)}):\t', dict({("Tom", 23), ("Tim", 21), ("Jack", 22)}))

print('\n----------------clear----------------')
student = {"Tom":"23", "Tim":21, "Jack":"China"}
student.clear()
print('clear:\t', student)
student = {"Tom":"23", "Tim":21, "Jack":"China"}
student = {}
print('stucent = {}:\t', student)
print('pop-existed:{"Tom":"23", "Tim":21, "Jack":"China"}.pop("Tom"):\t', {"Tom":"23", "Tim":21, "Jack":"China"}.pop("Tom"))
#print('pop-not existed-none:{"Tom":"23", "Tim":21, "Jack":"China"}.pop("Lucy"):\t', {"Tom":"23", "Tim":21, "Jack":"China"}.pop("Lucy")) # key error
print('pop-not existed-23:{"Tom":"23", "Tim":21, "Jack":"China"}.pop("Lucy", 23):\t', {"Tom":"23", "Tim":21, "Jack":"China"}.pop("Lucy", 23))
student = {"Tom":"23", "Tim":21, "Jack":"China"}
print("popitem:\t", student.popitem())
print("after popitem:\t", student)

print('\n----------------copy----------------')
student = {"Tom":"23", "Tim":21, "Jack":"China"}
tmp = student
print("tmp == student:\t", tmp == student)
print("tmp is student:\t", tmp is student)
print("id(tmp) == id(student):\t", id(tmp) == id(student))
print('tmp["Tom"] is student["Tom"]:\t', tmp["Tom"] is student["Tom"])

tmp = student.copy()
print("copy:tmp is student:\t", tmp is student)
print('copy:tmp["Tom"] is student["Tom"]:\t', tmp["Tom"] is student["Tom"])

scores = {"Tom":[98, 88, 90], "Jack":[87, 96, 78]}
tmp = copy.deepcopy(scores)
print("copy.deepcopy:tmp is student:\t", tmp is scores)
print('copy.deepcopy:tmp["Tom"] is student["Tom"]:\t', tmp["Tom"] is scores["Tom"])

print('\n----------------dict.fromkeys----------------')
seq = ("Tom", "Tim", "Jack")
print("dict.fromkeys(seq):\t", dict.fromkeys(seq))
print("dict.fromkeys(seq, 10):\t", dict.fromkeys(seq, 10))

print('\n----------------in not in----------------')
print('"Lucy" not in {"Tom":"23", "Tim":21, "Jack":"China"}:\t', "Lucy" not in {"Tom":"23", "Tim":21, "Jack":"China"})
print('"Tom" in {"Tom":"23", "Tim":21, "Jack":"China"}:\t', "Tom" in {"Tom":"23", "Tim":21, "Jack":"China"})

print('\n----------------get----------------')
print('{"Tom":"23", "Tim":21, "Jack":"China"}.get("Tom"):\t', {"Tom":"23", "Tim":21, "Jack":"China"}.get("Tom"))
print('{"Tom":"23", "Tim":21, "Jack":"China"}.get("Lucy", 33):\t', {"Tom":"23", "Tim":21, "Jack":"China"}.get("Lucy", 33))

print('\n----------------items----------------')
for k, v in {"Tom":"23", "Tim":21}.items():
	print("(", k, ",", v, ")\t", end="")
else:
	print("\n", end="")

print('\n----------------other----------------')
print('len({"Tom":"23", "Tim":21, "Jack":"China"}):\t', len({"Tom":"23", "Tim":21, "Jack":"China"}))
print('str({"Tom":"23", "Tim":21, "Jack":"China"}):\t', str({"Tom":"23", "Tim":21, "Jack":"China"}))
print('type(str({"Tom":"23", "Tim":21, "Jack":"China"})):\t', type(str({"Tom":"23", "Tim":21, "Jack":"China"})))