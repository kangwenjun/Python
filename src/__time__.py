#! /usr/bin/env python
# coding=utf-8

import time
import os

print('\n----------------utc time----------------')
current_utc_time = time.time()
print("utc:", current_utc_time)#获取utc time

print('\n----------------time.struct_time  "tupletime"----------------')
tm_gmtime = time.gmtime(current_utc_time)
print("gmtime:", tm_gmtime)
assert(0 == tm_gmtime.tm_isdst)

current_gm_utc = time.mktime(tm_gmtime)
print("current gmtime to utc:", current_gm_utc)

tm = time.localtime(current_utc_time)
print("localtime", time.localtime()) #获取time.struct_time
print("localtime-tm:", tm)

print("type(tm):", type(tm))
print("tm_year:", tm.tm_year)
print("tm_isdst:", tm.tm_isdst) #Daylight Saving Time 1:True 0: False -1:unknown

print('\n----------------asctime-tm----------------')
current_asctime = time.asctime(tm)
print("asctime:", current_asctime)
print("asctime from ctime:", time.ctime(current_utc_time))

#%a 本地简化星期名称
#%c 本地相应的日期表示和时间表示
#asctime
asctime_format = "%a %b %d %H:%M:%S %Y"
print("strftime-asctime:", time.strftime(asctime_format, tm))

print('\n----------------strftime----------------')
cntime_format = "%Y-%m-%d %H:%M:%S"
print("strftime:", time.strftime(cntime_format, tm))

print('\n----------------strptime----------------')
some_asctime = "Mon Jun 15 23:23:23 1988"
asctime2strptime = time.strptime(some_asctime, asctime_format) #获取time.struct_time
print("asctime2strptime-some day:", asctime2strptime)
print("asctime2strptime-current:", time.strptime(current_asctime, asctime_format))
print("type(asctime2strptime):", type(asctime2strptime))
assert(type(tm) == type(asctime2strptime))

#print("asctime-tuple:", time.asctime([tm, asctime2strptime])) #illegal

print('\n----------------mktime----------------')
#接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）
#asctime2strptime.tm_isdst = 0# readonly attribute
print("mktime:", time.mktime(asctime2strptime)) #获取utc time tm_isdst=-1

print('\n----------------altzone----------------')
#返回格林威治西部的夏令时地区的偏移秒数
if 1 == tm.tm_isdst:
	print("time.altzone:", time.altzone) #对夏令时启用地区才能使用。
elif 0 == tm.tm_isdst:
	print("time.altzone:is not Daylight Saving Time.") 
else:
	print("time.altzone:is unknown Daylight Saving Time.")
print("current_utc_time-current_gm_utc:", current_utc_time-current_gm_utc)
print("zone by utc:", (current_utc_time-current_gm_utc) // 3600)


print('\n----------------clock----------------')
print("time.perf_counter:", time.perf_counter()) #系统运行时间
print("time.process_time():", time.process_time()) #进程运行时间
time.sleep(1) #休眠1s
print("time.perf_counter-sleep:", time.perf_counter()) #包含休眠时间
print("time.process_time-sleep:", time.process_time()) #不包含休眠时间


print('\n----------------tzset() -- discarded----------------')
#print("os.environ['TZ']:", os.environ['TZ']) #KeyError "TZ"
#os.environ["TZ"] = 'EST+05EDT,M4.1.0,M10.5.0'
#time.tzset()
#print(time.strftime("%X %x %Z"))