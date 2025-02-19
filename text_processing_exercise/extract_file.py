def extraction():
    data = input().split('\\')
    needed_file = data[-1]
    needed_file = needed_file.split('.')
    print(f"File name: {needed_file[0]}")
    print(f"File extension: {needed_file[1]}")


extraction()