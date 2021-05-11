gcc -g test.c
gdb a.out

#清屏
shell clear

#显示代码
list 1,10

#在第10行打断点
break 10

#查看断点
info breakpoint

#删除断点，两种方法
clear 10    #10 代表的是行号
delete 1    #1 代表断点编号，通过info breakpoint查看

#使断点失效
disable 1   #1 代表断点编号

#运行程序到断点
run

#单步执行
step    #进入函数
next    #不进入函数，直接返回函数结果

#查看变量，例如：int a=2;
print a     #$0=1      查看值
whatis      #type=int    查看类型

#查看函数堆栈（能看到当前运行到的位置）
bt

#退出调试
quit

#设置变量的值，两种方法，例如有变量: int a=1; 
print a=4
set a=4









