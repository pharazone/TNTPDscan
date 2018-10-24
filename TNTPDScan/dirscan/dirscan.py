#!/usr/bin/python
#encoding:utf-8

import time
import threading
import requests
from listall.listtamper import *
from listall.lsitcms import *
from listall.listleaks import *
from allscan.tamperscan.sacntamper import *
from allscan.adminscan.adminscan import *

def scanurlonlyportanddir(url, dir, port, times):   #指定url，指定端口扫描目录
    dirscan2(url, dir, port, times)


def scanurlportanddir(url, dir, times):      #先扫描端口，然后再根据存活端口扫描目录

    file1 = open('result/portresult.txt','w')
    file1.close()
    so(url,dir, times)
    time.sleep(1)

def so(url, dir, times):
    for port in range(1, 65536):
        try:
            t = threading.Thread(target=scan, args=(url, port, dir, times,))
            t.start()
        except:
            pass

def scan(url, port, dir, times):
    try:
        header = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'DNT': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://'+url,
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }

        url2 = "http://"+url+":"+str(port)
        if port == 3:
            url2 = "https://"+url

        if port % 3 == 0 or port == 65535:
            print(url2)


        if port == 100:
            time.sleep(2)
            print("\r\n\r\n")
            print("端口扫描完毕，开始扫描目录，请稍后".decode("utf-8").encode("gbk"))
            print("****************OK********************")
            dirscan2('', dir, '', times)

        reponse = requests.get(url2, timeout=3, headers=header)
        code = reponse.status_code
        banner = reponse.headers['Server'][:20]

        if code == 200 or code == 302 or code == 404 or code == 403 or code == 500:
            print(url2+'--'+str(code)+'***************端口存活'.decode("utf-8").encode("gbk"))
            file = r'result/portresult.txt'

            with open(file, 'a+') as f:
                f.write(url2+'\n')
                f.close()

    except Exception as a:
        pass

def dirscan2(url, dir, port, times):
    #print("目录开始扫描-------------------------------------------".decode("utf-8").encode("gbk"))
    time.sleep(1)

    tampers = ['asp', 'aspx', 'php', 'jsp', 'mdb', 'py', 'cfm', 'cgi', 'ini', 'sql', 'xml', 'all', 'pack']   #脚本类型

    if times:         #判断延迟时间
        t = times
    else:
        t = 0

    if dir == 'list.tamper':
        listtamper()             #此处输出tamper下的目录 ,完成

    elif dir == 'list.cms':
        listcms()             #此处输出cms下的目录 ,完成

    elif dir == 'list.leaks':
        listleaks()            #此处输出leaks下的目录 ,完成

    elif dir == 'cms':
        print("功能暂未实现".decode("utf-8").encode("gbk"))             #此处进行开源cms目录扫描

    elif dir == 'leaks':
        print("功能暂未实现".decode("utf-8").encode("gbk"))             #此处进行开源漏洞集合扫描

    elif dir in tampers:
        if port:
            onlyporttamperscan(url, dir, port, times)
        else:
            tamperscan(dir, t)               #此处为指定脚本扫描

    elif dir == 'admin':        #后台目录扫描
        if port:
           onlyporthoutaiscan(url, dir, port, times)
        else:
            houtaiscan(dir, t)               #此处为指定脚本扫描

    elif dir == 'common':       #常用高频目录字典扫描
        print("功能暂未实现".decode("utf-8").encode("gbk"))

    elif dir == 'other':        #自定义目录字典扫描
        print("功能暂未实现".decode("utf-8").encode("gbk"))

    else:
        print("目录指定错误".decode("utf-8").encode("gbk"))


