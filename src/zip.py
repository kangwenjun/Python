#! /usr/bin/env python
# coding=utf-8

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

#同时遍历两个或更多的序列
for q, a in zip(questions, answers):
	print("What is your {0}, It is {1}.".format(q, a))