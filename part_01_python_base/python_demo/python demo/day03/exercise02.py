"""
    练习:在控制台中获取一个季度(春夏秋冬)，
        显示相应的月份。
        春 --> １月２月３月
        夏 --> ４月５月６月
        秋 --> ７月８月９月
        冬 --> １０月１１月１２月
    14:18
"""
season = input("请输入季度：")
# if season == "春":
#     print("１月２月３月")
# if season == "夏":
#     print("４月５月６月")
# if season == "秋":
#     print("７月８月９月")
# if season == "冬":
#     print("１０月１１月１２月")

# 相比上面代码的优点：如果前面条件满足，后续条件不再判断。
if season == "春":
    print("１月２月３月")
elif season == "夏":
    print("４月５月６月")
elif season == "秋":
    print("７月８月９月")
elif season == "冬":
    print("１０月１１月１２月")






