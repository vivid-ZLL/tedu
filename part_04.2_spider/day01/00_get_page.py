import time
from urllib import request


# 1.拼接url地址函数:

def get_url(baseurl):
    # baseurl = 'http://www.baidu.com/s?wd='
    # 编码 + 拼接
    # params = parse.quote(word)
    # url = baseurl + params

    return baseurl


# 2.请求 + 保存
def write_html(url):
    # 拿到响应内容
    req = request.Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    )
    # 获取响应对象
    res = request.urlopen(req)
    # 拿到响应内容
    html = res.read().decode('utf-8')
    # 保存到本地文件
    filename = 'result' + '.html'
    with open(filename, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    word = 'https://maoyan.com/board/4'
    url = get_url(word)
    try:
        write_html(url)
    except Exception as e:
        print(e)
        time.sleep(2)
