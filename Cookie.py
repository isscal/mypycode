#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
早听说用python做网络爬虫非常方便，正好这几天单位也有这样的需求，需要登陆XX网站下载部分文档，于是自己亲身试验了一番，效果还不错。
 
本例所登录的某网站需要提供用户名，密码和验证码，在此使用了python的urllib2直接登录网站并处理网站的Cookie。
 
Cookie的工作原理： 
Cookie由服务端生成，然后发送给浏览器，浏览器会将Cookie保存在某个目录下的文本文件中。在下次请求同一网站时，会发送该Cookie给服务器，这样服务器就知道该用户是否合法以及是否需要重新登录。
 
Python提供了基本的cookielib库，在首次访问某页面时，cookie便会自动保存下来，之后访问其它页面便都会带有正常登录的Cookie了。
 
原理：
 
（1）激活cookie功能
 （2）反“反盗链”，伪装成浏览器访问
 （3）访问验证码链接，并将验证码图片下载到本地
 （4）验证码的识别方案网上较多，python也有自己的图像处理库，此例调用了火车头采集器的OCR识别接口。
 （5）表单的处理，可用fiddler等抓包工具获取需要提交的参数
 （6）生成需要提交的数据，生成http请求并发送
 （7）根据返回的js页面判断是否登陆成功
 （8）登陆成功后下载其它页面
 
此例中使用多个账号轮询登陆，每个账号下载3个页面。
 
下载网址因为某些问题，就不透露了。
 
以下是部分代码：
"""
import os
import urllib2
import urllib
import cookielib
import xml.etree.ElementTree as ET


# -----------------------------------------------------------------------------
# Login in www.***.com.cn
def ChinaBiddingLogin(url, username, password):
    # Enable cookie support for urllib2
    cookiejar = cookielib.CookieJar()
    urlopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    urllib2.install_opener(urlopener)

    urlopener.addheaders.append(
        ('Referer', 'http://www.chinabidding.com.cn/zbw/login/login.jsp'))
    urlopener.addheaders.append(('Accept-Language', 'zh-CN'))
    urlopener.addheaders.append(('Host', 'www.chinabidding.com.cn'))
    urlopener.addheaders.append(
        ('User-Agent', 'Mozilla/5.0 (compatible; MISE 9.0; Windows NT 6.1); Trident/5.0'))
    urlopener.addheaders.append(('Connection', 'Keep-Alive'))

    print
    'XXX Login......'

    imgurl = r'http://www.*****.com.cn/zbw/login/image.jsp'
    DownloadFile(imgurl, urlopener)
    authcode = raw_input('Please enter the authcode:')
    # authcode=VerifyingCodeRecognization(r"http://192.168.0.106/images/code.jpg")

    # Send login/password to the site and get the session cookie
    values = {'login_id': username, 'opl': 'op_login',
              'login_passwd': password, 'login_check': authcode}
    urlcontent = urlopener.open(urllib2.Request(url, urllib.urlencode(values)))
    page = urlcontent.read(500000)

    # Make sure we are logged in, check the returned page content
    if page.find('login.jsp') != -1:
        print
        'Login failed with username=%s, password=%s and authcode=%s' \
        % (username, password, authcode)
        return False
    else:
        print
        'Login succeeded!'
        return True


# -----------------------------------------------------------------------------
# Download from fileUrl then save to fileToSave
# Note: the fileUrl must be a valid file
def DownloadFile(fileUrl, urlopener):
    isDownOk = False

    try:
        if fileUrl:
            outfile = open(r'/var/www/images/code.jpg', 'w')
            outfile.write(urlopener.open(urllib2.Request(fileUrl)).read())
            outfile.close()

            isDownOK = True
        else:
            print
            'ERROR: fileUrl is NULL!'
    except:
        isDownOK = False

    return isDownOK


# ------------------------------------------------------------------------------
# Verifying code recoginization
def VerifyingCodeRecognization(imgurl):
    url = r'http://192.168.0.119:800/api?'
    user = 'admin'
    pwd = 'admin'
    model = 'ocr'
    ocrfile = 'cbi'

    values = {'user': user, 'pwd': pwd, 'model': model,
              'ocrfile': ocrfile, 'imgurl': imgurl}
    data = urllib.urlencode(values)

    try:
        url += data
        urlcontent = urllib2.urlopen(url)
    except IOError:
        print
        '***ERROR: invalid URL (%s)' % url

    page = urlcontent.read(500000)

    # Parse the xml data and get the verifying code
    root = ET.fromstring(page)
    node_find = root.find('AddField')
    authcode = node_find.attrib['data']

    return authcode


# ------------------------------------------------------------------------------
# Read users from configure file
def ReadUsersFromFile(filename):
    users = {}
    for eachLine in open(filename, 'r'):
        info = [w for w in eachLine.strip().split()]
        if len(info) == 2:
            users[info[0]] = info[1]

    return users


# ------------------------------------------------------------------------------
def main():
    login_page = r'http://www.***.com.cnlogin/login.jsp'
    download_page = r'http://www.***.com.cn***/***?record_id='

    start_id = 8593330
    end_id = 8595000

    now_id = start_id
    Users = ReadUsersFromFile('users.conf')
    while True:
        for key in Users:
            if ChinaBiddingLogin(login_page, key, Users[key]):
                for i in range(3):
                    pageUrl = download_page + '%d' % now_id
                    urlcontent = urllib2.urlopen(pageUrl)

                    filepath = './download/%s.html' % now_id
                    f = open(filepath, 'w')
                    f.write(urlcontent.read(500000))
                    f.close()

                    now_id += 1
            else:
                continue


# ------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
