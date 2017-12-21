# -*- coding:utf-8 -*-  
'''
@software: PyCharm 
@file: xmly.py
@time: 2017/9/30 0030 下午 2:25 
@author: Gainsboroly
'''

import json
import os
import random
import time

import requests
from bs4 import BeautifulSoup
from lxml import etree

UA_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
headers1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Proxy-Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': random.choice(UA_LIST)
}
headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.ximalaya.com/dq/all/2',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': random.choice(UA_LIST)
}


def get_url():
    """
    获取喜马拉雅专辑的链接
    :return:
    """
    start_urls = ['http://www.ximalaya.com/dq/all/{}'.format(num) for num in range(1, 85)]
    for page_num, start_url in enumerate(start_urls[:1]):
        print("共计{}页,开始解析第{}页".format(len(start_urls), page_num + 1).center(80, "*"))
        html = requests.get(start_url, headers=headers1).text
        soup = BeautifulSoup(html, 'lxml')
        items = soup.find_all(class_="albumfaceOutter")
        for item_num, item in enumerate(items):
            content = {
                'href': item.a['href'],
                'title': item.img['alt'],
                'img_url': item.img['src']
            }
            print("开始解析第{}个专辑：<<{}>>  ".format(item_num + 1, content["title"]).center(60, "*"))
            # another(item.a['href'])
            mkdir(item.img['alt'])
            # 更改目录，以便文件下载到对应的文件夹中
            os.chdir(os.path.join(os.path.join('E:\\xmly\\', item.img['alt'])))
            download_ablum_pic(item.img['alt'], item.img['src'])
            get_audio_id(item.a['href'])
        time.sleep(1)


def get_audio_id(album_url):
    """
    获取专辑里内容列表的每个id，并拼接成请求地址
    """
    html = requests.get(album_url, headers=headers1).text
    ifanother = etree.HTML(html).xpath('//div[@class="pagingBar_wrapper"]/a[last()-1]/@data-page')

    if len(ifanother):
        num = ifanother[0]
        print('该专辑一共有' + num + '页！！！')
        for n in range(1, int(num) + 1):
            print('开始解析{}页中的第{}页！！！'.format(num, n))
            album_anther_page = album_url + '?page={}'.format(n)
            print(album_anther_page)
            # album_anther_page_list.append(album_anther_page)
            response = requests.get(album_anther_page, headers=headers1).text
            soup = BeautifulSoup(response, "lxml")
            soundids = soup.find("div", attrs={"class": "album_soundlist"})
            soundid = soundids.find_all("li")
            sound_id = sound_id["sound_id"]
            for sound_id in soundid:
                # 通过li标签的sound_id 属性获取sound_id值
                # 也可以通过xpath获取 etree.HTML(html).xpath('//div[@class="album_soundlist"]/ul/li/@sound_id')
                downloadJson = "http://www.ximalaya.com/tracks/{}.json".format(sound_id)
                get_download_info(downloadJson)
    else:
        print("该专辑只有一页！！！")


def get_download_info(download_json_url):
    """
    获取专辑里内容列表的下载地址
    """
    response = requests.get(download_json_url, headers=headers1).text
    data = json.loads(response)
    audioInfo = {
        "play_path": data["play_path"],  # 下载内容的具体地址
        "title": data["title"]  # 下载内容的名称
    }
    dowload_ablum_adio(audioInfo["play_path"], audioInfo["title"])


def mkdir(title):
    """
    创建以每个专辑命名的文件夹
    """
    path = title.strip()
    isExists = os.path.exists(os.path.join('E:\\xmly\\', path))
    if not isExists:
        print("正在创建一个名叫{}的文件夹".format(title))
        os.makedirs(os.path.join('E:\\xmly\\', title))
    else:
        print("名叫{}的文件夹已存在！！！".format(title))


def download_ablum_pic(album_title, album_img_ulr):
    """
    下载封面图片
    :param album_title:
    :param album_img_ulr:
    :return:
    """
    response = requests.get(album_img_ulr, headers=headers1).content
    print("---专辑封面图片<<{}>>开始下载！！！".format(album_title))
    with open(album_title + ".jpg", "wb") as f:
        f.write(response)
    print("---专辑封面图片<<{}>>下载完成！！！".format(album_title))


def dowload_ablum_adio(json_url, url_name):
    """
    下载专辑里的音频
    :param json_url:
    :param url_name:
    :return:
    """
    response = requests.get(json_url, headers=headers1).content
    print("---音频{}开始下载！！！".format(url_name))
    with open(url_name + ".m4a", "wb") as f:
        f.write(response)
    print("---音频{}下载完成！！！".format(url_name))


if __name__ == '__main__':
    get_url()
