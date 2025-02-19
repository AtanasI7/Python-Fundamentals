lines = int(input())
sum = 0

for _ in range(1, lines + 1):
    char = input()
    sum += ord(char)

print(sum)