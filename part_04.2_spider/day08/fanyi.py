import re
import execjs
import requests
import json


class BaiduTranslate:
    def __init__(self):
        self.get_url = 'https://fanyi.baidu.com/?aldtype=16047'
        self.post_url = 'https://fanyi.baidu.com/v2transapi'
        self.headers = {

            # "accept": " */*",
            # "accept-encoding": " gzip, deflate, br",
            # "accept-language": " zh-CN,zh;q=0.9",
            # "content-length": " 121",
            # "content-type": " application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "BAIDUID=33F73A12F1C59AA0A6A58671D045D815:FG=1; PSTM=1568272125; BIDUPSID=3D3508B0D3A4999CEEA92269E5813851; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[mkUqnUt8juD]=aeXf-1x8UdYcs; delPer=0; H_PS_PSSID=1461_21093_29522_29519_29568_29220; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1568789935,1568794846; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1568794864; __yjsv5_shitong=1.0_7_9ddad96b49e57b93d7decb75275d47e0310c_300_1568794863156_43.254.90.134_4162b891; yjs_js_security_passport=d756d16051617d22fa323aee5e91f68bc8b76c5e_1568794866_js",
            # "origin" : " https://fanyi.baidu.com",
            "referer":" https://fanyi.baidu.com/?aldtype=16047",
            "user-agent": " Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            # "x-requested-with": " XMLHttpRequest",

        }

    def get_token_gtk(self):
        html = requests.get(
            url=self.get_url,
            headers=self.headers
        ).text

        gtk = re.findall("window.gtk = '(.*?)'", html)[0]
        token = re.findall("token: '(.*?)'", html)[0]
        # print(gtk, token)
        return token, gtk

    def get_sign(self, word, gtk):
        with open('translate.js', 'r') as f:
            js_data = f.read()
        exec_obj = execjs.compile(js_data)
        sign = exec_obj.eval('e("{}","{}")'.format(word, gtk))

        return sign

    def run(self):
        word = input('please enter your word:')
        token, gtk = self.get_token_gtk()
        sign = self.get_sign(word, gtk)

        # print(token,gtk,sign)
        # print(sign)
        # input()
        data = {
            "from": "auto",
            "to": "auto",
            "query": word,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": token
        }
        html = requests.post(
            url=self.post_url,
            data=data,
            headers=self.headers
        ).json()

        result = html['trans_result']['data'][0]['dst']


        print(html)
        print(result)

b01 = BaiduTranslate()
b01.run()
# 00fa0e980a98ac6b4f487b6f8d0d6158 320305.131321201 112152.349481