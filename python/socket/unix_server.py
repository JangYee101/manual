#!/usr/bin/python
#coding:utf-8

import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
add_path = './unix.sock'
if os.path.exists(add_path):
    os.remove(add_path)
sock.bind(add_path)
sock.listen(5)
clie, addr = sock.accept()
print "发送者地址：", addr
print "消息：", clie.recv(1024)
clie.send("welcome!!!")
clie.close()
sock.close()
