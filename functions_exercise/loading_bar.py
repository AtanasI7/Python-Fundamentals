def loading_bar(current_percent):
    percentage = (current_percent // 10)
    percentage_symbol = '%' * percentage
    dots = 10 - percentage
    dots_symbol = '.' * dots
    if current_percent < 100:
        print(f"{current_percent}% [{percentage_symbol}{dots_symbol}]")

    if current_percent == 100:
        print(f"{current_percent}% Complete!")
        print('[%%%%%%%%%%]')
    else:
        print('Still loading...')


percent = int(input())
loading_bar(percent)