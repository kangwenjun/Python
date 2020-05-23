#! /usr/bin/env python
# coding=utf-8

lVal = 20; #long
bVal = True; #bool
fVal = 1.2; #float
cVal = 1+2j; #complex
print(lVal);
print(bVal);
print(fVal);
print(cVal);

lVal = 0x0f; #16进制
print("0x0f: ", lVal);

lVal = 0o10; #八进制
print("0o10: ", lVal);

cVal = complex(fVal, 3.14)
print(cVal);

fVal = 1.2e5
print(fVal);

#强制转换
print("int(fVal): ", int(fVal))
print("float(lVal): ", float(lVal))
print("complex(lVal):", complex(lVal))
print("complex(lVal, bVal): ", complex(lVal, bVal))

"""
 在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。例如：

>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
"""

