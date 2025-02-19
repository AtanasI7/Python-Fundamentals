def palindromes(num):
    for i in num:
        if i == list(reversed(i)):
            return True
        else:
            return False


data = list(map(int, input().split(', ')))
print(palindromes(data))
# print(list(reversed(data)))