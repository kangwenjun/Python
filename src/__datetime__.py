#! /usr/bin/env python
# coding=utf-8

from datetime import date

print("today:\t", date.today())

birthday = date(2020, 2, 22) #year month day
print(birthday)
print("type(birthday):\t", type(birthday))
print("today - birthday:\t", date.today() - birthday)