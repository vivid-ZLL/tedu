int_year = int(input("请输入年份："))
result = (int_year % 4 == 0 and int_year % 100 != 0
          or int_year % 400 == 0)
print(result)
