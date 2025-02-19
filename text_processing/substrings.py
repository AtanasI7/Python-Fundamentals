def substrings():
    special_word = input()
    data = input()

    while special_word in data:
        data = data.replace(special_word, '')

    print(data)


substrings()

