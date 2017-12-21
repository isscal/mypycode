# encoding=utf-8
import time

import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# url = "http://10.80.73.7/IISP/views/login.jsp"  # 河南生产环境
url = "http://192.168.1.139/IISP/views/login.jsp"  # 河南测试环境

def open_browser(url):
    """
    使用chrome打开浏览器，并打开网页
    """
    drvier = webdriver.Chrome()
    drvier.maximize_window()
    # drvier = webdriver.PhantomJS(
    #     executable_path=r"D:\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    drvier.get(url)
    print(drvier.current_window_handle)


    return drvier


def login(drvier, verifycode):
    """
    登录操作，并处理验证码过期及输入错误的情况
    """
    loginName = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'loginName')))
    loginName.clear()
    # drvier.find_element_by_id('loginName').clear()
    drvier.find_element_by_id('loginName').send_keys("wangfei")
    drvier.find_element_by_id('password').clear()
    drvier.find_element_by_id('password').send_keys("1234567")
    # 调用js对相中的元素标红
    js = "var q=document.getElementById(\"loginName\");q.style.border=\"1px solid red\";"
    # drvier.execute_script(js)
    drvier.find_element_by_xpath("//*[@id=\"identitryCodeValue\"]").clear()
    # 手动输入验证码
    # verifycode = str(input("输入验证码："))

    print("打印验证码：" + verifycode)
    drvier.find_element_by_xpath("//*[@id=\"identitryCodeValue\"]").send_keys(verifycode)
    print("-----------验证码输入成功---------------------")
    drvier.find_element_by_xpath("//*[@id=\"dowebok\"]/div/div/div[2]/div/div[4]/a").click()
    time.sleep(3)
    title = driver.title
    if (title == "登录"):
        errMsg = driver.find_element_by_css_selector("#errmsg").text
        print("errMsg:", errMsg)
        while (errMsg == "验证码输入错误" or "验证码已过期"):
            try:
                Msg = drvier.find_element_by_id("errmsg").text
                print("Msg:", Msg)
                # 如果验证码输入错误，刷新页面
                drvier.refresh()
                login(drvier)
                get_verifycode(driver)

            except:
                print("登录成功后，该元素不存在")
                break
    print("tilet is :", driver.title)
    print("登录成功!")


def get_verifycode(driver):
    """处理图片验证码"""
    # 截取当前网页，该网页有我们需要的验证码
    driver.save_screenshot('d:\\aa.jpg')
    # 定位验证码
    image_ement = driver.find_element_by_id("identitryCode")
    # 获取验证码x,y轴坐标
    location = image_ement.location
    size = image_ement.size  # 获取验证码的长宽
    # 写成需要截取的位置坐标
    rangle = (
        int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
    i = Image.open("d:\\aa.jpg")  # 打开截图
    i = i.convert('RGB')
    frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('d:\\frame4.jpg')
    qq = Image.open('d:\\frame4.jpg')
    # qq.show() #显示获取到的图片验证码
    # 使用image_to_string识别验证码
    try:
        verifycode = pytesseract.image_to_string(qq).strip()
    except Exception as msg:
        print(msg)
    return verifycode

def getDailyReportPage(driver):
    """
    进入报表页面，默认为日报表页面
    """

    # 建立动作链
    chain = ActionChains(driver)
    # 定位元素综合报表
    implement = driver.find_element_by_css_selector(".user_d_h301")
    print(implement.text)
    # 执行移动鼠标悬停到该元素上
    chain.move_to_element(implement).perform()
    # 点击Add Target
    # time.sleep(10)
    print("点击综合报表")
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul/li[2]/div/ul/li[2]/div/a[2]").click()
    time.sleep(3)

    print("日报表URL：", driver.current_url)
    # pageSource = driver.page_source
    # time.sleep(1)
    # print("pageSource:", pageSource)
    print("点击下拉按钮")
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div[1]/h2").click()
    removeReadonlyJs = "document.getElementById('dayReportDate').removeAttribute('readonly');"
    # JS = "$('input[id=dayReportDate]').removeAttr('readonly')"
    # driver.execute_script(JS)
    driver.execute_script(removeReadonlyJs)
    time.sleep(3)
    print("输入查询日期")
    driver.find_element_by_css_selector("#dayReportDate").clear()
    driver.find_element_by_css_selector("#dayReportDate").send_keys("20170101")
    # driver.find_element_by_id("dayReportDate").clear()
    # driver.find_element_by_id("dayReportDate").send_keys("20170701")

    print("********日期输入成功，点击查询********")
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div[1]/div/ul/li[6]/a[1]").click()
    time.sleep(3)
    print(driver.find_element_by_xpath("//td[contains(.,'两个细则考核日报')]").text)
    driver.find_element_by_xpath("//td[contains(.,'两个细则考核日报')]").click()
    # print(driver.find_element_by_xpath("//*[@id=\"HNDailyReportQuo20170601\"]/td[1]").text)
    # driver.find_element_by_xpath("//*[@id=\"HNDailyReportQuo20170601\"]/td[1]").click()
    # driver.find_element_by_css_selector("#HNDailyReportQuo20170703 > td:nth-child(2)").click()
    print("指定报表URL：", driver.current_url)
    pageSource = driver.page_source
    time.sleep(1)
    current_url = driver.current_url
    print("pageSource:", pageSource)
    return pageSource, current_url


def get_text(driver, html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    jsGetMonthElecGenPlanAssess = "alert(document.getElementById('monthElecGenPlanAssess1').value);"
    driver.execute_script(jsGetMonthElecGenPlanAssess)
    print(jsGetMonthElecGenPlanAssess)
    monthElecGenPlanAssess = soup.select("#monthElecGenPlanAssess1")

    print("================FIND TR TIPS================\n\n", type(monthElecGenPlanAssess), monthElecGenPlanAssess)


def get_text(driver, html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    jsGetMonthElecGenPlanAssess = "alert(document.getElementById('monthElecGenPlanAssess1').value);"
    driver.execute_script(jsGetMonthElecGenPlanAssess)
    print(jsGetMonthElecGenPlanAssess)
    monthElecGenPlanAssess = soup.select("#monthElecGenPlanAssess1")

    print("================FIND TR TIPS================\n\n", type(monthElecGenPlanAssess), monthElecGenPlanAssess)


if __name__ == '__main__':
    driver = open_browser(url)
    verifycode = get_verifycode(driver)
    login(driver, verifycode)
    pageSource, current_url = getDailyReportPage(driver)
    get_text(driver, pageSource)
