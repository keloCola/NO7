# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:28:38 2018
1.加载网络数据(现在不是重点，要会记住，可以复制)
2.解析字典数据(重点分析)
练习题3：
1.通过复制联网天气代码，获取老家的天气字典
2.打印温度temp,天气情况description 天气气压pressure
@author: Administrator
"""
a=b'1'#byte类型
print(a)
import urllib.request as r  #导入联网工具包，   打开网址，读取内容转换为str
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')

import json#字符串转字典的工具包
data=json.loads(data)
data['main']['temp']
data['main']['pressure']
data['weather'][0]['description']
print('温度'+str(data['main']['temp']))
print('天气情况'+str(data['weather'][0]['description']))
print('天气气压'+str(data['main']['pressure']))