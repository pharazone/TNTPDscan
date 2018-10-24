#!/usr/bin/python
#encoding:utf-8

from onlyPS.urlportscan import *
from onlyPS.urlsportscan import *
from dirscan.dirscan import *

def onlyportscan(url, port):   #指定url，只扫描端口
    if(port == "all"):   #指定url，扫描全端口
        scanurlport(url)   #完成
    else:
        print("请更正port=all".decode("utf-8").encode("gbk"))


def scanportanddir(url, port, dir, times):    #指定url扫描目录

    if(port == "all"):   #指定url，扫描全端口

        scanurlportanddir(url, dir, times)   #先扫描端口，然后再根据存活端口扫描目录
    else:
        if(0<int(port)<65530):    #指定url，指定端口扫描目录
            scanurlonlyportanddir(url, dir, port, times)

def filedirscan(urls, port, dir):  #指定urls文件批量扫描目录
    print()

def fileurlsscan(urls, port):   #指定文件
    if(port == "all"):   #指定文件，扫描全端口
        scanurlsport(urls)    #完成
    else:
        if(0<int(port)<65530):    #指定文件，指定端口扫描目录
            print(port)