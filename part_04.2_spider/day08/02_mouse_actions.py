from selenium import webdriver


# 设置无界面
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# 创建浏览器对象
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 鼠标移动到设置节点
set_node = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
mouse_obj = ActionChains(browser)
mouse_obj.move_to_element(set_node).perform()

# 找 高级搜索节点 点击
browser.find_element_by_link_text('高级搜索').click()