#!/bin/bash

a=nihao,woshi,jiangye;

IFS=','		#设置分隔符

arr=($a)	#这个括号不能少

echo ${arr[0]}	#根据下标找指定元素

echo ${arr[@]}	#整个数组

echo ${!arr[@]}	#获取所有下标

echo ${#arr[@]}	#获取数组长度

#遍历所有元素
for i in ${arr[@]}
do
echo ${i}
done

