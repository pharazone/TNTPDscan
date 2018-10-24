#!/usr/bin/python
#encoding:utf-8

import os
def listtamper():
    path = os.path.abspath('.')
    print("******************************脚本类型列表*********************************".decode("utf-8").encode("gbk"))
    for root, dirs, files in os.walk(path+"\\file\\tamper"):
        for file in files:
            print("                                "+file)
