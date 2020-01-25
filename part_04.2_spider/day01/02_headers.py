from urllib import request
from urllib import parse

# 创建请求对象
req = request.Request(
    url='http://httpbin.org/get',
    headers={
        # 'User-Agent': 'hahahahahahaha'
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
)

# 获取响应对象
res = request.urlopen(req)

# 读取内容
html = res.read().decode('utf-8')

print(html)
