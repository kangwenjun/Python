#! /usr/bin/env python
# coding=utf-8

list = ['k', 'a', 'n', 'g']
print(list)
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