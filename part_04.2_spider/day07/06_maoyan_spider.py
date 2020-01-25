from selenium import webdriver

url = 'https://maoyan.com/board/4'
browser = webdriver.Chrome()
browser.get(url)
# 基准xpath: []
li_list = browser.find_elements_by_xpath('//dd')
for li in li_list:
    print(li.text)



    # item = {}
    # info_list = li.text.split('\n')
    # # ['1', '霸王别姬', '主演：张国荣,张丰毅,巩俐', '上映时间：1993-01-01', '9.5']
    # item['number'] = info_list[0]
    # item['name'] = info_list[1]
    # item['actor'] = info_list[2]
    # item['time'] = info_list[3]
    # item['score'] = info_list[4]
    #
    # print(item)

"""
1\n霸王别姬\n主演：张国荣,张丰毅,巩俐\n上映时间：1993-01-01\n9.5
"""
