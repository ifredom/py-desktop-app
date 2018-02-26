# -*- coding: utf-8 -*-
# @Author: ifredom
# @Date:   2017-07-11 11:06:56
# @Last Modified time: 2017-07-11 12:08:31
import urllib

url = "http://www.baidu.com"
page = urllib.urlopen(url)
html = page.read()
print(html)
# def getHtml(url):
#     page = ur.urlopen(url)
#     html = page.read()
#     return html

# def getImg(html):
#     reg = /^'src="(.+?\.jpg)"/
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     return imglist

# html = getHtml("http://www.baidu.com")

# print(getImg(html))
