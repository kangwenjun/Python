#! /usr/bin/env python
# coding=utf-8

import sys

sys.stdout.write("2--stdout:info\n")
sys.stderr.write("1--stderr:warn,error\n") # 先输出stderr信息，后输出stdout信息
sys.stdout.write("3--stdout:info\n")
sys.exit()