#!/usr/bin/python
#coding:utf-8

import SocketServer
import os
import threading
import time

thread_lock_100 = threading.Semaphore(300)

class MyHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print self.request.recv(1024)
        #self.request.send("welcome!!!")
        thread_lock_100.acquire()
        with open('./myre.txt','a') as fd:
            fd.write('a\n')
        time.sleep(1)
        thread_lock_100.release()


addr_path = './unix.sock'
if os.path.exists(addr_path):
    os.remove(addr_path)
#server = SocketServer.UnixStreamServer(addr_path, MyHandler)
server = SocketServer.ThreadingUnixStreamServer(addr_path, MyHandler)
server.serve_forever()
