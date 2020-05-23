#! /usr/bin/env python
# coding=utf-8

file_name = "py.txt"

def ShowFile(tips, path):
	with open(path, "r") as f:
		print("\n{0}\n{1}, file size:{2}\n".format(tips, f.read(), f.tell()))

f = open(file_name, "w")
size = f.write("www.kangwenjun\t")
f.write("size:{0}".format(size))
f.flush()
f.close()

ShowFile("write:", file_name)
with open(file_name, "a+") as f:
	f.seek(size, 0)
	f.truncate() #从当前位置截断，舍弃当前位置之后的
	f.seek(0, 2)
	print("truncate position:{0}".format(f.tell()))
ShowFile("truncate-default:", file_name)
	
ls = {"1:www.kangwenjun\n", "2:www.kangwenjun\n", "3:www.kangwenjun\n"} #自行制定换行符\n
with open(file_name, "w") as f:
	size = f.writelines(ls) #没有返回值
	f.write("size:{0}".format(size))
	f.flush()
	
ShowFile("writelines:", file_name)
with open(file_name, "a+") as f:
	f.seek(15, 0)
	f.truncate(5) #从文件开始位置截断为5字节
	f.seek(0, 2)
	print("truncate-5 position:{0}".format(f.tell()))
ShowFile("truncate-5:", file_name)