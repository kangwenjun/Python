#! /usr/bin/env python
# coding=utf-8

#元素除了是 0、空、None、False 外都算 True
#空元组、空列表返回值为True，这里要特别注意

#assert(False)

print('\n----------------元素除了是 0、空、None、False 外都算 True----------------')
assert(False == all([1, 2, 0]))
assert(False == all([1, 2, ""]))
assert(False == all([1, 2, False]))
assert(False == all([1, 2, None]))

print('\n----------------空元组、空列表返回值为True----------------')
assert(all([])) #找到False即返回，否则返回True
assert(all(()))
assert(all(set()))
assert(all({}))

