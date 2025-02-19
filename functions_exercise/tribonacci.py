def tribonacci(num):
    tribonacci_list = list()
    for n in range(1, num + 1):
        tribonacci_list.append(n)

        if len(tribonacci_list) > 3:
            tribonacci_list.pop(0)


        print(sum(tribonacci_list), end=' ')


number = int(input())

tribonacci(number)