#!/usr/bin/python
#coding:utf-8

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr_port = ('127.0.0.1', 65534)
sock.sendto("hello!!!", addr_port)
print sock.recv(1024)
sock.close()
