"""
    通用操作str
"""

str01 = "悟空"
str02 = "八戒"
# 字符串拼接
str03 = str01 + str02
# 　字符串累加
str01 += str02
print(str01)

# 重复生成元素
print(str02 * 3)#八戒八戒八戒
str02 *=3
print(str02)
# 依次比较两个容器中元素,一但不同则返回比较结果。
print("a悟空" > "b八戒")

#　成员运算符
print("我叫" in "我叫齐天大圣")

# 索引
message = "我叫齐天大圣"
# 获取正数第三个字
print(message[3])
# 获取最后一个字
print(message[-1])

# 切片
print(message[0:2])# 我叫
# 开始值默认为开头
print(message[:2])# 我叫
# 结束值默认为末尾
print(message[-2:])# 大圣
print(message[:])#我叫齐天大圣

print(message[-2:-5:-1])#大天齐
print(message[::-1])# 圣大天齐叫我

print(message[1:1])# 空
print(message[3:1])# 空
print(message[-2:1])# 空
# 索引不能越界
# print(message[7])
# 切片越界不报错
print(message[1:7])# 叫齐天大圣








