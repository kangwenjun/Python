#! /usr/bin/env python
# coding=utf-8

str="www.kangwenjun.com";

print(str);
print(str[4]); #char
print(str[4:]); #第一点之后
print(str[4:-4]); #两点之间
print(str[4:14]); #两点之间
print(str[4:14:3]); #两点之间,间隔为3个字节的组合
print(str[4:-4] * 2); #两点之间,两次,即重复一次

desc= \
"""

	c/c++
	python
	java
"""

str += desc;

print(str);

print('Hello\tWorld!');
print(r'Hello\tWorld!'); #不发生转义
print(R'Hello\tWorld!'); #不发生转义

str = r'Hello\tWorld!'
print(r"'\t' in str: ", '\t' in str) #FALSE
print(r"'\b' not in str: ", '\b' not in str)

str = 'Hello\tWorld!'
print(r"'\t' in str: ", '\t' in str) #True

name = "kang wen jun"
print("kang: ", "kang" in name)
print("kwj: ", "kwj" not in name)

#c风格字符串格式化
print("My name is %s, I'm %d years old." % ("Justin", 32))

#f-string格式化
print(f"Hello {name}!") #以f开头，用大括号表达式计算后替换进去

#unicode
print("capitalize:", name.capitalize()) #首字母大写，字符串name的元素不可以改变
print("center:", name.center(50, "-")) #宽度50，居中显示，两旁以横杠填充
print("count", name.count("kang")) #count(str, beg= 0,end=len(string))

#encode decode
name = "康文君"
strUtf8 = name.encode("UTF-8") #字符串编码
strGbk = name.encode("GBK") #bytes存储
print("type(strUtf8):", type(strUtf8))
print("type(strGbk):", type(strGbk))
print("name:", name)
print("UTF-8:", strUtf8) #bytes :以16进制等显示
print("GBK:", strGbk)	#bytes :以16进制等显示

utf8ToStr = strUtf8.decode("UTF-8", "strict")
GBKToStr = strGbk.decode("GBK", "strict")
print("type(utf8ToStr):", type(utf8ToStr))
print("type(GBKToStr):", type(GBKToStr))

#endswith
name = "[kang wen jun]"
print("endswith:", name.endswith("]"))
print("endswith-start-end:", name.endswith("wen", 2, -5)) #包括end那个字符

#UTF-8转GBK
print("UTF-8 TO GBK:", strUtf8.decode("utf-8", "strict").encode("GBK", "strict").decode("GBK", "strict"))
print("GBK TO UTF-8:", strGbk.decode("GBK", "strict").encode("UTF-8", "strict").decode("UTF-8", "strict"))

print("\\a:\t", "\"\a\"")
print("\\000:\t", "\"\000\"")
print("\\v:\n", "\"\v\"")
print("\\f:\t", "\"\f\"")
print("\\o10: ", "\o12")
print("\\x10: ", "\x10")
print("\\other: ", "\x10")
