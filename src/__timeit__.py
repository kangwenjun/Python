#! /usr/bin/env python
# coding=utf-8

from timeit import Timer

print(Timer('a,b = b,a', 'a=1; b=2').timeit())
print(Timer('t=a;a=b;b=t', 'a=1;b=2').timeit())