#! /usr/bin/env python
# coding=utf-8

import pickle

print('\n----------------dump load----------------')
file = "pickel.bin"
ls = [1, (2, 3), [4, 5], {6, 7}, {8:"8", 9:"9"}, 1.1, True, 1+2j, None]
with open(file, "wb") as f:
	pickle.dump(ls, f)

tmp = ""
with open(file, "rb") as f:
	tmp = pickle.load(f)
print("load:", tmp)
print("tmp==ls:", tmp==ls)

print('\n----------------dumps----------------')
ls2bytes = pickle.dumps(ls)
print("type(ls2bytes):", type(ls2bytes))
print(ls2bytes)

print('\n----------------loads----------------')
bytes2ls = pickle.loads(ls2bytes)
print("type(bytes2ls):", type(bytes2ls))
print(bytes2ls)
print("bytes2ls == ls:", bytes2ls == ls)