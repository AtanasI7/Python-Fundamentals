def count_chars(words):
    words = words.split(' ')
    char_dict = dict()

    for i in words:
        for j in i:
            if j not in char_dict:
                char_dict[j] = 0
            char_dict[j] += 1

    for k in char_dict.keys():
        print(f"{k} -> {char_dict[k]}")

data = input()
count_chars(data)
