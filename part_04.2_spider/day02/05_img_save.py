from urllib import request

url = 'https://c-ssl.duitang.com/uploads/item/201702/19/20170219105214_amnKx.jpeg'
res = request.urlopen(url)
html = res.read()

with open('alice.jpg','wb') as f:
    f.write(html)

