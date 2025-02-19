def data_types(word, num):
    if word == 'int':
        result = int(num) * 2
        return result
    if word == 'real':
        result = num * 1.5
        return f"{result:.2f}"
    if word == 'string':
        return f"${num}$"


data = input()
if data == 'int' or data == 'real':
    number = float(input())
else:
    number = input()

print(data_types(data, number))