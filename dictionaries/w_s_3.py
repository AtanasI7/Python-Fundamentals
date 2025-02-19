def synonyms(number):
    synonym_dict = dict()

    for i in range(number):
        word = input()
        synonym = input()

        if word not in synonym_dict.keys():
            synonym_dict[word] = list()
        synonym_dict[word].append(synonym)

    for j in synonym_dict.keys():
        print(f"{j} - {', '.join(synonym_dict[j])}")


count = int(input())
synonyms(count)