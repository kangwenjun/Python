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

#startswiths
print("startswith:", "I'm chinese. I'm 23".startswith("I"))
print("startswith-start:", "I'm chinese. I'm 23".startswith("chinese", 4))
print("startswith-start-end:", "I'm chinese. I'm 23".startswith("chinese", 4, -8)) #[4,-8)

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

tabs = "\"\t\"\t\""
print("tabs:\t", tabs.encode("utf-8", "strict"))
tabs = tabs.expandtabs()
print("expandtabs:\t", tabs.encode("utf-8", "strict")) #显示效果一致，但已将水平制表符转为空格

name = "kang wen jun"
index = name.find("wen", 5, -4) #左闭右开
if index > 0 :
	print("index:\t", index)
index = name.rfind("n")
print("rfind:\t", "justin".rfind("in"))
	
index = name.index("wen", 5, -4)
print("index:\t", index)
print("rindex:\t", "kang wen jun".rindex("wen"))
#index = name.index("wen", 5, -5) #跟find()方法一样，只不过如果str不在字符串中会报一个异常.

print("isalnum:\t", "name康文君age23".isalnum()) #UNICODE字符，数字
print("isalpha:\t", "name康文君".isalpha()) #UNICODE字符
print("isdigit:\t", "1一".isdigit()) #False
print("isdecimal:\t", "12334".isdecimal())
print("isnumeric:\t", "½1一3²\u00B2".isnumeric())

print("islower:\t", "justin".islower())
print("isupper:\t", "CHINA".isupper())
print("isspace:\t", "\t \v".isspace())
print("istitle:\t", "China Is Great".istitle()) #如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.

print("lower:\t", "CHINA".lower())
print("upper:\t", "justin".upper())
print("swapcase:\t", "Justin".swapcase())

print("join:\t", "-".join(("kang", "wen", "jun"))) #以-连接各个元素
print("ljust:\t", "justin".ljust(23, "-")) #返回一个原字符串左对齐,并使用空格(可指定字符)填充至指定长度的新字符串。
print("rjust:\t", "justin".rjust(23, "-"))
print("lstrip:\t", "justin".rjust(23, "-").lstrip("-"))
print("rstrip:\t", "justin".ljust(23, "-").rstrip("-"))
print("lstrip-default:\t", "    justin".lstrip())
print("zill:\t", "justin".zfill(10)) #

print("split:", "I'm chinese. I'm 23".split())
print("split-m:", "I'm chinese. I'm 23".split("m"))
print("split-m-1:", "I'm chinese. I'm 23".split("m", 1)) #最多1次分割
print("split-m-0:", "I'm chinese. I'm 23".split("m", 0))

#splitlines
print("splitlines-keepens=False:", "I'm chinese.\nI'm 23 old".splitlines()) #don't keepends
print("splitlines-keepends=True:", "I'm chinese.\nI'm 23 old".splitlines(True)) #keepens
print("splitlines-\\r:", "I'm chinese.\rI'm 23 old".splitlines()) #don't keepends
print("splitlines-\\r\\n:", "I'm chinese.\r\nI'm 23 old".splitlines()) #don't keepends

intab = "aeiou"
outtab = "12345" #长度与intab一致，字符一一对应,如a对应1，并翻译成1
tabtrans = str.maketrans(intab, outtab) #1. 创建内建的映射表
str = "china"
print("maketrans-translate:\t", str.translate(tabtrans)) #2. 按映射表进行转译
print("maketrans-translate:\t", "chinese".translate(tabtrans)) #2. 按映射表进行转译

#bytes.maketrans,bytes.translate
bytes_tabtrans = bytes.maketrans(intab.encode("UTF-8", "strict"), outtab.encode("utf-8", "strict"))
print("bytes-maketrans-translate:\t", b"china".translate(bytes_tabtrans)) #2. 按映射表进行转译
print("bytes-maketrans-translate-delete:\t", b"china".translate(bytes_tabtrans, b"a"))#2. 按映射表进行转译,并删除字母o

print("replace-all:\t", "liao liao wen jun".replace("liao", "kang"))
print("replace-some:\t", "liao liao wen jun".replace("liao", "kang", 1))

#len
print("len-str:\t", len("justin"))
print("len-tupple:\t", len(("kang", "wen", "jun")))
print("len-list:\t", len(["kang", "wen", "jun"]))
print("len-dictionary:\t", len({"name":"justin", "age":23}))
print("len-set:\t", len({"justin", "23"}))

print("max:\t", max("abcde"))
print("min:\t", min("abcde"))