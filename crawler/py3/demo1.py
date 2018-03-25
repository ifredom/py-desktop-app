# -*- coding: UTF-8 -*-
# @Author: ifredom
# @Date:  2018/1/22
from urllib import request
from urllib import parse
import json
import chardet
url = "http://fanyi.baidu.com"


# 获取请求http的具体内容
def getHttpHtml(url):
    if __name__ == "__main__":
        response = request.urlopen(url)
        html = response.read()
        charset = chardet.detect(html)
        html = html.decode("utf-8")
        print(html)
        print(charset)

# 获取请求http的参数
def getReq(url):
    req = request.Request(url)
    res = request.urlopen(req)
    print("geturl 打印信息: %s" % (res.geturl()))
    print("info 打印信息: %s" % (res.info()))
    print("getcode 打印信息: %s" % (res.getcode()))


# 有道云翻译借口
def translateWithYouDao():
    if __name__ == "__main__":
        Request_URL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc"
        Form_Data = {
            "type": "AUTO",
            "i": "你好",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON"
        }

        #使用urlencode方法转换标准格式
        data = parse.urlencode(Form_Data).encode('utf-8')
        #传递Request对象和转换完格式的数据
        response = request.urlopen(Request_URL,data)
        #读取信息并解码
        html = response.read().decode('utf-8')
        #使用JSON
        translate_results = json.loads(html)
        #找到翻译结果
        translate_results = translate_results['translateResult'][0][0]['tgt']
        #打印翻译信息
        print("翻译的结果是：%s" % translate_results)


translateWithYouDao()
