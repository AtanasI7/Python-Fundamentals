def to_do_list(info):
    work = ['' for i in range(1, 10 + 1)]

    while info != 'End':
        info = info.split('-')
        importance = int(info[0])
        job = info[1]

        work[importance] = job


        info = input()

    while '' in work:
        work.remove('')
    print(work)

data = input()
to_do_list(data)

