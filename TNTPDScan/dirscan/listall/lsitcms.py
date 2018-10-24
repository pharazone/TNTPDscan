#!/usr/bin/python
#encoding:utf-8

import os
def listcms():
    path = os.path.abspath('.')
    print("******************************开源cms列表*********************************".decode("utf-8").encode("gbk"))
    for root, dirs, files in os.walk(path+"\\file\\cms"):
        for file in files:
            print("                                "+file)