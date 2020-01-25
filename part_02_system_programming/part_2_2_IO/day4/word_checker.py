def word_check(target_word):
    target = target_word
    dict01 = open("dict.txt", "r")
    while True:
        data = dict01.readline()

        # print(data)

        if not data:
            print("没有找到单词oh yeah")
            break
        elif data[:len(target)] == target:
            # print(data)
            return data







