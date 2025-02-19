leters = int(input())

for i in range(0, leters):
    for k in range(0, leters):
        for j in range(0, leters):
            print(f"{chr(97+ i)}{chr(97 + k)}{chr(97 + j)}")