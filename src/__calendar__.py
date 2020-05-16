#! /usr/bin/env python
# coding=utf-8

import time
import calendar

current_tm = time.localtime()

print('\n----------------calendar.month----------------')
widthBetweenDays = 2 	#小于2无效，每日宽度间隔字符数
LinesBetweenWeeds=1 	#上下两行星期间的空行行数
print(calendar.month(current_tm.tm_year, current_tm.tm_mon, widthBetweenDays, LinesBetweenWeeds))

print('\n----------------calendar.monthcalendar----------------')
#月日历二维数组（列表）：非月日历日期（1~31）用0表示
lsCurMonth = calendar.monthcalendar(current_tm.tm_year, current_tm.tm_mon)
print(lsCurMonth)
print("first week days:", lsCurMonth[0])

print('\n----------------calendar.calendar----------------')
#3个月一行
widthBetweenMonths = 6	#每个月之间间隔字符数
widthBetweenDays = 2 	#小于2无效，每日宽度间隔字符数
LinesBetweenWeeds=1 	#上下两行星期间的空行行数
print(calendar.calendar(current_tm.tm_year, widthBetweenDays, LinesBetweenWeeds, widthBetweenMonths))

print('\n----------------calendar.firstweekday()----------------')
print(calendar.firstweekday()) #0:星期一
calendar.setfirstweekday(6) #0~6:星期一至星期日
print(calendar.firstweekday())

print('\n----------------calendar.isleap----------------')
print("year:", current_tm.tm_year) #已经加上1970年
print(calendar.isleap(current_tm.tm_year))

#year1, year2之间的闰年总数
print("year.leapdays:", calendar.leapdays(current_tm.tm_year, current_tm.tm_year+1))

print('\n----------------calendar.monthrange----------------')
monthInfo = calendar.monthrange(current_tm.tm_year, current_tm.tm_mon)
print("type(monthInfo):", type(monthInfo))
print("first wday:", monthInfo[0])
print("It's {0} days in month {1}".format(monthInfo[1], current_tm.tm_mon)) 

print('\n----------------calendar.timegm----------------')
tm_gmtime = time.gmtime()
assert(0 == tm_gmtime.tm_isdst)
print("gmtime:", tm_gmtime)
#print(calendar.timegm(time.localtime()))
print(calendar.timegm(tm_gmtime))

print('\n----------------calendar.weekday----------------')
#0~6:星期一~星期日
print(calendar.weekday(current_tm.tm_year, current_tm.tm_mon, current_tm.tm_mday))
