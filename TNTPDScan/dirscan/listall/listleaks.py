#!/usr/bin/python
#encoding:utf-8

import os
def listleaks():
    path = os.path.abspath('.')
    print("******************************已知漏洞列表*********************************".decode("utf-8").encode("gbk"))
    for root, dirs, files in os.walk(path+"\\file\\leaks"):
        for file in files:
            print("                   "+file)