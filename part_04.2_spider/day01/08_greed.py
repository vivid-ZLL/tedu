import re

html = '''
<div><p>九霄龙吟惊天变</p></div>   
<div><p>风云际会浅水游</p></div>   

'''
# 贪婪匹配
pattern = re.compile(r'<div><p>(.*?)</p></div>', re.S)
re_list = pattern.findall(html)

print(re_list)
