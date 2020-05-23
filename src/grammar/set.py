#! /usr/bin/env python
# coding=utf-8

print('\n----------------special set----------------')
print("empty set:\t", set())

print('\n----------------unique----------------')
print('{1, 1, 3, 5, 7, 7}:\t', {1, 1, 3, 5, 7, 7})

print('\n----------------algorithm----------------')
print('{1, 3, 5) - {1, 3}:\t', {1, 3, 5} - {1, 3})	#在集合a当中，集合b没有的元素
print('{1, 3} - {1, 3, 5}:\t', {1, 3} - {1, 3, 5})
print('{1, 3, 5} & {1, 3}:\t', {1, 3, 5} & {1, 3}) 
print('{1, 3, 5} | {1, 3, 7}:\t', {1, 3, 5} | {1, 3, 7})
print('{1, 3, 5} ^ {1, 3, 7}:\t', {1, 3, 5} ^ {1, 3, 7})
print('-:{1, 3, 5}.difference({1, 3}):\t', {1, 3, 5}.difference({1, 3})) #-
data = {1, 3, 5}
data.difference_update({1, 3})
print("difference_update:\t", data)
print("&:{1, 3, 5}.intersection({1, 7, 9}, {1, 11, 111}):\t", {1, 3, 5}.intersection({1, 7, 9}, {1, 11, 111})) #&
data = {1, 3, 5}
data.intersection_update({1, 7, 9}, {1, 11, 111})
print("intersection_update:\t", data)
print("^:symmetric_difference:\t", {1, 3, 5}.symmetric_difference({1, 3, 7})) #^
data = {1, 3, 5}
data.symmetric_difference_update({1, 3, 7})
print("symmetric_difference_update:\t", data)
print("|:{1, 3}.union({5, 7}, {9, 11}):\t", {1, 3, 5}.union({5, 7, 9}, {9, 11, 13})) #|
data = {1, 3, 5}
data.update((1, 7, 9), [1, 2], {3, 4}, {6:"Lucy", 8:"Lily"})
print("update:\t", data)

print('\n----------------is----------------')
print("{1, 3, 5}.isdisjoint({6, 7, 8}):\t", {1, 3, 5}.isdisjoint({6, 7, 8}))
print("{1, 3, 5).isdisjoint({1, 6, 7, 8}):\t", {1, 3, 5}.isdisjoint({1, 6, 7, 8}))
print("{1, 3}.issubset({1, 3, 5}):\t", {1, 3}.issubset({1, 3, 5}))
print("{1, 3, 5}.issuperset({1, 3})\t", {1, 3, 5}.issuperset({1, 3}))

print('\n----------------in not in----------------')
print('1 in {1, 3, 5}:\t', 1 in {1, 3, 5})
print('7 not in (1, 3, 5):\t', 7 not in {1, 3, 5})

print('\n----------------append----------------')
data = {1, 3, 5}
data.add(7)
print("add:\t", data)
data.update((1, 9))
print("update-tuple:\t", data)
data.update([8, 3])
print("update-list:\t", data)
data.update({6:"Lucy", 5:"Lily"})
print("update-dictionary:\t", data)
data.update((11, 12), {13, 14}, {15, 16}, {17:"Tom", 18:"Jack"})
print("update-tuple|list|set|dict:\t", data)

print('\n----------------clear----------------')
data = {1, 3, 5}
if 1 in data :
	data.remove(1)
print("remove:\t", data)
data.discard(1) #不报错

data = set(("Google", "Runoob", "Taobao", "Facebook"))
data.pop()
print("pop(random):\t", data)
data.clear()
print("clear:\t", data)

print('\n----------------copy----------------')
print("{1,3,5}.copy():\t", {1, 3, 5}.copy())

print('\n----------------other----------------')
all = {1, 1.2, True, "name"}
print("all:\t", all)
