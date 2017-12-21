# -*- coding:utf-8 -*-  
'''
@software: PyCharm 
@file: run.py
@time: 2017/8/22 0022 下午 3:44 
@author: Gainsboroly
'''
from hnDayliReport import *
from hnLogin import *
from hnRealtimeImage import *


def main():
    driver = open_browser()
    login(driver, loginInfo["username"], loginInfo["password"])
    if driver.title == "发电企业智能信息服务平台":
        print("恭喜你成功登录{}!".format(driver.title))
    getDailyReportPage(driver)
    # hnRealtimeImage(driver)


if __name__ == '__main__':
    main()
