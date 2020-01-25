from selenium import webdriver
import time


# 创建浏览器对象
browser = webdriver.Chrome()

# 地址栏输入 百度地址
browser.get('http://www.baidu.com/')

# 在搜索框输入""
# //*[@id="kw"]

kw = browser.find_element_by_xpath('//*[@id="kw"]')
kw.send_keys('Alice Margatroid')

# 点击搜索按钮
#  //*[@id="su"]
su = browser.find_element_by_xpath('//*[@id="su"]')
su.click()
