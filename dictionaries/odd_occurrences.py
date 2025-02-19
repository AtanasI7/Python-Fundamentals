def occurrences(data):
    odd_times = dict()
    data = data.lower().split(' ')
    for i in data:
        if i not in odd_times:
            odd_times[i] = 1
        else:
            odd_times[i] += 1

    for j in odd_times.keys():
        if odd_times[j] % 2 != 0:
            print(j, end=' ')

info = input()
occurrences(info)