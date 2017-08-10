# coding:utf-8
import urllib
import http.cookiejar
import requests
from bs4 import BeautifulSoup

url="http://10.80.73.7/IISP/views/report/daily/re_asa.jsp?Id=HNDailyReportAsa20170601&dateTime=20170601&statu=0"

def Cookie():
    # 声明一个CookieJar对象来保存cookie
    cookie = http.cookiejar.CookieJar()
    # 创建cookie处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 构建opener
    opener = urllib.request.build_opener(handler)

    # 创建请求
    res = opener.open('http://10.80.73.7/IISP/views/login.jsp')
    for item in cookie:
        print('name:' + item.name + '-value:' + item.value)

# 将cookie保存在文件中


def saveCookie():
    # 设置保存cookie的文件
    filename = 'cookie.txt'
    # 声明一个MozillaCookieJar对象来保存cookie，之后写入文件
    # cookie =cookielib.MozillaCookieJar(filename)
    cookie = http.cookiejar.MozillaCookieJar(filename)
    # 创建cookie处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 构建opener
    opener = urllib.request.build_opener(handler)
    # 创建请求
    res = opener.open('http://10.80.73.7/IISP/views/report/daily/re_daily_quota.jsp?id=HNDailyReportQuo20170601&dateTime=20170601&secondCompanyCode=HN')
    # 保存cookie到文件
    # ignore_discard的意思是即使cookies将被丢弃也将它保存下来
    # ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
    cookie.save(ignore_discard=True, ignore_expires=True)

# 从文件中获取cookie并且访问(我们通过这个方法就可以打开保存在本地的cookie来模拟登录)


def getCookie():
    Cookie=""
    # 创建一个MozillaCookieJar对象
    cookie = http.cookiejar.MozillaCookieJar()
    # 从文件中的读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    # 打印cookie内容,证明获取cookie成功
    for item in cookie:
        Cookie=Cookie+item.name+":"+item.value
        # print(type(item),'name:' + item.name + '-value:' + item.value)
        print(Cookie)
    # 利用获取到的cookie创建一个opener
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    res = opener.open(
        'http://10.80.73.7/IISP/views/report/daily/re_daily_quota.jsp?id=HNDailyReportQuo20170601&dateTime=20170601&secondCompanyCode=HN')
    html = res.read().decode("utf-8")
    # print (html)
    return html


def getContent(html):
    soup = BeautifulSoup(html, "html.parser")
    print(soup.prettify())
    print("================FIND TR TIPS==================\n\n", soup.find("tr"))


def postData():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
         "cookie":"JSESSIONID=5B060C2D9AC18AA873EF927CDD774E02; ZDKJ_TICKET=8426C128FF4AD8FFCCE2B99F557F90B4"
    }
    playLoad = {"id": "HNDailyReportQuo20170601",
                "dateTime": "20170601", "secondCompanyCode": "HN", "type": "1"}
    data=requests.post(url,headers=headers,data=playLoad).content.decode("utf-8")
    print(data)


if __name__ == '__main__':
    # Cookie()
    # saveCookie()
    # html = getCookie()
    # getContent(html)
    postData()
