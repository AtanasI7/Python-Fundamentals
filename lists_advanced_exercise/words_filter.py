def even_word(words):
    new_string = [i for i in words if len(i) % 2 == 0]
    print('\n'.join(new_string))


data = input().split(' ')
even_word(data)