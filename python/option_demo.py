#!/usr/bin/python
#coding:utf-8
#参数解析

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-n', '--name', action='store', dest='name')
parser.add_option('-e', '--email', action='store', dest='email', default='nothing')
parser.add_option('-t', '--true', action='store_true', dest='true')
parser.add_option('-f', '--false', action='store_false', dest='false')

options, args = parser.parse_args()
print options.name
print options.email
print options.true
print options.false
