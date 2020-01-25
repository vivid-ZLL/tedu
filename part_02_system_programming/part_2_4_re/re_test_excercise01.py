import re

test_string01 = "alice@163.com,etc"
test_string02 = "1124_0102,etc,as usual"
test_string03 = "11,-12,650,13.6,4/5,45%,etc"
test_string04 = "H-base iPython"

c = re.findall("\w+@\w+.com", test_string01)
print(c)

c = re.findall("[0-9a-zA-Z_]{8,12}", test_string02)
print(c)

c = re.findall("-?\d+/?\.?\d*%?", test_string03)
print(c)

c = re.findall(r"\b[A-Z][-_a-zA-Z]*", test_string04)
print(c)

c = re.search("a", test_string01).group()
print(c)

print("匹配身份证号------------------------")
test = "51150219931124411X"
c = re.search(r"\d{17}(\d|X)", test).group()
print(c)

print("re模块功能函数演示------------------")
print("re 模块调用findall----------------")

s = "Alice:1994,Alicinya:1996"
pattern = r"\w+:\d+"  # 正则表达式
l = re.findall(pattern,s)
print("无子组",l)

pattern = r"(\w+):\d+"  # 正则表达式
l = re.findall(pattern,s)
print("一个子组",l)

pattern = r"(\w+):(\d+)"  # 正则表达式
l = re.findall(pattern,s)
print("两个子组",l)

# 也可以直接用compile创建对象调用findall



