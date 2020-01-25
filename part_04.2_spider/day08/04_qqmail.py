from selenium import webdriver


class QQSpider:
    def __init__(self):
        self.url = 'https://mail.qq.com/'
        self.browser = webdriver.Chrome()

    def main(self):
        self.browser.get(self.url)

        # 切换iframe子框架
        login_iframe = self.browser.find_element_by_id('login_frame')

        self.browser.switch_to.frame(login_iframe)

        # 2.找节点:user,password,login
        user = self.browser.find_element_by_id('u').send_keys('1346037005')
        #
        pwd = self.browser.find_element_by_id('p').send_keys('qq987415~')
        login_button = self.browser.find_element_by_id('login_button').click()


q01 = QQSpider()
q01.main()
