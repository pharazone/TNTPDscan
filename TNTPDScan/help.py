#!/usr/bin/python
#encoding:utf-8

import argparse
from portScan import *
from dirscan.dirscan import *
from dirscan.listall.listtamper import *
from dirscan.listall.lsitcms import *
from dirscan.listall.listleaks import *


def help():
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", help='URL')
    parse.add_argument("-us", "--urls", help='Use FileURLS')
    parse.add_argument("-p", "--port", help='PORT')
    parse.add_argument("-d", "--dir", help='Directory')
    parse.add_argument("-t", "--time", help='TIME', type=int)
    parse._action_groups
    args = parse.parse_args()
    url = args.url
    urls = args.urls
    port = args.port
    dir = args.dir
    times = args.time

    if(url and urls):
        print("url和urls不能同时存在".decode("utf-8").encode("gbk"))
        return

    elif(url):  #url存在
        if(port): #端口存在
            if(dir): #目录存在

                scanportanddir(url, port, dir, times)    #指定url扫描


            else:   #目录不存在则只扫描端口
                onlyportscan(url, port) #完成

        else:
            print("端口不能为空".decode("utf-8").encode("gbk"))
            return

    elif(urls and port):   #指定url不存在，指定扫描文件存在
        if(dir):   #扫描目录
            filedirscan(urls, port, dir)
        else:
            urls = args.urls
            port = args.port
            fileurlsscan(urls, port)   #完成

    elif(dir):
        if dir == 'list.tamper':
            listtamper()

        elif dir == 'list.cms':
            listcms()             #此处输出cms下的目录 ,完成

        elif dir == 'list.leaks':
            listleaks()            #此处输出leaks下的目录 ,完成

    else:
        print("必须指定url或者指定urls文件和端口".decode("utf-8").encode("gbk"))