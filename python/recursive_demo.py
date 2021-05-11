#!/usr/bin/python
#coding:utf-8


def func(num):
    if num < 3:
        num += 1
        print "num:",num
        num = func(num)     #这个num不能换成其他,因为后面要return num，换成其他return就会错误
    return num


print func(1)

glo_num = 1

def func1():
    global glo_num
    if glo_num < 3:
        glo_num += 1
        func1()

func1()
print glo_num
