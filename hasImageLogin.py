
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:49:49 2015

@author: DJ
"""

import urllib
import urllib2
import cookielib
	
from bs4 import BeautifulSoup
from PIL import Image
import cStringIO
#登录地址
LoginUrl = "http://gsmis.njust.edu.cn/UserLogin.aspx?exit=1"
mainpage="http://http://gsmis.njust.edu.cn/Gstudent/Default.aspx"
checkCodeUrl = ''
kaitibaogao='http://gsmis.njust.edu.cn/Gstudent/Topic/Topic_Manage.aspx?EID=ZfJPCMhdYM0Q2rZHdgSidgWH2ovrUbhP6ygVVycyPf0='

#登录主函数
def login():
    headerdic={
        'User-Agent'    : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
        'Host' : 'gsmis.njust.edu.cn',
        'Referer' : 'http://gsmis.njust.edu.cn/',
        'Accept'        : '*/*',
        'Connection' : 'Keep-Alive',
         }

    postdic={
         'UserName' : yourusername ,
         'PassWord' : yourpassword,
         'drpLoginType' : '1',
         '__ASYNCPOST' : 'true',
         'ScriptManager1' : 'UpdatePanel2|btLogin',
         '__EVENTTARGET' : 'btLogin',
         '__VIEWSTATE' : '/wEPDwULLTE5OTkyNTM4MzEPZBYCAgMPZBYGAg0PZBYCZg9kFgICAQ8PFgIeCEltYWdlVXJsBSp+L1B1YmxpYy9WYWxpZGF0ZUNvZGUuYXNweD9pbWFnZT02ODA3OTUyOTFkZAIRD2QWAmYPZBYCAgEPEGRkFgFmZAIVD2QWAmYPZBYCAgEPDxYCHgtOYXZpZ2F0ZVVybAUtfi9QdWJsaWMvRW1haWxHZXRQYXNzd2QuYXNweD9FSUQ9VHVyOHZadXVYa3M9ZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFDVZhbGlkYXRlSW1hZ2W5HJlvYqz666q9lGAspojpOWb4sA==',
         '__EVENTVALIDATION' : '/wEdAAoKNGMKLh/WwBcPaLKBGC94R1LBKX1P1xh290RQyTesRQa+ROBMEf7egV772v+RsRJUvPovksJgUuQnp+WD/+4LQKymBEaZgVw9rfDiAaM1opWKhJheoUmouOqQCzlwTSNWlQTw3DcvmMLY3PAqFoA+uFSTy5ozCEG4XBxL/Ykep0cgC/Irwlr9d8VObb8MnYO0GRqRfbdgDIW2dtIsr6rbUIwej/LsqVAg3gLMpVY6UeARlz0=',
         '__EVENTARGUMENT' : '',
         '__LASTFOCUS' : ''
         }

    #cookie 自动处理器
    global checkCodeUrl
    cookiejar = cookielib.LWPCookieJar()#LWPCookieJar提供可读写操作的cookie文件,存储cookie对象
    cookieSupport= urllib2.HTTPCookieProcessor(cookiejar)
    opener = urllib2.build_opener(cookieSupport, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    #打开登陆页面
    img_url="http://gsmis.njust.edu.cn/Public/ValidateCode.aspx?image="
    getCheckCode(img_url,postdic,headerdic)
#    print postdic
    postData=urllib.urlencode(postdic)
    sendPostData(LoginUrl, postData, headerdic,opener)
#    print opener.open(kaitibaogao).read()
    ktbgtxt=opener.open(kaitibaogao).read()
    print ktbgtxt
    soup=BeautifulSoup(ktbgtxt)
    print soup.td    
    


def sendPostData(url, data, header,opener):
    print "+"*20+"sendPostData"+"+"*20
#    data = urllib.urlencode(data)      
    request = urllib2.Request(url, data, header)
    response = opener.open(request)
    url = response.geturl()
    text = response.read()
    print url
    print text

 

def getUrlResponse(url,head) :
    url = str(url)
    req = urllib2.Request(url)
    for eachhead in head.keys():
        req.add_header(eachhead,head[eachhead])
        
    resp = urllib2.urlopen(req)  
    return resp

def getUrlRespHtml(url,head) :
    resp = getUrlResponse(url,head)
    respHtml = resp.read()
    return respHtml 
    
def getCheckCode(url,postdic,headerdic):
    print "+"*20+"getCheckCode"+"+"*20
#    response = urllib2.urlopen(url)
    respHtml = getUrlRespHtml(url,headerdic)
    img = Image.open(cStringIO.StringIO(respHtml))
    img.show()
    checkCode = raw_input("code：") 
    print 'aaa'
    postdic["ValidateCode"] = checkCode
    return postdic

 
if __name__ == "__main__":   
    login()