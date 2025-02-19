def between(a, b):
    for i in range(ord(a) + 1, ord(b)):
        words.append(chr(i))
    return words

first_word = input()
second_word = input()
words = list()

result = between(first_word, second_word)
print(' '.join(result))