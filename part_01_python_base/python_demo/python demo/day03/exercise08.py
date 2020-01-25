# 　练习:使下列代码循环执行，按e键退出。
#  调试程序

while True:
    season = input("请输入季度：")
    if season == "春":
        print("１月２月３月")
    elif season == "夏":
        print("４月５月６月")
    elif season == "秋":
        print("７月８月９月")
    elif season == "冬":
        print("１０月１１月１２月")

    if input("输入e键退出:") == "e":
        break
