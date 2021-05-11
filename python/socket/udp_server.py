#!/usr/bin/python
#coding:utf-8

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 65534))
data, addr = sock.recvfrom(1024)
print "发送者地址：", addr
print "消息：", data
sock.sendto("welcome!!!", addr)
sock.close()
