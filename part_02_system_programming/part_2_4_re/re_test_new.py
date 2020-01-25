import re

s = """Hail
Roy
歌莉娅
"""

regex = re.compile(r".+", flags=re.S)
l = regex.findall(s)
print(l)
