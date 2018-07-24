# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:57:17 2018

练习6
1.显示4个商品然后打印分割线，只要第一个36个商品信息
2.列出36个商品
3.获取所有的商品并且给商品排序，从低到高排序
4.按照销售量排序
5.商品过滤，只要15天包退的或者包邮的商品信息，显示
@author: 旭宝
"""
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r    #导入联网工具包，打开网址，读取内容为str
data=r.urlopen(url).read().decode('utf-8','ignore')
import json#字符串转字典的工具包
data=json.loads(data)
title=data['mods']['itemlist']['data']['auctions'][0]['title']
price=data['mods']['itemlist']['data']['auctions'][0]['view_price']
print(title)

def sp1():
    for i in range(1,5):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])

def sp2():
    for i in range(5,9):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])
def sp3():
    for i in range(9,13):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])
def sp4():
    for i in range(13,17):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])
def sp5():
    for i in range(17,21):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])
def sp6():
    for i in range(21,25):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])
def sp7():
    for i in range(25,29):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])
def sp8():
    for i in range(29,33):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])
def sp9():
    for i in range(33,37):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])


sp1()
print('-'*101)
sp2()
print('-'*101)
sp3()
print('-'*101)
sp4()
print('-'*101)
sp5()
print('-'*101)
sp6()
print('-'*101)
sp7()
print('-'*101)
sp8()
print('-'*101)
sp9()
print('-'*101)
##优化练习六1,2
def sp():
    for i in range(1,37):
        print('NO'+str(i)+'件商品信息：')
        print(data['mods']['itemlist']['data']['auctions'][i-1]['title'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_price'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['item_loc'])
        print(data['mods']['itemlist']['data']['auctions'][i-1]['view_sales'])
        if i%4==0:
            print('-'*101)
sp()
##商品排序
paixu=[]
def price():
    for j in range(0,36):
        p=float(data['mods']['itemlist']['data']['auctions'][j]['view_price'])
        paixu.append(p)
    return p
price()
a=sorted(paixu)
print('从高到低')
b=list(reversed(a))
print(b)
print('从低到高')
c=list(reversed(b))
print(c)
##按销售排序
xiaoshou=[]
def xs():
    for i in range(0,36):
        x=str(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
        x=x[0:-3]
        xiaoshou.append(int(x))
xs()
a=sorted(xiaoshou)
print('按销售从高到低')
b=sorted(a)
print(b)

####按销售排序
xiaoshou=[]
def xs():
    for i in range(0,36):
        x=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        xiaoshou.append(float(x[0:-3]))
    return x

xs()
a=sorted(xiaoshou)
print('按销售从高到低')
b=list(reversed(a))
print(b)

###包邮不
def youfei():
    for i in range(0,36):
        if float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.0:
            print('第'+str(i+1)+'件商品包邮')
youfei()
c=youfei()
print(c)
    
        
    
       


