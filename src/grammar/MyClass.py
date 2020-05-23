#! /usr/bin/env python
# coding=utf-8

#from enum import IntEnum
from enum import IntEnum, unique #枚举类中的key也不能相同，那么在导入Enum|IntEnum的同时，需要导入unique函数

class tagATTR(IntEnum):
	NAME = 0
	AGE = 1
	WEIGHT = 2
	TREASURE = 3

class MyBase:
	pass
	
class MyClass(MyBase):
	#定义公共属性			#定义私有属性
	def __tell(self, prefix): 	#定义私有方法
		return "{0}:name={1}, age={2}, weight={3}, treasure={4}".format(prefix, self.name, self.age, self.__weight, self.__treasure)
	
	def __init__(self, name="", age=0, weight=0, treasure=0):#构造函数
		self.name = name #使用self动态追加属性
		self.age = age
		self.__weight = weight
		self.__treasure = treasure
	
	def __del__(self): 	#析构函数
		print(self.__tell("__del__"))
		
	def __repr__(self): #必须返回字符串 ,用于repr函数
		return self.__tell("__repr__")
	
	def __str__(self):	#如果没有实现__str__函数，则改调__repr__
		return self.__tell("__str__")
		
	def __call__(self, prefix): 	#将类实列变为可调用的对象，如函数般使用
		return "{0}-{1}".format(prefix, self.__tell("__call__"))
		
	def __getitem__(self, index): #[0]
		if index < 0 or index > 2:
			return None
		else:
			if tagATTR.NAME == index: 		return self.name #枚举类的使用:枚举类不能实列化，直接用"类" + "."
			elif tagATTR.AGE == index: 		return self.age
			elif tagATTR.WEIGHT == index: 	return self.__weight
			elif tagATTR.TREASURE == index: return self.__treasure
	
	def __setitem__(self, index, value): #[0]="Jack"
		if index < 0 or index > 2:
			return False
		else:
			if tagATTR.NAME == index: 		self.name = value
			elif tagATTR.AGE == index:	self.age = value
			elif tagATTR.WEIGHT == index:	self.__weight = value
			elif tagATTR.treasure == index: self.__treasure = value
			
	def __len__(self):
		return len(self.name)
		#return len(self.name) + len(self.age) + len(self.__weight) # int has no len()
	'''	
	#3.0 取消了__cmp__ 使用__eq__和__lt__代替
	def __cmp__(self, other): #按财富从高到低排序
		if self.__treasure == other.__treasure:
			return cmp(self.name, other.name)
		if self.__treasure > other.__treasure:
			return -1 	#排在前面
		elif self.__treasure < other.__treasure:
			return 1 	#排在后面
	'''
	
	def __eq__(self, other):
		return self.__treasure == other.__treasure
	def __lt__(self, other):
		return self.__treasure < other.__treasure

	def __add__(self, treasure):
		return self.__treasure + treasure
		
	def __sub__(self, treasure):
		return self.__treasure - treasure
		
	def __mul__(self, num):
		return self.__treasure * num
		
	def __truediv__(self, num):
		return self.__treasure / num
		
	def __mod__(self, num):
		return self.__treasure % num
		
	def __pow__(self, index):
		return self.__treasure ** index
	
	def ClassName(wwwkangwenjuncom): #第一参数self不是关键字，可以是其他名称，即就是第一个参数就是类对象自身的指针（this）
		print(wwwkangwenjuncom)
		return wwwkangwenjuncom.__class__		#<class '__main__.MyClass'>
		#		return repr(wwwkangwenjuncom.__class__) #<class '__main__.MyClass'>

#实例化类	
Justin = MyClass("justin", 23, 123, 1.23e6)	
#print(Justin.__weight) 		#私有属性不允许外部访问，提示为has no attribute "__weight"
#print(Justin.__tell("test")) 	#私有方法不允许外部访问，提示为has no attribute "__tell"

print('\n----------------repr----------------')
print(repr(Justin))
print(str(Justin)) #如果没有实现__str__函数，则调__repr__
print("len=", len(Justin))

print('\n----------------__call__----------------')
print(Justin("Justin2func"))

print('\n----------------item----------------')
print("name=", Justin[tagATTR.NAME])
print("age=", Justin[tagATTR.AGE])
print("weight=", Justin[tagATTR.WEIGHT])
Justin[tagATTR.NAME] = "Justin"
Justin[tagATTR.AGE] = 32
Justin[tagATTR.WEIGHT] = 120
print(repr(Justin))

#sorted(iterable, cmp=None, key=None, reverse=False)
print('\n----------------sorted by treasure asc----------------')
Lucy = MyClass("Lucy", 22, 80, 1e3)
Jack = MyClass("Jack", 21, 110, 14320)
print(sorted([Lucy, Justin, Jack]))
print('\n----------------sorted by treasure desc----------------')
print(sorted([Lucy, Justin, Jack], reverse=True))

print('\n----------------+ - * / % ^----------------')
print("+\t", Justin + 2000)
print("-\t", Justin - 2000)
print("*\t", Justin * 2)
print("/\t", Justin / 2)
print("%\t", Justin % 10000)
print("^\t", Justin ** 2)

