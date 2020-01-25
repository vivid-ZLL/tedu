
"""
输入吧名,提取所有帖子内的图片和视频
"""



import requests
from lxml.html import etree
import time
import random
import pymongo


class TiebaImgSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {
            'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; "
                          "Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729;"
                          " Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['baiduSpider']
        self.myset = self.db['tiebaImg']
        self.i = 1

    # 通用功能 获取html
    def get_html(self, url, params=None):
        for i in range(1, 4):
            try:
                res = requests.get(url=url, headers=self.headers, params=params, timeout=5)
                html = res.content
                time.sleep(0.5)
                return html
            except Exception:
                print('Failed connected with', url)
                continue

    # 通用功能 解析xpath
    def xpath_func(self, html, xpath_bds):
        parse_obj = etree.HTML(html)
        r_list = parse_obj.xpath(xpath_bds)

        return r_list

    # 主要功能 提取一级html信息
    def parse_html(self, url, params):
        # 提取帖子链接
        try:
            one_html = self.get_html(url, params=params).decode()
        except Exception:
            return
        xpath_bds = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        tlink_list = self.xpath_func(one_html, xpath_bds)
        # ['/html/xxx',...]

        # 提取一级页帖子链接
        for tlink in tlink_list:
            tlink = 'http://tieba.baidu.com' + tlink
            # http://tieba.baidu.com/xxx
            self.get_img(tlink)
            self.i = int(self.i) + 1

    # 主要功能 进入帖子链接地址,提取图片链接
    def get_img(self, tlink):
        try:
            html = self.get_html(tlink).decode('utf-8', 'ignore')
        except Exception:
            return
        xpath_bds = '//div[@class="video_src_wrapper"]/embed/@data-video' \
                    '|//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src'
        img_link_list = self.xpath_func(html, xpath_bds)
        for img_link in img_link_list:
            # 进入图片链接,保存图片
            self.save_image(img_link)

    def save_image(self, img_link):
        try:
            html = self.get_html(img_link)
        except Exception:
            return
        img_name = img_link.split('/')[-1]
        if self.img_is_repeated(img_name):
            return
        direction = './baidu_img/'
        # filename = direction + 'topic{}_'.format(round(self.i,1))  # +img_link.split('/')[-1]
        filename = direction + 'topic{}_.jpg'.format(round(self.i, 1))
        self.i += 0.1
        with open(filename, 'wb') as f:
            f.write(html)
        print(filename, '下载成功')

    def run(self):
        name = input('贴吧名')
        start = int(input('起始页'))
        end = int(input('终止页:'))
        for page in range(start, end + 1):
            pn = (page - 1) * 50
            params = {
                'kw': name,
                'pn': pn
            }
            self.parse_html(self.url, params)
            print('第%d页抓取完成' % page)

            # 每爬取一个页面,休眠1-3秒
            time.sleep(random.randint(1, 3))

    def img_is_repeated(self, img_name):
        """
            图片重复,return True
        """
        item = {'name': img_name}
        re = self.myset.find_one(item)
        if not re:
            self.myset.insert_one(item)
        else:
            print(img_name, '数据已存在')
            return True


if __name__ == "__main__":
    spider = TiebaImgSpider()
    begin = time.time()
    spider.run()
    stop = time.time()
    time0 = stop - begin
    print('总执行的时间为%.2f' % time0)
