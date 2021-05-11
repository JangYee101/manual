#!/usr/bin/python
#coding:utf-8
#不要用os.system和commands.getstatusoutput()来执行命令，因为可能会造成命令注入和资源浪费
import subprocess
import Queue

queue_msg = Queue.Queue()
fd = open('jiangye.txt', 'w')

#a = subprocess.Popen('find / -type d -name "*openvas*"', shell=True, stdout=subprocess.PIPE)   #延时很长
a = subprocess.Popen('cat ../JY/m.log', shell=True, stdout=subprocess.PIPE)     #返回大数据
#info = a.wait()   #不需要
#print info     #0表示成功
#print type(info)   #int
#print a.stdout.read()      #会阻塞，等待stdout有数据读取才返回，但是数据太大会死锁
while True:
    try:
        stdout_msg, stderr_msg = a.communicate()    #与子进程交互，给子进程stdin=None，返回stdout和stderr，防止返回数据太大造成死锁
        print stdout_msg
    except ValueError:
        print "end"
        break
    except:
        print "error"
        exit()


fd.close()
#正确做法：参数化防止命令注入当命令如下时，不会创建aa文件，也不会执行ls -a命令
#a = subprocess.Popen(['ls','-a;touch aa'])
#print a.wait()


#错误做法：当执行如下命令时，会执行ls -a命令，也会创建bb文件
#a = subprocess.Popen('ls -a;touch bb', shell=True)
#print a.wait()

