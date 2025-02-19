command = input()
coffee = 0


while command != 'END':
    if command.isupper():
        if command == 'CODING':
            coffee += 2
        elif command == 'CAT' or command == 'DOG':
            coffee += 2
        elif command == 'MOVIE':
            coffee += 2

    elif command.islower():
        if command == 'coding':
            coffee += 1
        elif command == 'cat' or command == 'dog':
            coffee += 1
        elif command == 'movie':
            coffee += 1

    command = input()

if coffee > 5:
    print('You need extra sleep')

else:
    print(coffee)