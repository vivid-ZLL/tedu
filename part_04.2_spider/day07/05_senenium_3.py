from selenium import webdriver
import time


# 创建浏览器对象
browser = webdriver.Chrome()

# 地址栏输入 百度地址
browser.get('http://www.baidu.com/')

res = browser.page_source.find('kw')
print(res)

res = browser.find_elements_by_xpath('//div')
print(res)
for li in res:
    print(li.text)