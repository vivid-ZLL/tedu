list01 = []
for year in range(1970,2051):
    if year % 4 == 0 and year % 400 != 0 or year % 400 == 0:
        list01.append(year)
print(list01)

list01 = [year for year in range(1970,2051) if year % 4 == 0 and year % 400 != 0 or year % 400 == 0]
print(list01)