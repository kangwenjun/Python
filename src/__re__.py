#! /usr/bin/env python
# coding=utf-8

import re

text = """<!Doctype html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta property="qc:admins" content="465267610762567726375" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Python3 正则表达式</title>

  <link rel='dns-prefetch' href='http://s.w.org' />
<link rel="canonical" href="http://localhost/python3/python3-reg-expressions.html" />
<meta name="keywords" content="Python3 正则表达式">
<meta name="description" content="Python3 正则表达式 正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。   re 模块使 Python 语言拥有全部的正则表达式功能。  compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。  re 模块也提供了与这些方法功能完全一致的函数，..">
		
	<link rel="shortcut icon" href="https://static.localhost/images/favicon.ico" mce_href="//static.localhost/images/favicon.ico" type="image/x-icon" >
	<link rel="stylesheet" href="https:///wp-content/themes/runoob/style.css?v=1.156" type="text/css" media="all" />	
	<link rel="stylesheet" href="https://static.localhost/assets/font-awesome/4.7.0/css/font-awesome.min.css" media="all" />	
  <!--[if gte IE 9]><!-->
  <script src="https://static.localhost/assets/jquery/2.0.3/jquery.min.js"></script>
  <!--<![endif]-->
  <!--[if lt IE 9]>
     <script src="https://cdn.staticfile.org/jquery/1.9.1/jquery.min.js"></script>
     <script src="https://cdn.staticfile.org/html5shiv/r29/html5.min.js"></script>
  <![endif]-->
  <link rel="apple-touch-icon" href="https://static.localhost/images/icon/mobile-icon.png"/>
  <meta name="apple-mobile-web-app-title" content="Python3 正则表达式">
</head>
"""
print('\n----------------match-单行匹配-从头匹配----------------')
print("text-length:", len(text))
result = re.match(".+(html).+", text, re.I|re.U)
print(result)
print("type(re.match):", type(result))
if result:
	print("span:", result.span())
	print("group-html:", result.group(1))

print('\n----------------match-多行匹配-从头匹配----------------')
expression = r".*?href=[\'|\"](.*?)[\'|\"]"
result = re.match(expression, text, re.M|re.S|re.I)
print(result)
if result:
	cnt = len(result.groups())
	print("number of group:", cnt);
	print("groups:", result.groups())
	print(result.group(cnt))

print('\n----------------search-多行匹配-全文搜索并返回第一成功的对象----------------')
result = re.search(expression, text, re.M|re.S|re.I)
print(result)
if result:
	cnt = len(result.groups())
	print("number of group:", cnt);
	print(result.group(cnt))

print('\n----------------re.findall----------------')
result = re.findall(expression, text) # 返回list
print(result)
for url in result:
	print(url)
	
print('\n----------------\b \B----------------')
sentence = "cat in the the hat."
print(sentence)
print("\\b:", re.findall(r"\b[a-z]+", sentence)) #\b单词边界
print("\\B:", re.findall(r"\B[a-z]+", sentence)) #\B非单词边界

print('\n----------------?: 非获取匹配----------------')
result = re.match("industr(?:y|ies)", "industry")
print(result.groups())
assert(0 == len(result.groups()))

result = re.match("industr(y|ies)", "industry")
assert(1 == len(result.groups()))
print(result.groups())

print('\n----------------?= 非获取匹配-正向肯定预查----------------')
result = re.findall("Windows(?=95|98|NT|2000)", "Windows2000")
assert("Windows" == result[0])
result = re.findall("Windows(?=95|98|NT|2000)", "Windows3.1")
assert([] == result)

print('\n----------------?! 非获取匹配-正向否定预查----------------')
result = re.findall("Windows(?!95|98|NT|2000)", "Windows2000")
assert([] == result)
result = re.findall("Windows(?!95|98|NT|2000)", "Windows3.1")
assert("Windows" == result[0])

print('\n----------------?<= 非获取匹配-反向肯定预查----------------')
#result = re.findall("(?<=95|98|NT|2000)Windows", "2000Windows") #result = re.findall("(?<=95|98|NT|2000)Windows", "2000Windows")
result = re.findall("(?<=2000)Windows", "2000Windows") #仅支持固定长度的表达式，不支持或表达式
assert("Windows" == result[0])
result = re.findall("(?<=2000)Windows", "3.1Windows")
assert([] == result)

print('\n----------------?<= 非获取匹配-反向否定预查----------------')
#result = re.findall("(?<!95|98|NT|2000)Windows", "2000Windows") #look-behind requires fixed-width pattern
result = re.findall("(?<!2000)Windows", "2000Windows")
assert([] == result)
result = re.findall("(?<!2000)Windows", "3.1Windows")
assert("Windows" == result[0])

print('\n----------------?<= and ?=----------------')
#?<= 	: 	我断言，我所要提取的目标字符串，它前面的内容一定要匹配表达式<div>
#?= 	:	我断言，我所要提取的目标字符串，它后面的内容一定要匹配表达式</div>
result = re.findall("(?<=<div>).*(?=</div>)", "<div>hello world</div>")
assert("hello world" == result[0])
print(result)

print('\n----------------re.compile----------------')
pattern = re.compile(expression, re.M|re.S|re.I)
print(pattern)
print("type(pattern):", type(pattern))

GROUP_INDEX = 1
START_POS = 0
END_POS = len(text)
result = pattern.match(text, START_POS, END_POS)
print("re.compile-match:", result.group(GROUP_INDEX))
print("start:{0}, end:{1}, span:{2}".format(result.start(GROUP_INDEX), result.end(GROUP_INDEX), result.span(GROUP_INDEX)))

result = pattern.search(text, START_POS, END_POS)
print("re.compile-search:", result.group(GROUP_INDEX))
print("start:{0}, end:{1}, span:{2}".format(result.start(GROUP_INDEX), result.end(GROUP_INDEX), result.span(GROUP_INDEX)))

print("re.compile-findall:", pattern.findall(text, START_POS, END_POS))

print('\n----------------re.finditer----------------')
it = re.finditer(expression, text, re.M|re.S|re.I)
print(it)
print("type(it):", type(it))

index = 1
for match in it:
	print(index, ":", match.group(1))
	index += 1
	
print('\n----------------re.sub----------------')	
result = re.sub(expression, "http://www.kangwenjun.com\n", text, 0, re.M|re.S|re.S)
print(result)

print('\n----------------re.sub-repl----------------')
def double(matched):
	value = int(matched.group("value"))
	return str(value * 2)

print(re.sub("(?P<value>\d+)", double, "Justin23Lucy22Jack25"))

print('\n----------------re.split----------------')	
MAX_SPLIT=0 #分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数
print(re.split("\W+", "Justin, Lucy, Jack", MAX_SPLIT, re.I))

print('\n----------------replace----------------')	
print(re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat")) #\b 描述单词的前或后边界，\B 表示非单词边界
print("tea for too".replace("too", "two")) #优先考虑字符串的方法