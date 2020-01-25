"""
6. (扩展)一个小球从１００ｍ的高度落下
    　　每次弹回原高度的一半．
    　　计算：总共弹起来多少次（最小弹起高度0.01ｍ）．
            总共走了多少米
"""
#10:35 上课
height = 100
count = 0
# 经过距离
distance = height
# 弹起前高度 大于　最小弹起高度
# while height > 0.01:
# 弹起来的高度 大于　最小弹起高度
while height / 2 > 0.01:
    count += 1
    # 弹起
    height /= 2
    print("第%d次弹起来的高度是%f." % (count, height))
    # 累加起/落高度
    distance += height * 2

print("总共弹起来%d次" % count)
print("总共经过的距离是%.2f" % distance)
