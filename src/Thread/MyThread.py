#! /usr/bin/env python
# coding=utf-8

import threading
import time

class MyThread(threading.Thread):
	def __init__(self, id, name, delay_time):
		threading.Thread.__init__(self)
		self.id = id
		self.name = name
		self.delay_time = delay_time
		
	def run(self):
		print("{0} started".format(self.name))
		print_time(self.name, self.delay_time, 5)
		print("{0} stoped".format(self.name))
		
def print_time(name, delay_time, counter):
	while counter:
		time.sleep(delay_time)
		print("%s: %s" % (name, time.ctime(time.time())))
		counter -= 1
		
t1 = MyThread(1, "Thread-1", 1)
t2 = MyThread(2, "Thread-2", 2)

t1.start()
t2.start()
t1.join()
t2.join()
print("exit")