from selenium import webdriver
import time
drvier=webdriver.Chrome(r"D:\Python\IEDriverServer\chromedriver.exe")
"""
使用phantomjs打开
driver = webdriver.PhantomJS(
        executable_path=r"D:\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe")
"""
drvier.get("http://iess.03199.com/")
#给用户名的输入框标红
js="var q=document.getElementById(\"userName\");q.style.border=\"1px solid red\";"
drvier.execute_script(js)
#去掉日期控件的只读属性，使其可以手动输入
# js = "document.getElementById('txtBeginDate').removeAttribute('readonly')"  # 1.原生js，移除属性
# js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
# js = "$('input[id=txtBeginDate]').attr('readonly',false)"  # 3.jQuery，设置为false
js = "$('input[id=txtBeginDate]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
time.sleep(3)
 drvier.find_element_by_id('userName').send_keys("13272639137")
 drvier.find_element_by_id('password').send_keys("123456")
 drvier.find_element_by_xpath("//*[@id=/"page-layout/"]/div/div[4]/div/div/a[1]").click
 