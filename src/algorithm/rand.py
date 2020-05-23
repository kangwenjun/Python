#! /usr/bin/env python
# coding=utf-8

import random


print("range(10): ", range(10))

print("random.choice([1, 3, 9, 13, 83]): ", random.choice([1, 3, 9, 13, 83])) #没有choice
print("random.randrange(1, 10, 2): ", random.randrange(1, 10, 2)) #randrange [1,10) step=2
#print("random.randrange(10, 1, 2): ", random.randrange(10, 1, 2)) #错误
print("random.random(): ", random.random()) #[0, 1)

list = [1, 3, 9, 13, 83]
random.shuffle(list)
print("random.shuffle: ", list)

print("random.uniform(1, 10): ", random.uniform(1, 10)) #浮点数 [1,10]
print("random.uniform(10, 1): ", random.uniform(10, 1))

random.seed(1)
print("random.random():", random.random())
random.seed(1)
print("random.random():", random.random())