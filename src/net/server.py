#! /usr/bin/env python
# coding=utf-8

import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serversocket.bind((host, port))
serversocket.listen(5)

while True:
	clientsocket, addr = serversocket.accept()
	
	print("client-addr:%s" % str(addr))
	
	clientsocket.send(b"Hello!") #a bytes-like object
	clientsocket.close()