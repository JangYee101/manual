"""
	a.py为主文件，调用了b.py，但是b.py想使用a.py中的变量
        方案一：直接通过参数传递
        方案二：若b.py为多个文件，考虑全局变量，编辑新文件data.py，将a.py的共享变量移到data.py中，在a.py中设置值，在其他文件中引用值，
                虽然有多次import，但是data.py只会执行一次（python会自动避免重复调用）
"""


#----------------a.py-------------------#
print '\t\t\ta import c start'
from data import c
print '\t\t\ta import c end'
import b
c.setValue(33)
b.printC()


#----------------b.py-------------------#
print '\t\t\tb import c start'
from data import c
print '\t\t\tb import c end'

def printC():
    print c.getValue()


#----------------data.py-------------------#
print 'here is data, i have c'
class ClassC(object):
    
    def __init__(self):
        pass
    def setValue(self, value):
        self.value = value
    def getValue(self):
        return self.value
c = ClassC()
print 'id:',id(c)
