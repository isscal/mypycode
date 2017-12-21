# coding=utf-8
# import threading
# from time import ctime,sleep


# def music(func):
#     for i in range(2):
#         print ("I was listening to %s. %s" %(func,ctime()))
#         sleep(1)

# def move(func):
#     for i in range(2):
#         print ("I was at the %s! %s" %(func,ctime()))
#         sleep(5)

# threads = []
# t1 = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)

# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()

#     print ("all over %s" %ctime())


# import unittest
# import paramunittest

# @paramunittest.parametrized(
#     ('1', '2'),
#     # (4, 3),
#     ('2', '3'),
#     (('4', ), {'b': '5'}),
#     ((), {'a': 5, 'b': 6}),
#     {'a': 5, 'b': 6},
# )
# class TestFoo(paramunittest.ParametrizedTestCase):
#     def setParameters(self, a, b):
#         self.a = a
#         self.b = b

#     def testLess(self):
#         self.assertLess(self.a, self.b)

# @paramunittest.parametrized(
#     ('1', '2'),
#     # (4, 3),
#     ('2', '3'),
#     (('4', ), {'b': '5'}),
#     ((), {'a': 5, 'b': 6}),
#     {'a': 5, 'b': 6},
# )
# class TestBar(unittest.TestCase):
#     def setParameters(self, a, b):
#         self.a = a
#         self.b = b

#     def testLess(self):
#         self.assertEqual(self.a, self.b)
# if __name__ == '__main__':
#     unittest.main()

# 线性筛选

# isp=[1]*101
# isp[0]=isp[1]=0
# p=list()
# for i in range(2,101):
#     if isp[i]:
#         p.append(str(i))
#         j=i*i
#         while j<101:
#             isp[j]=0
#             j+=i
# print (' '.join(p))


# 快速排序法

# l=[6,2,3,8,7.9]
# left=0
# right=len(l)-1
# def quick(l,left,right):
#     while left<right and l[left]<l[right]:
#         right=right-1
#         l[left],l[right]=l[right],l[left]
#     print(l)

#     while left<right and l[left]<l[right]:
#         left=left+1
#         l[left],l[right]=l[right],l[left]
#     print(l)


# 装饰器

# def fun():
#     print(fun.__closure__)
#     print("fun")
#     def infun():
#         print(infun.__closure__)
#         print("infun")
#         return 0
#     return infun()

# fun()
# passline=90
# def setPassline(x):
#     print(setPassline.__closure__)

#     def dec():
#         if x>passline:
#             print("pass",x)
#         else:
#             print("filed")
#     return dec
# fun100=setPassline(89)
# fun100()
# fun150=setPassline(59)
# fun150()
# print(fun100)
# print(fun150)

# def outer():
#     print("outer.__closure__:",outer.__closure__)
#     x = 1
#     def inner():
#         print("inner.__closure__:",inner.__closure__)
#         print(x)
#     return inner
# outer()
# f=outer()
# print("f:",f)
# f()


# def logger(func):
#     def inner(*args, **kwargs):
#         print ("Arguments were: %s, %s" % (args, kwargs),func.__name__)
#         return func(*args, **kwargs)
#     return inner


# @logger
# def foo1(x, y=1):
#     return x * y
# foo1(4,5)

# #带参数的装饰器
# import logging
# def use_logging(level):
#     def dec(func):
#         def wrapp(*args,**kwargs):
#             if level=="warn":
#                 logging.warn("%s is running",func.__name__)
#             return func(*args)
#         return wrapp
#     return dec


# @use_logging(level="warn")
# def foo(name="foo"):
#     print("i am {}".format(name))
# foo()


# 类装饰器

# class Foo:
#     def __init__(self,func):
#         self._fun=func
# def __call__(self):
#     print("class decorator running")
#     self.func()
#     print("class de corator ending")
# @Foo
# def bar():
#     print("bar")
# bar()


