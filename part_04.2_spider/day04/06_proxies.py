import requests
import fake_useragent

url = 'http://httpbin.org/get'
# url = 'http://www.baidu.com/'
ip = '61.164.39.66:53281'
headers = {'User-Agent':fake_useragent.UserAgent().random}


proxies = {
    'http': 'http://{}'.format(ip),
    # 'http': 'http://61.157.206.174:37259',
    'https': 'https://{}'.format(ip),
}

for i in range(7,12):
    try:
        html = requests.get(url=url, proxies=proxies, timeout=8,headers=headers)
        html.encoding='utf-8'
        print(html.text)
        break
    except Exception as e:
        pass




