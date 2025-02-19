events = input().split('|')
energy = 100
coins = 100
tester = list()
test_checker = 0

for i in events:
    i = i.split('-')
    event = i[0]
    number = int(i[1])

    if event == 'rest':
        if energy == 100:
            print(f"You gained 0 energy.")
            print(energy)



        elif energy + number <= 100:        #tuk moje da grumne
            print(f"You gained {number} energy.")

        tester.append('a')
        test_checker += 1
    if event == 'order':
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins")
            tester.append('a')
            test_checker += 1

        else:
            energy += 50
            print(f"You had to rest")

    if event != 'rest' and event != 'order':
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
            tester.append('a')
            test_checker += 1

        else:
            print(f"Closed! Cannot afford {event}.")
            break

if test_checker == len(tester):
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

