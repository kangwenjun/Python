#! /usr/bin/env python
# coding=utf-8

import sys;site="www.kangwenjun.com";sys.stdout.write(site);sys.stdout.write("\n")

print("sys.argv:", sys.argv)

sys.stdout.write("2--stdout:info\n")
sys.stderr.write("1--stderr:warn,error\n") # 先输出stderr信息，后输出stdout信息
sys.stdout.write("3--stdout:info\n")

print('\n----------------dir----------------')
print("dir():", dir())
print("dir(sys):", dir(sys))

'''
1--stderr:warn,error
2--stdout:info
3--stdout:info
'''

sys.exit()