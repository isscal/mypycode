# encoding: utf-8

'''
Created on 2016年5月4日

@author: Dongming
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import xlrd

#import xdrlib ,sys
def open_excel(file= 'file.xls'):
    data = xlrd.open_workbook(file)
    return data
    # try:
    #     data = xlrd.open_workbook(file)
    #     return data
    # except Exception,e:
    #     print str(e)
#根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    colnames = table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
                list.append(app)
    return list
            

def Login():
    listdata = excel_table_byindex(r"D:\myCode\pyCode\test.xlsx" , 0)
    if (len(listdata) <= 0 ):
        assert 0 , u"Excel数据异常"
        for i in range(0 , len(listdata) ):
            browser=webdriver.Chrome(r"D:\Python\IEDriverServer\chromedriver.exe")
            print("open browser")
            browser.get("http://iess.03199.com")
            assert "IESS2.0" in browser.title
            browser.find_element_by_id('userName').send_keys(listdata[i]['username'])
            browser.find_element_by_id('password').send_keys(listdata[i]['password'])
            browser.find_element_by_xpath("//*[@id='page-layout']/div/div[4]/div/div/a[1]").click()
            browser.find_element_by_xpath('//*[@id="page-index-school"]/header/div[1]/i/img').click()
            browser.find_element_by_xpath('//*[@id="page-1501134657970"]/div/div[1]/ul[1]/li/a/div[2]').click()
            browser.close()

        
if __name__ == '__main__':
    Login()

