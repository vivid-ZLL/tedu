"""
输入吧名,提取所有帖子内的图片和视频
"""

from urllib import parse
import requests
from lxml.html import etree
import time
import random


class TiebaImgSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {
            'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; "
                          "Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729;"
                          " Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}

    # 通用功能 获取html
    def get_html(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content
        return html

    # 通用功能 解析xpath
    def xpath_func(self, html, xpath_bds):
        parse_obj = etree.HTML(html)
        r_list = parse_obj.xpath(xpath_bds)

        return r_list

    # 主要功能 提取一级html信息
    def parse_html(self, url):
        # 提取帖子链接
        one_html = self.get_html(url).decode()
        xpath_bds = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        tlink_list = self.xpath_func(one_html, xpath_bds)
        # ['/html/xxx',...]

        # 提取一级页帖子链接
        for tlink in tlink_list:
            tlink = 'http://tieba.baidu.com' + tlink
            # http://tieba.baidu.com/xxx
            self.get_img(tlink)

    # 主要功能 进入帖子链接地址,提取图片链接
    def get_img(self, tlink):
        html = self.get_html(tlink).decode('utf-8', 'ignore')
        xpath_bds = '//div[@class="video_src_wrapper"]/embed/@data-video' \
                    '|//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src'
        img_link_list = self.xpath_func(html, xpath_bds)
        for img_link in img_link_list:
            # 进入图片链接,保存图片
            self.save_image(img_link)

    def save_image(self, img_link):
        html = self.get_html(img_link)
        direction = './baidu_img/'
        filename = direction + img_link.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(html)
        print(filename, '下载成功')

    def run(self):
        name = input('贴吧名')
        start = int(input('起始页'))
        end = int(input('终止页:'))
        name1 = parse.quote(name)
        for page in range(start, end + 1):
            pn = (page - 1) * 50
            url = self.url.format(name1, pn)
            self.parse_html(url)
            print('第%d页抓取成功' % page)

            # 每爬取一个页面,休眠1-3秒
            time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    spider = TiebaImgSpider()
    begin = time.time()
    spider.run()
    stop = time.time()
    time0 = stop - begin
    print('总执行的时间为%.2f' % time0)
