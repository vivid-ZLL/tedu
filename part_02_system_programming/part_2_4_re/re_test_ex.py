import re
s = "今年是2019年,建国70周年"
pattern = r"\d+"


it = re.finditer(pattern,s)

for i in it:
    print(i.group())


c = re.fullmatch(r"[\w,]+",s)
print("fullmatch测试:",c.group())

c = re.match(r"今年",s)
print("match 测试 : ",c.group())


pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj01 = regex.search("abcdefghi") # match对象

print("目标字符串开始位置:",obj01.pos)
print("目标字符串结束位置:",obj01.endpos)

# -------------------

print("正则表达式: ",obj01.re)
print("目标字符串",obj01.string)

# 属性方法
print("匹配内容在字符串中的位置: ",obj01.span())
print("匹配内容在字符串中开始的位置: ",obj01.start())
print("匹配内容在字符串中结束的位置: ",obj01.end())

print("捕获组字典: ",obj01.groupdict())
print("子组对应内容的元组: ",obj01.groups())
print("匹配结果:",obj01.group(0))  # 默认参数为0,表示匹配所有内容