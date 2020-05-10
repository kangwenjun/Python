#! /usr/bin/env python
# coding=utf-8

import sys
import shutil

temp_dir = "d:/temp/"
temp_file = temp_dir + "temp"
temp2 = temp_dir + "temp.2"

shutil.copyfile(sys.argv[0], temp_file)
shutil.move(temp_file, temp2)