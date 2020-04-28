#! /usr/bin/env python
# coding=utf-8

list = ['k', 'a', 'n', 'g']

#取全部元素
print(list)
print(list[:])
print(list[0:])
print(list[-1::-1]) #逆向读取

print(list[-1])
print(list[0:-1])

print(list[0]*2) #* 重复

list2 = ['w', 'e', 'n']
print(list+list2) # +：连接
print((list+list2+['j', 'u', 'n'])[0::2]) #按步长2截取

list[0:2] = [] #删除某段元素
print(list)

list3 = [1, 1.2, 'name', 1+2j]
print(list3)
#list[0] = list[0]+3 #can only concatenate str (not "int") to str
list3[0] = 3 #list 可以修改元素
print(list3)