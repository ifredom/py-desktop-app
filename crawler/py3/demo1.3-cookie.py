# -*- coding: UTF-8 -*-
# @Author: ifredom
# @Date:  2018/3/25
from urllib import request
from http import cookiejar
# 伯乐在线
url = 'http://www.jobbole.com/wp-admin/admin-ajax.php'


def getCookie():
    if __name__ == "__main__":
        targetCookieUrl = "http://www.baidu.com"
        # 声明一个CookieJar对象实例来保存cookie
        cookie = cookiejar.CookieJar()
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        handle = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(handle)
        # 此处的open方法打开网页
        res = opener.open(targetCookieUrl)
        # 读取相应信息并解码
        html = res.read().decode("utf-8")
        # 打印信息
        for item in cookie:
            print('Name = %s' % item.name)
            print('Value = %s' % item.value)


def saveCookieToFile():
    targetCookieUrl = "http://www.baidu.com"
    # 设置保存cookie的文件，同级目录下的cookie.txt
    filename = "cookie.txt"
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(filename)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    res = opener.open(targetCookieUrl)
    # 保存cookie到文件
    # ignore_discard的意思是即使cookies将被丢弃也将它保存下来；
    # ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入。
    cookie.save(ignore_discard=True, ignore_expires=True)


def getCookieFromFile():
    targetCookieUrl = "http://www.baidu.com"
    filename = "cookie.txt"
    cookie = cookiejar.MozillaCookieJar(filename)
    # 从文件中读取cookie内容到变量
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    handle = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handle)
    res = opener.open(targetCookieUrl)
    print(res.read().decode("utf-8"))


getCookieFromFile()
