def testing(words):
    for i in words:
        if len(i) % 3 == 0:
            print(i)


data = input().split(' ')
testing(data)
