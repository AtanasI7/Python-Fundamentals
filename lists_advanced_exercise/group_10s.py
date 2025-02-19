def group_of_tens(numbers):
    numbers = list(map(int, numbers))
    group_10 = [i for i in numbers if i < 10]
    group_20 = [i for i in numbers if 10 < i <= 20]
    group_30 = [i for i in numbers if 20 < i <= 30]
    group_40 = [i for i in numbers if 30 < i <= 40]
    group_50 = [i for i in numbers if 40 < i <= 50]
    print(f"Group of 10's: {group_10}")
    print(f"Group of 20's: {group_20}")
    print(f"Group of 30's: {group_30}")
    print(f"Group of 40's: {group_40}")
    print(f"Group of 50's: {group_50}")

#one way that isnt working

data = input().split(', ')
group_of_tens(data)