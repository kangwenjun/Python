#! /usr/bin/env python
# coding=utf-8

import os
import glob

curdir = os.path.abspath(".")
file = os.path.join(curdir, "*.py")
#print(glob.glob(file))		#结果也为绝对路径
print(glob.glob("*.py")) 	#结果也为相对路径