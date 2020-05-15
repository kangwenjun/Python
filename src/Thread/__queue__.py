#! /usr/bin/env python
# coding=utf-8

import queue
import threading
import time

exit_flag = 0
class MyThread(threading.Thread):
	def __init__(self, id, name, q):
		threading.Thread.__init__(self)
		self.id = id 
		self.name = name
		self.q = q
		
	def run(self):
		print("{0} started".format(self.name))
		process_data(self.name, self.q)
		print("{0} stoped".format(self.name))

def process_data(name, q):
	while not exit_flag:
		gLock.acquire()
		if not q.empty():
			data = q.get()
			gLock.release()
			print("%s processing %s" % (name, data))
		else:
			gLock.release()
		time.sleep(1)

gLock = threading.Lock()
q = queue.Queue(10)
#data = q.get_nowait() #raise empty

threadId = 1
threads = []
threadList = ["Thread-1", "Thread-2", "Thread-3"]
for tName in threadList:
	t = MyThread(1, tName, q)
	t.start()
	threads.append(t)
	threadId += 1
	
nameList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
gLock.acquire()
for word in nameList:
	q.put(word)
gLock.release()

#q.join()
while not q.empty():
	pass
	
exit_flag = 1

for t in threads:
	t.join()
print("exit")