# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:12:54 2018
文件的保存：
    创建文件，文件名:喜欢的TV,保存的路径：当前目录，内容
    1.创建文件，文件名:喜欢的TV
    2.内容
    3.保存的路径
    4.设置文本格式
    5.保存到硬盘中
文件的打开：
    1.寻找路径
    2.打开文件
    3.读取内容
    4.关闭文件流


@author: Administrator
"""
######阅读文件会发生的问题，文字编码的问题，乱码？
add='D:\qqyu\喜欢阅读的书.txt'
add='喜欢阅读的书.txt'#####相对路径 和程序在同一个目录下
f=open(add)
ls=f.readlines()   #将文本读取成列表
#s=f.read()     读取文本当中所有的字符
f.close()
###########################
'''
文件的保存：
    创建文件，文件名:喜欢的TV,保存的路径：当前目录，内容
    1.创建文件，文件名:喜欢的TV
    2.内容
    3.保存的路径
    4.设置文本格式
    5.保存到硬盘中
'''
f=open('喜欢的手机.txt','w',encoding='utf-8')#write
f.write('华为mate7')
f.close()#关闭保存程序
#######################append-a追加
f=open('淘宝数据.csv','a',encoding='gbk')#write, ,, , utf-8,gbk
f.write('裙子1,99,972购买\n')
f.write('袜子1,20,9999购买\n')
f.close()#关闭保存程序
#######################
f3=open('喜欢的TV.txt','a',encoding='utf-8')
string=''
for i in rang(10):
    string=string+'cctv-'+str(i)+'\n'
f3.write(string)
f3.close()#关闭保存程序





