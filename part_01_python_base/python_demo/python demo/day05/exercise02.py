# 练习:在控制台中录入，所有学生成绩.
# 输入空字符串，打印(一行一个)所有成绩.
# 打印最高分,打印最低分,打印平均分.
# 11:41

list_score = []
# 录入过程
while True:
    str_score = input("请输入成绩：")
    if str_score == "":
        break
list_score.append(int(str_score))  # 输出过程
for item in list_score:
    print(item)

print("最高分：" + str(max(list_score)))
print("最低分：" + str(min(list_score)))
print("平均分：" + str(sum(list_score) / len(list_score)))
