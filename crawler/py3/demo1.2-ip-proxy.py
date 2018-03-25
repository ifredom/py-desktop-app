# -*- coding: UTF-8 -*-
# @Author: ifredom
# @Date:  2018/1/22
from urllib import request


# 出处 https://blog.csdn.net/c406495762/article/details/60137956
# IP代理网址 http://www.xicidaili.com/
# 设置IP代理


def ipProxy():
    if __name__ == "__main__":
        url = 'http://www.whatismyip.com.tw/'
        # #这是代理IP
        proxy = {'http': '222.186.45.145:57273'}
        # 创建ProxyHandler
        proxy_support = request.ProxyHandler(proxy)
        # 创建Opener
        opener = request.build_opener(proxy_support)
        # 设置ua
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
        # 安装OPener
        request.install_opener(opener)
        # 使用自己安装好的Opener
        res = request.urlopen(url)
        # 读取相应信息并解码
        html = res.read().decode("utf-8")

        # 打印信息
        print(html)


ipProxy()
