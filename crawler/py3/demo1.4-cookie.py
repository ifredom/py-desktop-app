# -*- coding: UTF-8 -*-
# @Author: ifredom
# @Date:  2018/3/25
from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar

# 伯乐在线
def getMMPhone():
    login_url = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
    # User-Agent信息
    user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    # Headers信息
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    # 登陆Form_Data信息
    Login_Data = {}
    Login_Data['action'] = 'user_login'
    Login_Data['redirect_url'] = 'http://www.jobbole.com/'
    Login_Data['remember_me'] = '0'  # 是否一个月内自动登陆
    Login_Data['user_login'] = 'ifredom'  # 改成你自己的用户名
    Login_Data['user_pass'] = '7583362'  # 改成你自己的密码

    logingpostdata = parse.urlencode(Login_Data).encode("utf-8")

    #声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(cookie_support)
    #创建Request对象
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head)

    #面向对象地址
    date_url = 'http://date.jobbole.com/wp-admin/admin-ajax.php'
    #面向对象
    Date_Data = {}
    Date_Data['action'] = 'get_date_contact'
    Date_Data['postId'] = '4128'
    #使用urlencode方法转换标准格式
    datepostdata = parse.urlencode(Date_Data).encode('utf-8')
    req2 = request.Request(url=date_url, data=datepostdata, headers=head)

    try:
        #使用自己创建的opener的open方法
        response1 = opener.open(req1)
        response2 = opener.open(req2)
        login_result = response1.read().decode('utf-8')
        mm_info = response2.read().decode('utf-8')
        index = mm_info.find('jb_contact_email')
        #打印查询结果
        print('登录结果:%s' % login_result)
        print('联系邮箱:%s' % mm_info[index+19:-2])

    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError:%d" % e.code)
        elif hasattr(e, 'reason'):
            print("URLError:%s" % e.reason)


getMMPhone()