# import os
# from bs4 import BeautifulSoup
# from lxml import etree
# import requests
# import json
# import urllib
#
# downloadlist = []
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36X-Requested-With:XMLHttpRequest"}
# album_url_list = []
# album_title_list = []
# album_img_ulr_list = []
# album_anther_page_list = []
# all_album_pages = ["http://www.ximalaya.com/dq/{}/".format(page) for page in range(1, 85)]
#
# testalbumurl = "http://www.ximalaya.com/36095869/album/3144025/"
# testjsonurl = "http://www.ximalaya.com/tracks/19452918.json"
# testimgeurl = "http://fdfs.xmcdn.com/group33/M05/FF/E9/wKgJTFnErdOCmj6rAAcH8aK9wrE345_web_large.jpg"
#
# mypath = os.getcwd()
# newpath = os.path.join(mypath, "xmlydownload")
# def get_album_info(page):
#     """
#     获取专辑相关信息
#     """
#     data = requests.get(page, headers=headers).text
#     soup = BeautifulSoup(data, "lxml")
#     album_infos = soup.find_all("div", attrs={"class": "discoverAlbum_item"})
#     for album_info in album_infos:
#         album_url = album_info.a.get("href")  # 专辑地址
#         album_img_url = album_info.img.get("src")  # 专辑封面地址
#         album_title = album_info.img.get("alt").strip()  # 专辑名称并去掉行尾空格
#         album_url_list.append(album_url)
#         album_img_ulr_list.append(album_img_url)
#         album_title_list.append(album_title)
#
#         album_info = {"album_url": album_url,
#                       "album_img_url": album_img_url,
#                       "album_title": album_title
#                       }
#
#
# def get_audio_id(album_url):
#     """
#     获取专辑里内容列表的每个id，并拼接成请求地址
#     """
#     html = requests.get(album_url, headers=headers).text
#     ifanother = etree.HTML(html).xpath('//div[@class="pagingBar_wrapper"]/a[last()-1]/@data-page')
#     if len(ifanother):
#         num = ifanother[0]
#         print('该专辑一共有' + num + '页！！！')
#         for n in range(1, int(num) + 1):
#             print('开始解析{}页中的第{}页！！！'.format(num, n))
#             album_anther_page = album_url + '?page={}'.format(n)
#             print(album_anther_page)
#             # album_anther_page_list.append(album_anther_page)
#             response = requests.get(album_anther_page, headers=headers).text
#             soup = BeautifulSoup(response, "lxml")
#             soundids = soup.find("div", attrs={"class": "album_soundlist"})
#             soundid = soundids.find_all("li")
#             for sound_id in soundid:
#                 downloadJson = "http://www.ximalaya.com/tracks/{}.json".format(sound_id["sound_id"])
#                 downloadlist.append(downloadJson)
#     else:
#         print("该专辑只有一页！！！")
#     return downloadlist
#
#
# def get_download_info(download_json_url):
#     """
#     获取专辑里内容列表的下载地址
#     """
#     response = requests.get(download_json_url, headers=headers).text
#     data = json.loads(response)
#     audioInfo = {
#         "play_path": data["play_path"],  # 下载内容的具体地址
#         "title": data["title"]  # 下载内容的名称
#     }
#     for k, v in audioInfo.items():
#         print(k, v)
#     return audioInfo
#
#
# def download_audio(album_img_ulr):
#     """
#     1、创建以每个专辑命名的文件夹
#     2、下载每个专辑的内容到相应的文件夹中
#     3、下载内容包括每个专辑封面图片及专辑内容
#     """
#     if not os.path.isdir(newpath):
#         for index, album_title in enumerate(album_title_list):
#             print("开始第{}个文件夹：{} ".format(index + 1, album_title))
#             os.makedirs(newpath + "//{}".format(album_title))  # 创建以专辑名称命名的文件夹
#             # 下载专辑封面图片
#             print("开始下载第{}个封面图片：{}!!!".format(index + 1, album_title))
#             os.chdir(os.path.join(newpath + "\\" + album_title))
#             mynewpath=os.getcwd()
#             print(mynewpath)
#             response = requests.get(album_img_ulr, headers=headers).content
#             with open(album_title+".jpg", "wb") as f:
#                 f.write(response)
#         print("下载完成！！！")
#     else:
#         print("文件已存在！！")
#
#
#
#
# if __name__ == '__main__':
#     for page,page_url in enumerate(all_album_pages[:2]):
#         print("共计{}页,开始解析第{}页".format(len(all_album_pages),page+1).center(80,"*"))
#         get_album_info(page_url)
#         for album_num,album_url in enumerate(album_url_list[:]):
#             print("共计{}专辑,开始解析第{}个专辑：<<{}>>  ".format(len(album_url_list),album_num+1,album_title_list[album_num+1]).center(60,"*"))
#             get_audio_id(album_url)
#             download_audio(album_img_ulr_list[album_num])


# from bs4 import BeautifulSoup
# import requests
# from lxml import etree

