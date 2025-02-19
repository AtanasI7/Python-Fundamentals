def palindromes(num):
    for i in num:
        reversed_i = ''.join(list(reversed(i)))
        if i == reversed_i:
            print(True)
        else:
            print(False)


data = input().split(', ')
palindromes(data)

# number = 5123
# new_num = list(reversed(str(number)))
# print(''.join(new_num))
