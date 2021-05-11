>>> a=1
>>> b=None
>>> c=a if a else 2
>>> c
1
>>> c=a if b else 2
>>> c
2


>>> ord('a')
97
>>> chr(97)
'a'
>>> unichr(97)
u'a'
>>> 'a'
'a'
>>> 'a'.decode('utf-8')
u'a'


>>> import traceback
>>> try:
...     print asdf
... except:
...     traceback.print_exc()
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  NameError: name 'asdf' is not defined


>>> time.time()
1537859784.7381001
>>> datetime.datetime.now()
datetime.datetime(2018, 9, 25, 15, 17, 33, 606735)
>>> datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
'2018-09-25 15:18:08'
>>> datetime.datetime.strptime('2018-09-27 17:30:21', "%Y-%m-%d %H:%M:%S")
datetime.datetime(2018, 9, 27, 17, 30, 21)
>>> time.mktime(datetime.datetime.now().timetuple())
1539834385.0
>>> time.mktime(time.strptime('2018-09-25 15:18:08', "%Y-%m-%d %H:%M:%S"))
1537859888.0
>>> time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1537859888.0))
'2018-09-25 15:18:08'
#获取前一天时间
print( (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))


>>> a={'a':'你'}
>>> json.dumps(a)
'{"a": "\\u4f60"}'
>>> json.dumps(a, ensure_ascii=False)
'{"a": "\xe4\xbd\xa0"}'
>>> json.loads(json.dumps(a, ensure_ascii=False))
{u'a': u'\u4f60'}


>>> '\t192.168.1.2     \n    '.strip()
'192.168.1.2'


>>> glob.glob('*')
['option_demo.py', 'unittest_demo.py', 'README.txt', 'sql_demo.py', 'ava_demo.py', 'cmd_demo.py', 'loggin_demo.py']
>>> glob.glob('ava*')
['ava_demo.py']
>>> a[0]
'../python/ava_demo.py'
>>> os.path.basename(a[0])
'ava_demo.py'


>>> add_lambda = lambda x : x+x
>>> add_lambda(1)
2
>>> map(add_lambda, [1,2,3,4,5])
[2, 4, 6, 8, 10]
>>> filter(lambda x : x%2==0, [1,2,3,4,5])
[2, 4]


>>> sys.getsizeof(a)


>>> a=[]
>>> a.extend([1,2,3,4,5,6])
>>> a
[1, 2, 3, 4, 5, 6]

#还未验证
yield val   #阻塞，可以有下面两种方式解除阻塞
1.  func.send("value")      #val = 'value
2.  func.next()             #return val


>>> os.getcwd()     #查看当前路径
'/root'
>>> os.chdir("/root/JY/")       #修改当前路径
>>> os.getcwd()
'/root/JY'
>>> os.__file__     #查看这个包的目录位置
'/usr/lib64/python2.6/os.pyc'


>>> o_obj = object()        #object是一个类，o_obj是一个实例（对象）
>>> type(object)            
<type 'type'>               #类
>>> type(o_obj)
<type 'object'>             #实例
>>> object.__bases__        #查看类的父类
()
>>> o_obj.__class__         #查看实例的类
<type 'object'>


>>fd.seek(p,0)      #移动当文件第p个字节处，绝对位置
>>fd.seek(p,1)      #移动到相对于当前位置之后的p个字节
>>fd.seek(p,2)      #移动到相对文章尾之前的p个字节
>>fd.tell()         #返回文件指针位置
>>fd.truncate({number})    #保留文件开头到number(默认为当前tell())的字符，其他删除



#查找某目录下所有的文件
dir_file = os.walk('.')
>>> for i,j,k in dir_file:
...     print 'i:\t',i
...     print 'j:\t',j
...     print 'k:\t',k
... 
i:  .
j:  ['pipe', 'socket', '.git', 'spider']
k:  ['option_demo.py', 'commands_demo.py', 'lxml_demo.py', 'unittest_demo.py', 'recursive_demo.py', 'shelve_demo.py', 'README.txt', 'sql_demo.py', 'ava_demo.py', 'cmd_demo.py', 'loggin_demo.py', 'threadpool_demo.py']
i:  ./pipe
j:  []
k:  ['pipeserson.py', 'pipeser.py', 'pipecli.py']
i:  ./socket
j:  []
k:  ['unix_server.py', 'udp_client.py', 'unix_client.py', 'ThreadUnixStreamServer_demo.py', 'myre.txt', 'socket_client.py', 'UnixStreamServer_demo.py', 'socket_server.py', 'udp_server.py']
...............................................#内容过多，不一一列举



#dict排序
>>> a
{'1': 'a', '3': 'b', '2': 'c'}
>>> for i in sorted(a):
...     print i
1
2
3
>>> for i in sorted(a,reverse=True):
...     print i
3
2
1


#base64对特殊字符转化，解决在在某些无法使用特殊字符的地方
>>> import base64
>>> a='你\好'
>>> a
'\xe4\xbd\xa0\\\xe5\xa5\xbd'
>>> base64.b64encode(a)
'5L2gXOWlvQ=='
>>> base64.b64decode(base64.b64encode(a))
'\xe4\xbd\xa0\\\xe5\xa5\xbd'




>>> a
[[1, 3], [2, 1]]
>>> sorted(a, key=lambda x: x[1])
[[2, 1], [1, 3]]
>>> sorted(a, key=lambda x: x[0])
[[1, 3], [2, 1]]



>>> a="\u5185\u7f51\u56db\u5ddd\u5927\u5b66\u671b\u6c5f\u6821\u533a"
>>> a
'\\u5185\\u7f51\\u56db\\u5ddd\\u5927\\u5b66\\u671b\\u6c5f\\u6821\\u533a'
>>> print a
\u5185\u7f51\u56db\u5ddd\u5927\u5b66\u671b\u6c5f\u6821\u533a
>>> print a.decode('unicode_escape').encode('utf8')
内网四川大学望江校区




>>> a
1
>>> b
2
>>> a, b = b, a
>>> a
2
>>> b
1
>>> c=0
>>> a>b>c
True


>>> a
[3, 2, 1]
>>> a.reverse()
>>> a
[1, 2, 3]
