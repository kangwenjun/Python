#! /usr/bin/env python
# coding=utf-8

from collections import deque
#效率慢
ls = []
ls.append(10)
ls.append(20)
print("list-pop:\t", ls.pop(0))
print("list-pop:\t", ls.pop(0))
#效率慢

q = deque([10, 20, 30])
q.append(1)
q.append(2)
print("deque-popleft:\t", q.popleft())
print("deque-popleft:\t", q.popleft())