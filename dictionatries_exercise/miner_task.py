def miner_task(command):
    resourses = dict()

    while command != 'stop':
        quantity = int(input())

        if command not in resourses.keys():
            resourses[command] = quantity

        else:
            resourses[command] += quantity

        command = input()

    for i, m in resourses.keys():
        print(f"{i} -> {m}")


word = input()
miner_task(word)
