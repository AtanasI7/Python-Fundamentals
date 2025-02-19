def synonyms(data):
    dict_synonyms = dict()



    for i in range(1, data * 2 + 1):
        new_data = input()

        if i % 2 != 0:
            dict_synonyms[new_data] = list()
            special_word = new_data
        else:
            dict_synonyms[special_word] = new_data





info = int(input())
synonyms(info)

