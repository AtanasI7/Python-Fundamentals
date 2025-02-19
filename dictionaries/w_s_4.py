def synonyms(number):
    wanted_dict = dict()

    for i in range(number):
        word = input()
        synonym = input()

        if word not in wanted_dict.keys():
            wanted_dict[word] = list()
        wanted_dict[word].append(synonym)

    for key in wanted_dict.keys():
        syn = ', '.join(wanted_dict[key])
        print(f"{key} - {syn}")


count = int(input())
synonyms(count)