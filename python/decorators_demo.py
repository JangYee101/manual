#!/usr/bin/python
# coding: utf-8

#简单装饰器
def decorato_one(func):
    def wrapper():
        print '------------'
        func()
    return wrapper

@decorato_one
def func_one():
    print 'I am one'

#func带一个参数
def decorato_two(func):
    def wrapper(hello):
        print '------------'
        func(hello)
    return wrapper

@decorato_two
def func_two(hello):
    print 'I am two, %s' % hello

#func带个参数
def decorato_three(func):
    def wrapper(*args, **kwargs):
        print '------------'
        func()
        print args
        print kwargs
    return wrapper

@decorato_three
def func_three():
    print 'I am three'

#装饰器带参数
def decorato_four(name):
    print name
    def wrapper_(func):
       def wrapper(*args, **kwargs):
           print '------------'
           func()
           print args
           print kwargs
       return wrapper
    return wrapper_

@decorato_four('LuoYe')
def func_four():
    print 'I am four'



if __name__ == '__main__':
    func_four(1, 'single', ['l','i','s','t'], ('q','u','t','e','r'), {'d':'i','c':'t'} )
