def classification(current_data):
    current_data = list(map(int, current_data))
    positive = [str(i) for i in current_data if i >= 0]
    negative = [str(i) for i in current_data if i < 0]
    even = [str(i) for i in current_data if i % 2 == 0]
    odd = [str(i) for i in current_data if i % 2 != 0]

    # positive = [str(i) for i in positive]
    # negative = [str(i) for i in negative]
    # even = [str(i) for i in even]
    # odd = [str(i) for i in odd]

    print(f"Positive: {', '.join(positive)}")
    print(f"Negative: {', '.join(negative)}")
    print(f"Even: {', '.join(even)}")
    print(f"Odd: {', '.join(odd)}")


data = input().split(', ')
classification(data)