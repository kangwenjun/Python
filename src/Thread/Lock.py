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
		gLock.acquire()
		print("{0}: {1}".format(name, time.ctime(time.time())))
		gLock.release()
		counter -= 1
		
gLock = threading.Lock()

t1 = MyThread(1, "Thread-1", 1)
t2 = MyThread(2, "Thread-2", 2)
threads = []
threads.append(t1)
threads.append(t2)

for t in threads:
	t.start()

for t in threads:
	t.join()
	
print("exit")
