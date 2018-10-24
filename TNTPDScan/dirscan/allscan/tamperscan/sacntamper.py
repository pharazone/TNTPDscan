#!/usr/bin/python
#encoding:utf-8

import os
import time
import threading
import urllib2
import requests

def onlyporttamperscan(url, dir, port, times):    #指定url，指定端口扫描目录
    d = dir    #获取指定脚本类型
    if times:
        t = times
    else:
        t = 0
    p = port
    u = 'http://'+url+':'+str(p)
    L = []
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
            'Referer': u,
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }

    for file in L:
        oneurlanddirs(u, file, header, t)

def tamperscan(dir, times):
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

    urls = open(path+"\\result\\portresult.txt", 'r')      #读取扫描的结果
    for url in urls:
        U.append(url.replace('\n', ''))
    urls.close()

    for url in U:
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
            oneurlanddirs(url, file, header, t)



def oneurlanddirs(url, file, header, times):
    try:
        time.sleep(times)
        path = os.path.abspath('.')
        print(url+'/'+file.replace(' ', ''))
        reponse = requests.get(url+'/'+file.replace(' ', ''), timeout=2, headers=header)
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