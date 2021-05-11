#!/usr/bin/python
#coding:utf-8

import MySQLdb

#链接数据库
db = MySQLdb.connect('localhost', 'root', 'password', 'the_DB', charset='utf8')
#获取游标
cursor = db.cursor()
#可以不用加分号在sql_str中，加了也不会错
sql_str = "select * from the_table where id = '{the_id}'"   #sql_str.format(the_id=1)   使用{}要用引号
sql_str = "select * from the_table where id = %s"           #使用%s不用引号

opt = '1 or 1=1'#用户恶意输入，简单的sql注入

#错误方法：将查询出所有表内数据
cursor.execute(sql_str % opt)

#正确方法：使用参数化，防止sql注入
cursor.execute(sql_str, opt)
data = cursor.fetchall()
cursor.close()
db.close()
#重要实例

cursor.execute("select * from tb_name")
while True:
    print cursor.fetchone()     #依次打印第1条、第2条·····数据


while True:
    cursor.execute("select max(id) tb_name")
    print cursor.fetchall()[0][0]
    db.commit()                 #一定要加上这一句，不然数据不会更新
    





