#! /usr/bin/env python
# coding=utf-8

#["kang", "wen", "jun"]
#["kang", "wen", "jun", [23, 1985]]

#取全部元素
print('\n----------------ALL----------------')
print('["kang", "wen", "jun"]:\t', ["kang", "wen", "jun"])
print('["kang", "wen", "jun"][:]:\t', ["kang", "wen", "jun"][:])
print('["kang", "wen", "jun"][0:]:\t', ["kang", "wen", "jun"][0:])
print('["kang", "wen", "jun"][-1:-1]:\t', ["kang", "wen", "jun"][-1::-1]) #逆向读取


#取一个元素
print('\n----------------ONE----------------')
print('["kang", "wen", "jun"][-1]:\t', ["kang", "wen", "jun"][-1])

#取部分元素
print('\n----------------SOME----------------')
print('["kang", "wen", "jun"][0:-1]:\t', ["kang", "wen", "jun"][0:-1])
print('["kang", "wen", "jun"][0::2]:\t', ["kang", "wen", "jun"][0::2])

#修改元素
print('\n----------------MODIFY----------------')
ls = ["kang", "wen", "jing"]
ls[-1] = "jun"
print('["kang", "wen", "jing"][-1] = "jun":\t', ls)
ls = ["kang", "weng", "jing"]
ls[1:] = ["wen", "jun"]
print('["kang", "weng", "jing"][1:] = ["wen", "jun"]:\t', ls)

#删除
print('\n----------------DEL--------------')
ls = ["kang", "wen", "jun"]
del ls[0]
print('del ["kang", "wen", "jun"][0]:\t', ls)
ls = ["kang", "wen", "jun"]
del ls[0:-1]
print('del ["kang", "wen", "jun"][0:-1]:\t', ls)
ls = ["kang", "wen", "jun"]
ls[0] = []
print('["kang", "wen", "jun"][0] = []:\t', ls)
ls = ["kang", "wen", "jun"]
ls[0:-1] = []
print('["kang", "wen", "jun"][0:-1]:\t', ls)

#拼接
print('\n----------------APPEND--------------')
ls = ["kang", "wen", "jun"]
ls.append(23)
print('["kang", "wen", "jun"].append(23):\t', ls)
print('["kang", "wen", "jun"]+["kang", "wen", "jun"]:\t', ["kang", "wen", "jun"]+["kang", "wen", "jun"])
print('["kang", "wen", "jun"]*2:\t', ["kang", "wen", "jun"]*2)

#扩展
print('\n----------------EXTEND--------------')
ls = ["kang", "wen", "jun"]
#ls.extend(23) #23 not iterable
ls.extend(("age", 23))
ls.extend({'Chinese', 'Japanese'})
ls.extend({"id":"20200503"}) #just key
ls.extend(["American", "Italian"])
print("extend:\t", ls)

print('\n----------------iterator--------------')
ls = ["kang", "wen", "jun"]
for x in ["kang", "wen", "jun"] :
	ls.append(x)
print('["kang", "wen", "jun"]-iterator:\t', ls)

print('\n----------------tupple to list--------------')
print('list(("kang", "wen", "jun")):\t', list(("kang", "wen", "jun")))

print('\n----------------sort--------------')
ls = [9, 7, 3, 5]
ls.sort() #reverse=False
print("sort:\t", ls)
ls = [9, 7, 3, 5]
ls.sort(key=None, reverse=True)
print("sort-reverse=True:\t", ls)

ls =[(2, 2), (3, 4), (4, 1), (1, 3)]
def takeSecond(elem) :
	return elem[1]
ls.sort(key=takeSecond)
print("sort-key:\t", ls)
ls.sort(key=takeSecond, reverse=True)
print("sort-key-reverse:\t", ls)

print('\n----------------clear--------------')
ls = ["kang", "wen", "jun"]
ls.clear()
print("clear:\t", ls)
ls = ["kang", "wen", "jun"]
ls[:] = []
print("ls[:] = []:\t", ls)

print('\n----------------copy--------------')
ls = ["kang", "wen", "jun"]
print("copy:\t", ls.copy())

print('\n----------------OTHER--------------')
print('len(["kang", "wen", "jun"]]:\t', len(["kang", "wen", "jun"]))
print('min([1, 5, 9]):\t', min([1, 5, 9]))
print('max([1, 5, 9]):\t', max([1, 5, 9]))
print('1 in [1, 5, 9]:\t', 1 in [1, 5, 9])
print('10 not in [1, 5, 9]:\t', 10 not in [1, 5, 9])
print('["kang", "wen", "jun", "jun"].count("jun"):\t', ["kang", "wen", "jun", "jun"].count("jun"))
print('["kang", "wen", "jun"].index("wen"):\t', ["kang", "wen", "jun"].index("wen"))
ls = ["kang", "wen", "jun"]
ls.pop() #-1
print("pop-end:\t", ls)
ls = ["kang", "wen", "jun"]
ls.pop(-2)
print("pop:\t", ls)
ls = ["kang", "wen", "jun", "jun"]
ls.remove("jun")
print("remove:\t", ls) #remove first
ls = ["kang", "jun"]
ls.insert(-1, "wen")
print("insert:\t", ls)
ls = ["kang", "wen", "jun"]
ls.reverse()
print("reverse:\t", ls)