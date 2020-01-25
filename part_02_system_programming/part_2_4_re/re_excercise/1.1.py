# （1.1）分组提取
# 需求：在分组1中匹配meta中author属性的值
# 源串：
#
# another author="Zjmainstay too"
# 预期：分组1得到Zjmainstay
# 正则："(\w\b) 用"作为锚点 \b判断结束位置 ()取得分组 \w 取得字符串 匹配次数
# 题样：http://regex.zjmainstay.cn/r/naCgc7/1
import re
def print_custom(str):
    def wrapper(func):
        def deco(*args, **kwargs):
            print(str)

            return func(*args, **kwargs)
        return deco
    return wrapper


another_author="Zjmainstay too"

@print_custom("\w")
def pr(re_0,):
    result = re.search(r"\w",another_author)
    print(result.group())

pr()

