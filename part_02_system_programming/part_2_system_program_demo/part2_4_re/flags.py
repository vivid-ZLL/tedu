"""
flags.py
flags 扩展功能演示
"""
import re

s = """Hello 
北京
"""

# 只能匹配ASCII编码
# regex = re.compile(r'\w+',flags=re.A)

# 不区分大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

# .可以匹配换行
# regex = re.compile(r'.+',flags= re.S)

# ^,$ 匹配每一行开头结尾位置
# regex = re.compile(r'^北京',flags=re.M)

# 给正则分行注释
pattern = r"""\w+ # hello
\s+  # 匹配换行
\w+ # 北京
"""

regex = re.compile(pattern,flags=re.X|re.I)

l = regex.findall(s)
print(l)

