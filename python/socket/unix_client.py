#!/usr/bin/python
#coding:utf-8

import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
add_path = './unix.sock'
sock.connect(add_path)
sock.send("hello!!!")
print sock.recv(1024)
sock.close()

