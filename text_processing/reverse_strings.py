def rev_word():
    word = input()
    rever_dict = dict()

    while word != 'end':
        reversed_word = ''.join(list(reversed(word)))
        # rever_dict[word] = reversed_word
        print(f"{word} = {reversed_word}")

        word = input()

    # for key, value in rever_dict.items():
    #     print(f"{key} = {value}")


rev_word()
