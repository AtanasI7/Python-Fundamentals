num_one = int(input())
num_two = int(input())
num_three = int(input())

if num_one > num_two and num_one > num_three:
    print(num_one)

if num_two > num_one and num_two > num_three:
    print(num_two)

if num_three > num_one and num_three > num_two:
    print(num_three)