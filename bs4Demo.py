#encoding=utf-8
from bs4 import BeautifulSoup
import requests
from lxml import etree
# r=requests.get("https://www.baidu.com/")
# html=r.text
soup=BeautifulSoup(open(r"D:\myCode\htmlCode\myhtml.html",encoding='gb18030',errors='ignore'),"lxml")
# html=etree.parse(r"D:\myCode\htmlCode\myhtml.html")
# html.xpath("p")
# print(Html.prettify())
# print(soup.head.contents[5])
picList = soup.find("div", attrs={"class": "picList"})
# titles = soup.find_all("p",attrs={"class":"f14 mgt5"})
# authors = soup.find_all("p",attrs={"class":"uids"})
imgs = soup.find_all('p',attrs={"class":"bigimg"})
# print(type(imgs),"\n\n")
# print(type(imgs[0]),imgs[0].img.get('src'))
# for i in imgs:
#     print(i.img.get('src'))
# print (r.status_code,r.text)
# print(soup.head.children)

# for child in soup.body.children:
# 	print (child)

# for child in soup.descendants:
# 	print (child)

# for string in soup.strings:
# 	print(repr(string))

#使用tripped_strings去掉多余空格
# for string in soup.stripped_strings:
# 	print(repr(string))

#查找第一个LI元素的父节点名称
# print(soup.li.parent.name)
#通过元素的 .parents 属性可以递归得到元素的所有父辈节点，例如
# content = soup.head.title.string
# for parent in content.parents:
# 	print(parent.name)

"""
（7）兄弟节点
 知识点：.next_sibling .previous_sibling 属性
 兄弟节点可以理解为和本节点处在统一级的节点，.next_sibling 属性获取了该节点的下一个兄弟节点，.previous_sibling 则与之相反，如果节点不存在，则返回 None
 注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
"""
# print(soup.li.next_sibling)
# print(soup.li.prev_sibling)

""""
（8）全部兄弟节点
 知识点：.next_siblings .previous_siblings 属性
 通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出
"""
# for sibling in soup.li.next_siblings:
# 	print(repr(sibling))

"""
（9）前后节点
 知识点：.next_element .previous_element 属性
 与 .next_sibling .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次
 比如 head 节点为
 <head><title>The Dormouse's story</title></head>
 那么它的下一个节点便是 title，它是不分层次关系的
"""
# print(soup.ul.next_element)
"""
（10）所有前后节点
 
    知识点：.next_elements .previous_elements 属性
 
通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样
"""
# for element in soup.li.next_elements:
# 	print(element)

"""
7.搜索文档树
（1）find_all( name , attrs , recursive , text , **kwargs )
 find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
（2）find( name , attrs , recursive , text , **kwargs )
（3）find_parents() find_parent()
(4）find_next_siblings() find_next_sibling()
（5）find_previous_siblings() find_previous_sibling()
（6）find_all_next() find_next()
（7）find_all_previous() 和 find_previous()
"""
# print(soup.find("li").string)
# print(soup.find_all("li")[3].string)
"""
8.CSS选择器
 我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，
 用到的方法是 soup.select()，返回类型是 list
"""
#（1）通过标签名查找  
# print(soup.select("li")[0].string)
#（2）通过类名查找
# print(soup.select(".img-responsive"))
# （3）通过 id 名查找
# print(soup.select("#indoor-outdoor"))
#（4）组合查找
# 组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开
# print(soup.select(".col-xs-6 #indoor-outdoor"))

#(5)直接子标签查找
# print(soup.select("ol > li")[0].string)
"""
（6）属性查找
查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
print soup.select("head > title")#[<title>CatPhotoApp</title>]
print soup.select('a[href="#""]')#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>] 
同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格
print soup.select('p a[href="http://example.com/elsie"]')#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>] 
好，这就是另一种与 find_all 方法有异曲同工之妙的查找方法，是不是感觉很方便？
"""
# print (soup.select("head > title"))
# print (soup.select('a[href="#"]'))