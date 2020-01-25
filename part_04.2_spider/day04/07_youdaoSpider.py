import requests
import time
import random
from hashlib import md5

data01 = {
    "i": "alice",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15682647149209",
    "sign": "0810dc9ab85bf448fa6f0b0824ae4849",
    "ts": "1568264714920",
    "bv": "59a2ee1b62619c43589e27bb52c2517a",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
}

data02 = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "238",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "OUTFOX_SEARCH_USER_ID=1677373506@110.184.225.26; "
              "OUTFOX_SEARCH_USER_ID_NCOO=962708536.8339987; "
              "_ntes_nnid=7e7c850688d24000770b0a4dc051facd,1568162322282; "
              "DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; "
              "JSESSIONID=abcoamr6DlS3XcKoxoJ0w; ___rl__test__cookies=1568264714917",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",

}


class YoudaoSpider(object):
    def __init__(self):
        # F12 抓到的url地址
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = data02

    def get_ts_salt_sign(self, word):
        # ts
        ts = int((time.time() * 1000))
        # salt
        salt = str(ts) + str(random.randint(0, 9))
        # sign
        # "fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj"
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts, salt, sign

    # 攻克有道
    def attack_yd(self, word):
        ts, salt, sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "59a2ee1b62619c43589e27bb52c2517a",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        res = requests.post(self.url, data, headers=self.headers)
        html = res.json()

        # print(res.text)  # 'str'
        print(html)  # 'dict'

        result = html['translateResult'][0][0]['tgt']

        return result

    def run(self):
        word = input("请输入要翻译的单词")
        result = self.attack_yd(word)
        print('翻译结果:', result)


if __name__ == "__main__":
    s01 = YoudaoSpider()
    s01.run()
