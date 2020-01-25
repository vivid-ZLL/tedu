import re

s = "Alice: alice@gensoko.cn"

c = re.findall("\w+@", s)
print(c)

# 字符集
c = re.findall("[Aa]", s)
print(c)
c = re.findall("[A-z]", s)
print(c)
c = re.findall("[poas5-p]", s)
print(c)
# 字符集取反
c = re.findall("^[a5-p]", s)
print(c)
c = re.findall("^[A]", s)
print(c)

# "或"关系
c = re.findall("Al|a", s)
print(c)

# 任意字符
c = re.findall("A.", s)
print(c)

# 匹配字符串的开头位置
c = re.findall("^alice", "alice,hello")  # ['alice']
print(c)

# 匹配字符串的结尾位置
c = re.findall("ice$", "Alice")  # ['ice']
print(c)

# ------------------完全匹配字符串的位置--------------------------
c = re.findall("alice$", "for alice")  # ['alice']
print(c)

# ----------------------匹配前的字符出现0次或多次----------------------
c = re.findall("al*", "alice is the best ahhhhh")  # ['al', 'a']
print(c)
# 匹配所有单词
# 一个小写字母或一个大写字母出现一次或多次
c = re.findall("[a-zA-Z]+", "alice is the best ahhhhh")  # ['alice', '', 'is', '', 'the', '', 'best', '', 'ahhhhh', '']
print("c:", c)

# 匹配首字母大写
# 一个大写字母加一个小写字母重复0次或多次
c = re.findall("[A-Z][a-z]*",
               "Alice is the best Ahhhhh")  # ['Alice', 'A']
print(c)

# ---------------------------------------------
# 匹配的字符出现0次或一次  如ab? --> 只能匹配a或者ab
# ----------------------------------------------

# 匹配整数
# 负号出现0次或多次 + 0-9 的数字
c = re.findall('-?[0-9]+', "alice:18, -26")  # ['18', '-26']
print("int:", c)

# 匹配除空格的所有字符
# 不要空格 任意字符出现一次或多次
c = re.findall("[^ ]+", "alice lkjw $& 873")  # ['alice', 'lkjw', '$&', '873']
print(c)

# 匹配手机号码
# 1开头的数 加 [0-9]的数字出现10次
re.findall('1[0-9]{10}', "Jame:13886495728")  # ['13886495728']

# ab{1,2}  -->  ab abb


# 匹配QQ号
c = re.findall("[1-9][0-9]{5,10}", "qq:283438692")  # ['283438692']
print(c)

# /d == [0-9]  /D == ^[0-9]
# 匹配端口号
re.findall('\d{1,5}', "Mysql: 3306, http:80")  # ['3306', '80']

# \w+  数字 字母 下划线 汉字 即普通的utf - 8 字符
re.findall('\w+', "server_port = 8888")  # ['server_port', '8888']

#### 匹配任意（非）空字符

# * 元字符： \s   \S
#
# * 匹配规则: \s 匹配空字符，\S 匹配非空字符
#
# * 说明：空字符指 空格 \r \n \t \v \f 字符

# 匹配数字
c = re.findall("-?\d+\.?\d*", "45,-65,1.3,-1.3")
print(c)

c = re.findall('\[.*?\]', "[alice],[alicinya],[iris][margatroid]")
print(c)
