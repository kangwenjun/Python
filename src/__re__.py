#! /usr/bin/env python
# coding=utf-8

import re

print(re.findall(r"\bf[a-z]*", "which foot or hand fell fastest"))
print(re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat"))

print("tea for too".replace("too", "two")) #优先考虑字符串的方法