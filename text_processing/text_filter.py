def replacement():
    banned_words = input().split(', ')
    text = input()

    while True:
        for i in banned_words:
            if i in text:
                text = text.replace(i, "*" * len(i))

        print(text)
        break



replacement()

