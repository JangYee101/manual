#!/usr/bin/python
#coding:utf-8

import os

pipe_file = '/root/current/10-26/pipefile'

fd_w = os.open(pipe_file, os.O_WRONLY)

while True:
    msg = raw_input("please input:")
    os.write(fd_w, msg)
    if msg == "quit":
        print 'Bye!'
        exit()

