import requests

url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0'}

res = requests.get(url=url, headers=headers)
# 改编码
res.encoding = 'utf-8'
# 　<Response [200]>

# 抓字符
html = res.text

# 抓二进制文件
htmlb = res.content

# 抓网址
html_url = res.url
# www.baidu.com

# 抓响应码
html_stat = res.status_code
#200

print(html_stat)

