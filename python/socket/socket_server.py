#!/usr/bin/python
#coding:utf-8

import socket

sock = socket.socket()
host = '0.0.0.0'
port = 12345
sock.bind((host, port))
sock.listen(5)
while True:
    clie, addr = sock.accept()
    clie.send('welcome!!!')
    #print '连接地址：', addr
    #print '消息：', clie.recv(1024)
    clie.close()
sock.close()
