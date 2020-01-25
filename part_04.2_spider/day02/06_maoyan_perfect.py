import os
from urllib import request
import re
from useragents import ua_list
import time
import random


class MaoyanSpider(object):
    def __init__(self, url):
        self.url = url

    # 功能1 获取响应内容
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        # print(headers)
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read()
        print(html[0:15])

        return html

    # 功能2 解析提取数据
    def re_func(self, re_bds, html):

        pattern = re.compile(re_bds, re.S)

        r_list = pattern.findall(html)

        return r_list

    # 功能3  获取想要的数据 - 解析一级页面
    def parse_html(self, url):
        one_html = self.get_html(url).decode()
        re_bds = '<p class="name"><a href="(.*?)" title=.*?data-act="boarditem-click" \
data-val=".*?">(.*?)</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">.*?(\d+.\d+.\d+).*?</p>'
        # one_list =  [('/html/592','name','actor','time'),(),(),.....]

        one_list = self.re_func(re_bds, one_html)
        # 直接调用数据处理函数
        self.write_html(one_list)

    # 功能4
    def write_html(self, one_list):
        item = {}
        for one in one_list:
            # one : 一个电影信息 包括 评论,图片...
            # 电影名称,主演,时间,评论,图片
            item['name'] = one[1]
            item['star'] = one[2].strip()
            item['time'] = one[3].strip()
            two_url = 'https://maoyan.com' + one[0]
            item['comment'] = self.get_comment(two_url)
            # 保存该电影所有图片

            print(two_url, item['name'])
            self.save_img(two_url, item['name'])

    # 从详情页中提取评论
    def get_comment(self, two_url):
        one_html = self.get_html(two_url).decode()
        re_bds = '<div class="comment-content">(.*?)</div>.*?</div>'

        comment_list = self.re_func(re_bds, one_html)
        # ['你不曾真的离去，你始终在我心里。\nMiss You Much Leslie',
        # '简直经典简直经典！！！即使是这么长的时间也令人不觉得厌烦 。每一个人都在用心的演，
        # 果然老片子就是老片子',
        # '总是为了你心痛。',
        # '片子是特别好 就是拷贝实在是旧到爆 音轨损失严重。真是应该修正蓝光数字什么的 这种经典影片影像质量还是很重要的。',
        # '人生如戏，戏如人生。

        return comment_list

    # 从详情页中提取出图片连接并把图片提取到本地
    def save_img(self, two_url, name):
        # 1.提取图片链接
        two_html = self.get_html(two_url).decode()
        re_bds = ' <img class="default-img" data-act="movie-img-click" data-src="(.*?)" alt="">'

        img_link_list = self.re_func(re_bds, two_html)

        # 2.保存图片 : img_link: http//xxx.jpg
        # /home/tarena/maoyan/top100/喜剧之王/
        # /home/tarena/maoyan/top100/霸王别姬/

        directory = '/home/tarena/maoyan/top100/{}/'.format(name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        for img_link in img_link_list:
            # img_link
            # https://p1.meituan.net/movie/767d387e6978ee559601d547f22eccca44664.jpg@465w_258h_1e_1c

            # 利用链接解决文件名问题
            filename = directory + img_link.split('/')[-1].split("@")[0]
            print(filename)
            # /home/tarena/maoyan/top100/霸王别姬/ccc0beb35f7f5c21ee75efab3b6eb5fb39201.jpg
            img_html = self.get_html(img_link)
            with open(filename, 'wb') as f:
                f.write(img_html)
            time.sleep(1)

    def run(self):
        for offset in range(0, 41, 10):
            url = self.url.format(offset)
            self.parse_html(url)
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    url = 'https://maoyan.com/board/4?offset={}'
    m01 = MaoyanSpider(url)
    m01.run()
