#! /usr/bin/env python
# coding=utf-8

import os

for root, dirs, files in os.walk("Z:\\Template", topdown=True):
	for name in dirs:
		print(os.path.join(root, name))
	for name in files:
		print(os.path.join(root, name))