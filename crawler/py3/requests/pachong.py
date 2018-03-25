# -*- coding: utf-8 -*-
# @Author: ifredom
# @Date:   2017-07-11 11:06:56
# @Last Modified time: 2017-07-11 12:08:31
import requests

url = "http://www.baidu.com"

def getHtmlText(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return r.text

text = getHtmlText(url)
print(text)
