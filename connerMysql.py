from urllib.parse import quote

import pymysql
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

KEYWORD = 'ipad'
MAX_PAGE = 3
# 设置缓存和禁用图片加载的功能
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
# 使用phantomjs打开
driver = webdriver.PhantomJS(
    executable_path=r"D:\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe", service_args=SERVICE_ARGS)
# driver = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)
products = []


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        driver.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = driver.page_source
    doc = pq(html)
    # print('+++++++++++++++++++++++++++doc+++++++++++++++++++++', doc)
    items = doc('#mainsrp-itemlist .items .item').items()
    # print("itemsType\n",type(items))

    for item in items:
        # print("itemType\n",type(item))
        # print("===============item===============",item)
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        products.append(product)
        # print(len(products))
        # print(products)
        save_to_mysql(products)


def save_to_mysql(products):
    # print('连接到mysql服务器...')
    mydb = pymysql.connect(host='localhost', user='root',
                           passwd='123456', db='spider', port=3306, charset='utf8')
    cursor = mydb.cursor()
    # print('连接上了!')
    cursor.execute("DROP TABLE IF EXISTS taoBaoData")
    createTableSql = """CREATE TABLE taoBaoData (
        id  int NOT NULL,
        title CHAR(100),
        price CHAR(10),
        deal CHAR(20),
        shop CHAR(50),
        location CHAR(30),
        image CHAR(200)
         )
        """
    cursor.execute(createTableSql)
    i = 0
    for product in products:
        i = i + 1
        cursor.execute(
            'insert into taoBaoData (id,title, price, deal,shop, location,image) VALUES ("{0}", "{1}", "{2}", "{3}", "{4}","{5}","{6}");'.format(
                i, product["title"], product["price"], product[
                    "deal"], product["shop"], product["location"],
                product["image"]))

        # data=(product["title"], product["price"], product["deal"],
        #         product["shop"], product["location"], product["image"])
    print("==========第{}条数据插入成功============".format(i))
    mydb.commit()
    mydb.close()


def main():
    """
    遍历每一页
    """

    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    print("插入完成")
    driver.close()


if __name__ == '__main__':
    main()
