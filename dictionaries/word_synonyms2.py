def synonyms(data):
    dict_synonyms = dict()
    values_list = list()

    for i in range(1, data * 2 + 1):
        new_word = input()

        if i % 2 != 0:
            if new_word not in dict_synonyms.keys():
                dict_synonyms[new_word] = list()
                special_word = new_word

        else:
            values_list.append(new_word)

info = int(input())
synonyms(info)