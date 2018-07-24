# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:57:56 2018
练习8：保存淘宝数据(小组项目)
1.每个组员爬取某个商品的100页数据 每个组员爬取的不同的城市，上海 北京 成都 郑州 组间城市不重复
2.保存淘宝商品信息(同练习题6)，并且保存为csv格式
3.每组组长合并各组员的数据  -后续班级合并数据
@author: 旭宝
"""
import json
import urllib.request as r
import time
word = r.quote('裙子')
url = 'https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E8%BE%BD%E5%AE%81&ajax=true'
itemList = []

def reqTimeOut(url,timeOut):
    for i in range(0,100):
        urlPage = url + '&s=' + str(i*44)
        try:
            req = r.urlopen(urlPage)
            if req.getcode()==200:
                data = req.read().decode('utf-8','ignore')
        except Exception as err:
            print('网络请求错误,正在重试中。。。')
            i = i-1
            break
        data = json.loads(data)
        try:
            fileURL = open('辽宁.txt','a+',encoding='utf-8')
#            fileList = open('reqList.txt','w',encoding='utf-8')
            fileURL.write(urlPage+'\n')
            fileURL.close()
        except Exception as err:
            print('文件写入错误！重试中。。。')
            break
        itemList.append(data['mods']['itemlist']['data']['auctions'])
        print('爬去第'+str(i+1)+'页成功')
        time.sleep(timeOut)
reqTimeOut(url,5)
