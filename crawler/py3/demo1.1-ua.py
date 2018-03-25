# -*- coding: UTF-8 -*-
# @Author: ifredom
# @Date:  2018/1/22
from urllib import request

url = 'http://www.csdn.net/'
# 出处 https://blog.csdn.net/c406495762/article/details/60137956

# 设置header方法一


def changeHeaderUa(url):
    if __name__ == "__main__":
        head = {}
        head["User-Agent"] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
        req = request.Request(url, headers=head)
        res = request.urlopen(req)
        result = res.read().decode("utf-8")
        print(result)

# 设置header方法二


def changeHeaderUa2(url):
    if __name__ == "__main__":
        head = {}
        req = request.Request(url)
        req.add_header(
            "User-Agent", 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')
        res = request.urlopen(req)
        result = res.read().decode("utf-8")
        print(result)


changeHeaderUa2(url)
