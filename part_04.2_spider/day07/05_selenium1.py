from selenium import webdriver
import requests
import time
<<<<<<< HEAD
=======
<<<<<<< HEAD:part_04.2_spider/day07/05_senenium.py
import scipy

# 创建浏览器对象
browser = webdriver.Firefox()

=======
>>>>>>> d296d4f798072d633ab61f370c741649018801a4
from PIL import Image

# 创建浏览器对象
browser = webdriver.Firefox()
<<<<<<< HEAD
=======
>>>>>>> 944d8b1c71514e2c0199dbbd2eb013e73599635d:part_04.2_spider/day07/05_selenium1.py
>>>>>>> d296d4f798072d633ab61f370c741649018801a4
# 地址栏输入 百度地址
browser.get('http://www.baidu.com/')

browser.get_screenshot_as_file('00001.png')
# 停留5秒
time.sleep(5)

#  关闭浏览器
browser.quit()
