import requests
from lxml import etree


class Session:
    def __init__(self):
        self.post_url = 'http://www.renren.com/PLogin.do'
        self.get_url = 'http://www.renren.com/972267469/profile'
        self.session = requests.session()

    # 提取数据,先post再get
    def parse_html(self):
        data = {
            'email': '13408315672',
            #
            'password': 'rr987415~'
        }

        # 先post,把cookie保存在session对象中 - 会话保持
        self.session.post(self.post_url, data=data)
        # 再get,正常抓取数据
        html = self.session.get(self.get_url).text
        parse_obj = etree.HTML(html)
        xpath_bds = '//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'
        r_list = parse_obj.xpath(xpath_bds)
        print(r_list)

    def run(self):
        self.parse_html()


s01 = Session()
s01.run()
