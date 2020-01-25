from selenium import webdriver
import mysql_helper


class GovSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'

        self.browser = webdriver.Chrome()

        self.mysql = mysql_helper.MysqlHelper(database='govdb')
        self.province_list = []
        self.city_list = []
        self.county_list = []

    def get_data(self):
        self.browser.get(self.url)
        a = self.browser.find_element_by_xpath('//div//a[contains(@title,"行政区划代码")]')
        # 自动补全域名
        href = a.get_attribute('href')
        res = self.mysql.find('version', f'where url = "{href}"')
        if res:
            print('区划列表已存在,结束抓取')
            return

        self.mysql.delete_all("version", "")
        self.mysql.add_one('version', [href])
        # 在version表中查询,得到一个结果result
        print(href)

        a.click()
        self.get_code()

    def get_code(self):
        # 切换句柄
        all_handles = self.browser.window_handles
        self.browser.switch_to.window(all_handles[1])
        # 抓数据
        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            print(name, code)
            if code[-4:] == '0000':
                self.province_list.append([name, code])
                # 直辖市加到city表
                if name in ['北京市', '上海市', '天津市', '重庆市']:
                    self.city_list.append([name, code, code])

            elif code[-2:] == '00':
                self.city_list.append([name, code, (code[0:2] + '0000')])
            else:
                if code[:2] in ['11', '12', '31', '50']:
                    self.county_list.append([name, code, code[:2] + '0000'])
                else:
                    self.county_list.append([name, code, (code[0:4] + '00')])
        self.insert_mysql()

    def insert_mysql(self):
        # 清空所有表
        self.mysql.delete_all('province', '')
        self.mysql.delete_all('city', '')
        self.mysql.delete_all('county', '')
        self.mysql.add_many('province',self.province_list)
        self.mysql.add_many('city',self.city_list)
        self.mysql.add_many('county',self.county_list)


g01 = GovSpider()
g01.get_data()
"""
select province.p_name,city.c_name,county.x_name from province inner join city on province.p_code = city.c_father_code inner join county on city.c_code = county.x_father_code;
"""

"""
select province.p_name,city.c_name,county.x_name from province,city,county where prvince.p_code = city.c_father_code and city.c_code =county.x_father_code
"""


