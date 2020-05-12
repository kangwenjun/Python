#! /usr/bin/env python
# coding=utf-8

def average(values):
	return sum(values) / len(values)

def __test__():
	import doctest
	doctest.testmod(verbose=True) 
if __name__ == "__main__":
	__test__()
'''
doctest.testmod是测试模块，verbose默认是False,意思是出错才用提示；True，对错都有执行结果
'''