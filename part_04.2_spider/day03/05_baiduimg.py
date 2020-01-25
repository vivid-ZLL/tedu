import requests
from urllib import parse
import re
import os
from useragents import ua_list
import time
import random


class BaiduImageSpider:
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'
        # 计数
        self.i = 1

    # 获取图片
    def get_img(self, url, name):
        headers = {'User-Agent': random.choice(ua_list)}
        # 获取图片列表
        html = requests.get(url=url, headers=headers).text
        pattern = re.compile('"middleURL":"(.*?)"', re.S)
        img_link_list = pattern.findall(html)
        print(len(img_link_list))
        print(img_link_list)
        # 创建下载文件夹  /home/tarena/imgs/名字

        directory = '/home/tarena/imgs/{}/'.format(name)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # for 循环遍历,下载每张图片
        for img_link in img_link_list:
            self.save_img(img_link, directory, name)
            time.sleep(random.randint(1, 2))

    def save_img(self, img_link, directory, name):
        headers = {'User-Agent': random.choice(ua_list)}
        # 1.向图片链接发请求,得到byte类型
        html = requests.get(url=img_link, headers=headers).content


        filename = directory + "{}_{}.jpg".format(name, self.i)
        # 2.命名文件名,以wb方式保存图片
        with open(filename, 'wb') as f:
            f.write(html)
        self.i += 1
        print(filename, '下载成功')

    # 入口函数
    def run(self):
        name = input('你渴望力量吗? -- >')
        name1 = parse.quote(name)

        url = self.url.format(name1)
        self.get_img(url, name)


if __name__ == '__main__':
    b01 = BaiduImageSpider()
    b01.run()

