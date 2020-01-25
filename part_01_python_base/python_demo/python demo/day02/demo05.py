"""
    bool
    运算符
        比较运算符  >  <  >=  <=  等于==  不等于!=
        　　　结果是：ｂｏｏｌ类型
        逻辑运算符：判断两个ｂｏｏｌ值关系
          　　　　　　与　　或　　　非
"""
# １．　bool 类型
# 取值：(真，对的，满足条件)True (假，错的，不满足条件)False
# 命题:带有判断性的陈述句。
# 例如：我是个男人。
#  1  > 2   -->  False
print(1 > 2)

# 2. 逻辑运算符
#   －－　与：一假俱假,表示并且(都得满足)的关系
print(True and True)  # True　都得满足条件，结论才满足条件。
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

#   －－　或：一真俱真,表示或者(一个满足就行)的关系
print(True or True)  # True　
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

#   －－　非：取反
print(not True)

# 练习：判断年份是否为闰年。
# 闰年Ｔｒｕｅ:年份能被4整除，但是不能被100整除。
#      能被400整除
# 平年Ｆａｌｓｅ
year = int(input("请输入年份："))
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(result)











