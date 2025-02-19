age = int(input())

if age > 15:
    if age <= 18:
        print('drink coke')

    elif 18 < age <= 21:
        print('drink beer')

    else:
        print('drink whisky')

else:
    print('drink toddy')