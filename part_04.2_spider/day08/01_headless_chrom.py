from selenium import webdriver


# 设置无界面
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--headless')
# 创建浏览器对象
browser = webdriver.Chrome(options=options)
browser.get('https://www.baidu.com')
browser.save_screenshot('baidu.png')
