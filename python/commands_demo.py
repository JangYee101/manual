#!/usr/bin/python
#coding:utf-8

import commands

status, output = commands.getstatusoutput("find -type d -name '*openvas*'")

print status
print output
