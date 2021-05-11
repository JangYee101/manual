#!/usr/bin/python
#coding:utf-8

import unittest

class MyClass(object):
    def addFunc(self, a, b):
        return a + b

    def getList(self):
        return [1,2]

    def returnTrue(self):
        return True


class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(m_cobj.addFunc(1,2), 3)
    
    def test_list(self):
        self.assertEqual(type(m_cobj.getList()), list)

    def test_True(self):
        self.assertTrue(m_cobj.returnTrue())
    
m_cobj = MyClass()


unittest.main()
