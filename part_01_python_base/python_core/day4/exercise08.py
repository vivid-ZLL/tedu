# result_1  = 0
# for item in range(1, 101):
#     result_1 += item
# print(result_1)
#
# result_2 = 0
# for count in range(2, 101, 2):
#     result_2 += count
# print(result_2)
#
# result_3 = 0
# for item_3 in range(10, 37):
#     result_3 += item_3
# print(result_3)
result = 0
for item in range(10,51):
    if item % 10 == 2:
        continue
    elif item % 10 == 5:
        continue
    elif item % 10 == 9:
        continue
    result += item
    print(item)
print(result)