# url="http://www.ganji.com/index.htm"
# headers={}
# response=requests.get(url).text

# soup=BeautifulSoup(response,"lxml")
# ci=soup.find_all("dd")
# # s=ci.attrs
# # for c in ci:
# #     print(c.string)
# city=etree.HTML(response).xpath("//div[@class='all-city']/d1/dd/a/text()")
# print(type(ci))
# # print(s)


# __author__ = 'CQC'
# # -*- coding:utf-8 -*-
# import urllib
# import urllib2
# import re
# import thread
# import time

# #糗事百科爬虫类
# class QSBK:

#     #初始化方法，定义一些变量
#     def __init__(self):
#         self.pageIndex = 1
#         self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#         #初始化headers
#         self.headers = { 'User-Agent' : self.user_agent }
#         #存放段子的变量，每一个元素是每一页的段子们
#         self.stories = []
#         #存放程序是否继续运行的变量
#         self.enable = False
#     #传入某一页的索引获得页面代码
#     def getPage(self,pageIndex):
#         try:
#             url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
#             #构建请求的request
#             request = urllib2.Request(url,headers = self.headers)
#             #利用urlopen获取页面代码
#             response = urllib2.urlopen(request)
#             #将页面转化为UTF-8编码
#             pageCode = response.read().decode('utf-8')
#             return pageCode

#         except urllib2.URLError, e:
#             if hasattr(e,"reason"):
#                 print u"连接糗事百科失败,错误原因",e.reason
#                 return None


#     #传入某一页代码，返回本页不带图片的段子列表
#     def getPageItems(self,pageIndex):
#         pageCode = self.getPage(pageIndex)
#         if not pageCode:
#             print "页面加载失败...."
#             return None
#         pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
#                          'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
#         items = re.findall(pattern,pageCode)
#         #用来存储每页的段子们
#         pageStories = []
#         #遍历正则表达式匹配的信息
#         for item in items:
#             #是否含有图片
#             haveImg = re.search("img",item[3])
#             #如果不含有图片，把它加入list中
#             if not haveImg:
#                 replaceBR = re.compile('<br/>')
#                 text = re.sub(replaceBR,"\n",item[1])
#                 #item[0]是一个段子的发布者，item[1]是内容，item[2]是发布时间,item[4]是点赞数
#                 pageStories.append([item[0].strip(),text.strip(),item[2].strip(),item[4].strip()])
#         return pageStories

#     #加载并提取页面的内容，加入到列表中
#     def loadPage(self):
#         #如果当前未看的页数少于2页，则加载新一页
#         if self.enable == True:
#             if len(self.stories) < 2:
#                 #获取新一页
#                 pageStories = self.getPageItems(self.pageIndex)
#                 #将该页的段子存放到全局list中
#                 if pageStories:
#                     self.stories.append(pageStories)
#                     #获取完之后页码索引加一，表示下次读取下一页
#                     self.pageIndex += 1

#     #调用该方法，每次敲回车打印输出一个段子
#     def getOneStory(self,pageStories,page):
#         #遍历一页的段子
#         for story in pageStories:
#             #等待用户输入
#             input = raw_input()
#             #每当输入回车一次，判断一下是否要加载新页面
#             self.loadPage()
#             #如果输入Q则程序结束
#             if input == "Q":
#                 self.enable = False
#                 return
#             print u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" %(page,story[0],story[2],story[3],story[1])

#     #开始方法
#     def start(self):
#         print u"正在读取糗事百科,按回车查看新段子，Q退出"
#         #使变量为True，程序可以正常运行
#         self.enable = True
#         #先加载一页内容
#         self.loadPage()
#         #局部变量，控制当前读到了第几页
#         nowPage = 0
#         while self.enable:
#             if len(self.stories)>0:
#                 #从全局list中获取一页的段子
#                 pageStories = self.stories[0]
#                 #当前读到的页数加一
#                 nowPage += 1
#                 #将全局list中第一个元素删除，因为已经取出
#                 del self.stories[0]
#                 #输出该页的段子
#                 self.getOneStory(pageStories,nowPage)


# spider = QSBK()
# spider.start()

# from pyecharts import Bar
# bar=Bar("我的第一张图表","这里是副标题")
# bar.add("服装",["衬衫","羊毛衫","裤子","高跟鞋"],[5,10,20,30,40,50])
# bar.show_config()
# bar.render()

print(map(lambda x: x % 2, range(3)))
