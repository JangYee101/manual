#!/usr/bin/python
#coding:utf-8

import socket

sock = socket.socket()
host = '127.0.0.1'
port = 12345
sock.connect((host, port))
sock.send("hello!!!")
print sock.recv(1024)
sock.close()
