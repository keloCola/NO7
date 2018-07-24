# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:49:22 2018
第十次作业：获取全国高校信息
1.获取2300所学校编号
2.获取31所城市编号
3.获取142000数据，31/10，每组三个城市,后面组装在一起
4.将142600数据使用spark统计
@author: 旭宝
"""
"""

url_ajaxGetMajor='http://www.gaokaopai.com/university-ajaxGetMajor.html'
#请求头信息
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}
req_W=r.Request(url_ajaxGetMajor,data='id={}&type=1&city={}&state=1'.format(school,city).encode(),headers=headers)
req_L=r.Request(url_ajaxGetMajor,data='id={}&type=2&city={}&state=1'.format(school,city).encode(),headers=headers)
#发送请求并获取数据到data中
data_W=r.urlopen(req_W).read().decode('utf-8','ignore')
data_L=r.urlopen(req_L).read().decode('utf-8','ignore')
print(data_W + '\n\n\n')
print(data_L + '\n\n\n')
"""
"""
#获取高校ID列表，并存储在allSchoolId.txt文件中
schoolId = {}
fileSchoolId = open('all_school.txt','r',encoding='utf-8')
#循环读取文件每一行
while True:
    lines = fileSchoolId.readline() # 整行读取数据
    #为空行则遍历文件结束，退出循环
    if not lines:
        break
    try:
        strSchool = re.findall(u"[\u4e00-\u9fa5]+|[0-9]\d*",lines)[0]
        strSchoolId = re.findall(r"[0-9]\d*",lines)[0]
        schoolId[strSchoolId] = strSchool
    except Exception as err:
        print('该行查询失败，重试中。。。')
        continue
fileSchoolId.close()
#将数据写入allSchoolId.txt文件中
writeInfo(schoolId,'allSchoolId.txt','a+','utf-8')
"""

import urllib.request as r
import json
#发送请求函数，三个参数都是int类型
def ajaxGetMajor(schoolId,cityId,type):
    #请求地址
    url_ajaxGetMajor = 'http://www.gaokaopai.com/university-ajaxGetMajor.html'
    #请求头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'}
    try:
        #拼接后的请求地址
        req = r.Request(url_ajaxGetMajor,data='id={}&type={}&city={}&state=1'.format(schoolId,type,cityId).encode(),headers=headers)
        #获取请求信息
        data = r.urlopen(req).read().decode('utf-8','ignore')
    except Exception as err:
        print('网络请求错误！')
    #请求结果为str，转化为字典
    data = json.loads(data)
    #添加返回结果信息，加入了schoolId、cityId、type
    data["schoolId"] = str(schoolId)
    data["cityId"] = str(cityId)
    data["type"] = type
    return data
#将数据写入文件，传入数据字典dictData,文件名flieName（没有则创建）（str）,写入方式TYPE（str）,写入的编码ENCODE（str）
def writeInfo(dictData,flieName,TYPE,ENCODE):
    try:
        #打开文件
        file = open(flieName,TYPE,encoding=ENCODE)
        #将字典dictData转化为str
        str = json.dumps(dictData)
        #写入文件，将数据放置缓存区中
        file.write(str + '\n')
        #关闭文件，将缓存区数据写入文件，关闭文件
        file.close()
    except Exception as err:
        print('文件写入dictData错误！')

#获取高校ID列表，并存储在allSchoolId.txt文件中
schoolId = {}
fileSchoolId = open('all_school.txt','r',encoding='utf-8')
#循环读取文件每一行
while True:
    lines = fileSchoolId.readline() # 整行读取数据
    #为空行则遍历文件结束，退出循环
    if not lines:
        break
    try:
        strSchool = re.findall(u"[\u4e00-\u9fa5]+|[0-9]\d*",lines)[0]
        strSchoolId = re.findall(r"[0-9]\d*",lines)[0]
        schoolId[strSchoolId] = strSchool
    except Exception as err:
        print('该行查询失败，重试中。。。')
        continue
fileSchoolId.close()
#将数据写入allSchoolId.txt文件中writeInfo(schoolId,'allSchoolId.txt','a+','utf-8')

'''
fileSchoolId = open('all_school.txt','r',encoding='utf-8')
data = json.loads(fileSchoolId.readline())
lenData = len(data)
schoolIdList = list(data.keys())
fileSchoolId.close()
#获取城市，放到cityList列表中
cityId = [11,12,13,14,15,21,22,23,31,32,33,34,35,36,37,41,42,43,44,45,46,50,51,52,53,54,61,62,63,64,65]
#cityId = [11]
#这是主进程，为了提高性能后期选择多线程
for schools in range(len(schoolIdList)):
    school = schoolIdList[schools]
    for citys in range(len(cityId)):
        city = cityId[citys]
        for i in range(2):
            try:
                dataMajor = ajaxGetMajor(school,city,i+1)
            except Exception as err:
                print('获取数据失败！不重试了，跳过该学校在该城市的数据，记录在错误文件中。。。\n')
                dataError = {}
                dataError["id"] = school
                dataError["学校"] = data[school]
                dataError["城市"] = city
                writeInfo(dataError,'all_school.txt','a+','gbk')
                break
            try:
                writeInfo(dataMajor,'school/'+data[school]+'.txt','a+','gbk')
            except Exception as err:
                print('写入数据失败！重试中。。。')
                continue
        print("获取学校{}在城市{}的招生计划数据成功！".format(school,city))
    #添加日志文件，记录已经成功写入的文件
    #还未获取的
    del data[school]#在学校字典中删除当前已经获取的学校ID
    writeInfo(data,'log/还未获取的学校ID.txt','w','gbk')
    print("******学校{}数据获取成功,进度：{}/{}******".format(school,schools+1,lenData))









