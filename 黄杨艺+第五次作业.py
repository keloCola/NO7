# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:57:59 2018
练习5
1.优化代码 用函数的方式修改练习4 输出每一天的天气（函数）
2.打印温度折线图，使用函数优化（必须有返回值）

@author: 旭宝
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

def day(a,b):
    print('day'+str(a))
    print('天气'+str(data['list'][b]['weather'][0]['main']))
    c=str(data['list'][b]['weather'][0]['main'])
    
    if c=='Clear':
        print('注意防晒')
    elif c=='Clouds':a
        print('记得带伞哦')
   
day(1,2)
day(2,10)
day(3,18)    
day(4,26)
day(5,34)
##问候


#第二问
def zhexian(a):
    data1=data['list'][a]['main']['temp']
    num=str('-')*int(data1)
    return num
print('五天的折线图')
print('1'+zhexian(2))
print('2'+zhexian(10))
print('3'+zhexian(18))
print('4'+zhexian(26))
print('5'+zhexian(34))