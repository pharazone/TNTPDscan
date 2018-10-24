#!/usr/bin/python
#encoding:utf-8

import os
import time
import threading
import urllib2
import requests

def aaa(url, dir, port, times):              #指定url，指定端口扫描目录
    d = dir    #获取指定脚本类型
    t = times  #获取指定扫描延迟时间
    L = []
    U = []
    path = os.path.abspath('.')

    dirresult = open(path+"\\result\\dirscanresult.txt", 'w')   #格式化结果文件
    dirresult.close()

    #print(path+"\\file\\tamper\\"+dir+'.txt')
    files = open(path+"\\file\\tamper\\"+dir+'.txt')    #读取脚本文件
    for file in files:
        L.append(file.replace('\n', ''))
    files.close()


    header = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'DNT': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': url,
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }

    for file in L:
        oneurloneportanddirs(url, dir, port, header, t)

def oneurloneportanddirs(url, file, port, header, times):
    try:
        time.sleep(times)
        url2 = url+str(port)
        path = os.path.abspath('.')
        print(url+'/'+file.replace(' ', ''))
        reponse = requests.get(url2+'/'+file.replace(' ', ''), timeout=2, headers=header)
        code = reponse.status_code
        if code == 200 or code == 302:
            path = os.path.abspath('.')
            rpath = path+"\\result\\dirscanresult.txt"
            #file = r"path+'\\result\\dirscanresult.txt'"
            with open(rpath, 'a+') as f:
                print(url+'/'+file.replace(' ', '')+'-------------------'+str(code))
                f.write(url+'/'+file.replace(' ', '')+'-------------------------'+str(code)+'\n')
                f.close()


    except urllib2.URLError as e:
        pass