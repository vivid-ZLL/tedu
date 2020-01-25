import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=' \
      'b9999_10000&sec=1568097492031&di=6f6292fa0c168a56e019f150' \
      'b6710d25&imgtype=0&src=http%3A%2F%2Fp3.music.126.net%2FlVgQryCe' \
      'NgCyn6C84WpTyQ%3D%3D%2F5949457418169260.jpg%3Fparam%3D180y180'

headers = {'User-Agent': 'Mozilla/5.0'}

html = requests.get(url=url, headers=headers).content

with open("alice.jpg", 'wb') as f:
    f.write(html)
