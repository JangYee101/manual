#!/usr/bin/python
#coding:utf-8


import threadpool
import time
from Queue import Queue

print "begin"
def test_func(i):
    while True:
        print queue.get()
        time.sleep(1)

queue = Queue()
for i in range(20):
    queue.put(i)

pool = threadpool.ThreadPool(5)
requests = threadpool.makeRequests(test_func, [i for i in range(5)])
[pool.putRequest(req) for req in requests]
pool.wait()

print "yes"



