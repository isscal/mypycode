# encoding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import urllib
import lxml
import pymysql

# 爬取好豆网某一类菜的图片信息
url = "http://www.haodou.com/recipe/album/14067884/"
# url = "http://www.haodou.com/recipe/album/"
# driver=webdriver.Chrome(r"D:\Python\IEDriverServer\chromedriver.exe")
os.chdir(r"D:\myCode\pyCode")


# def open_browser(url):
#     driver = webdriver.PhantomJS(
#         executable_path=r"D:\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe")
#     print("打开网址 ...")
#     driver.get(url)
#     driver.find_element_by_css_selector(
#         "#p_1 > div.title > p > a:nth-child(1)").click()
#     driver.find_element_by_css_selector(
#         "body > div.warpb.clearfix.mainbd > div > div.imit_table > div.tdCon > ul > li:nth-child(1) > dl > dt > a").click()
#     print("----")
#     return driver
# driver.find_element_by_xpath("//*[@id="p_1"]/div[1]/p/a[1]").click()
# text = driver.find_elements_by_link_text("三伏天")


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data


def get_text(html):
    soup = BeautifulSoup(html, 'lxml')
    picList = soup.find("div", attrs={"class": "picList"})
    titles = soup.find_all("p", attrs={"class": "f14 mgt5"})
    authors = soup.find_all("p", attrs={"class": "uids"})
    imgs = soup.find_all('p', attrs={"class": "bigimg"})
    # print(type(imgs),"\n\n")
    # print(type(imgs[0]),imgs[0].img.get('src'))
    # print("picList+:{}".format(picList))
    # print("titles:{}".format(tiltes))
    # print("authors:{}".format(authors))
    # print("imgs:{}".format(imgs))
    title_text = []
    author_text = []
    img_text = []
    # 将图片标题写入列表
    for title in titles:
        t = title.get_text()
        title_text.append(t)
        # print(t)
    # 将作者写入列表
    for author in authors:
        au = author.get_text()
        author_text.append(au)
        # print(au)
    # 将图片地址写入列表
    for i in imgs:
        imgAdrres = i.img.get('src')
        img_text.append(imgAdrres)
        # print(imgAdrres)
    # 打印爬取信息
    for line in range(len(title_text)):
        print("图片标题：{}".format(title_text[line]))
        print("图片作者：{}".format(author_text[line]))
        print("图片地址：{}".format(img_text[line]))
    return title_text, author_text, img_text


def save_text(title_text, author_text, img_text):
    # 保存爬取信息
    with open("haodou.tsv", "w", newline="") as file:
        file.write("图片标题\t图片作者\t图片地址\n")
        for line in range(len(title_text)):
            file.write("{}\t{}\t{}\n".format(
                title_text[line], author_text[line], img_text[line]))
            # writer = csv.writer(file)
            # writer.writerow(title_text[line]

def save_to_mysql(title_text, author_text, img_text):
    """
    将爬取内如存入mysql
    """
    print('======连接到mysql服务器======')
    mydb = pymysql.connect(host='localhost', user='root',
                           passwd='123456', db='spider', port=3306, charset='utf8')
    cursor = mydb.cursor()
    print('======连接上了=======')
    #创建表及字段
    cursor.execute("DROP TABLE IF EXISTS haodou")
    createTableSql = """CREATE TABLE haodou (
        id int NOT NULL ,
        title CHAR(30),
        author CHAR(10),
        img CHAR(100)
         )
        """
    cursor.execute(createTableSql)
    print("======表及字段创建成功=======")
    for line in range(len(title_text)):
        # {0} {1} 要和sql语句区分
        cursor.execute('insert into haodou (id,title,author,img) values("{0}","{1}","{2}","{3}");'.format(
            line, title_text[line], author_text[line], img_text[line]))
    print("======插入数据成功=======")
    cursor.close()  # 关游标
    mydb.commit()
    mydb.close()  # 关数据库


def downLoadImgs(img_text, title_text):
    # 下载爬取的图片
    path = os.getcwd()
    new_path = os.path.join(path, 'downLoadImgs')
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    new_path += '\ '

    try:
        x = 1
        if img_text == []:
            print("Done!")
        for img in img_text:
            if 'http' in img:
                # print("It's downloading %s" % x + "th's piture")
                print("总共{}图片,正在下载第{}张:{}.jpg".format(len(img_text), x, title_text[x - 1]))
                # python3中urlretrieve路径已变更到urllib.request
                urllib.request.urlretrieve(img, new_path + '{}.jpg'.format(title_text[x - 1]))
                x += 1

    except Exception as e:
        print(e)
    else:
        pass
    finally:
        if x:
            print("下载完成!!!")


if __name__ == '__main__':
    # open_browser(url)
    html = get_page(url)
    title_text, author_text, img_text = get_text(html)
    # save_text(title_text, author_text, img_text)
    save_to_mysql(title_text, author_text, img_text)
    # downLoadImgs(img_text, title_text)
