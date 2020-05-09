#! /usr/bin/env python
# coding=utf-8


import sys #导入整个模块
from sys import argv,path # 导入特定成员
import __name__ #导入时执行“被导入模块”的程序

sys.stdout.write("Hello World!\n")
print("argv:\t", argv[0])