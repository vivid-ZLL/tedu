from urllib import request

# urlopen() 向url发送请求,返回响应对象
res = request.urlopen('http://www.httpbin.org/get')
# 提取响应内容
html = res.read().decode('utf-8')
# 打印响应内容
print(html)

# html为字符串(特别长)
# read():bytes  read().decode():string

url = res.geturl()
print(url)
code = res.getcode()
print(code)
