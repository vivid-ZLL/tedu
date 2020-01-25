state = "偶数" if \
    int(input("请输入一个整数")) % 2 == 0 else "奇数"

code_year = int(input("请输入年份"))


year = "闰年" if code_year % 4 == 0 and code_year % 100 != 0 \
                or code_year % 400 == 0 else "平年"

print(year)

