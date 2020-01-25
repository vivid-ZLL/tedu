from lxml.html import etree
url = 'https://maoyan.com/board/4?offset=0'

parse_obj = etree.HTML(url)
print(parse_obj)
dd_list = parse_obj.xpath('//div')
print(dd_list)