list01 = []
result = []
list03 = []
list04 = []
count_01 = 0
count_02 = 0
while count_01 < 7:
    count_02 +=1
    count_01 = 0
    list01 = []
    result = []
    list03 = []
    list04 = []
    code_count = 1

    import random

    while code_count <= 6:
        random_number = random.randint(1, 33)
        if random_number not in list01:
            list01.append(random_number)
            code_count += 1

    code_count = 1
    while code_count <= 6:
        random_number = random.randint(1, 33)
        if random_number not in result:
            result.append(random_number)
            code_count += 1

    code_count = 1
    while code_count <= 1:
        random_number = random.randint(1, 16)
        if random_number not in list03:
            list03.append(random_number)
            code_count += 1

    code_count = 1
    while code_count <= 1:
        random_number = random.randint(1, 16)
        if random_number not in list04:
            list04.append(random_number)
            code_count += 1


    print(list01, result, list03, list04)
    for item in result:
        if item in list01:
            count_01 += 1

    for item in list04:
        if item in list03:
            count_01 += 1

    print(count_02)
    print(count_01)
