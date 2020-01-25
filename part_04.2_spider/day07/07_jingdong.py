import time

from selenium import webdriver


class Jdspider:
    def __init__(self):
        self.i = 0
        self.url = 'https://www.jingdong.com'
        self.browser = webdriver.Chrome()
        # 创建浏览器对象

    # 　跳转到商品页－爬虫书
    def get_html(self):
        """
               //*[@id="key"]
        """
        # 找节点，send_keys() click()
        self.browser.get(self.url)
        kw = self.browser.find_element_by_xpath('//*[@id="key"]')
        kw.send_keys('爬虫书')
        btn = self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
        btn.click()
        # 任何刷新页面的行为都必须给页面留出加载时间
        time.sleep(3)

    # 匹配每个商品信息的li节点列表,li.text
    def parse_html(self):
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(5)
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            item = {}
            # element
            item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
            item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text.strip()
            item['comment'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text.strip()
            item['market'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text.strip()
            print(item)
            print(self.i)
            self.i += 1

    def run(self):
        self.get_html()
        for i in range(10):
            self.parse_html()
            if self.browser.page_source.find('pn-next disabled') == -1:
                # 说明点击下一页按钮是可用的
                self.browser.find_element_by_class_name('pn-next').click()
                # 任何点击事件都需要给新的页面加载预留时间
                time.sleep(3)
                print(f'第{i+1}页抓取完成')
                # print(self.i)
            # else:
            #     break


j01 = Jdspider()
j01.run()
"""
￥47.40\nPython网络爬虫从入门到实践 第2版 电子工业出版社博文视点品牌庆,惊喜奉送互联网专业人员阅读书单,千种好书领券享满100-40
会场直达\n80+条评价\n机械工业出版社\n自营\n放心购\n关注\n加入购物车\n电子书\n￥30.00\n
"""
