def palindrome(data, important):
    data = data.split(' ')
    final_list = list()
    for i in data:
        rev_i = reversed(i)
        rev_i = ''.join(rev_i)
        if i == rev_i:
            final_list.append(i)

    important_count = final_list.count(important)
    print(final_list)
    print(f"Found palindrome {important_count} times")


info = input()
important_word = input()
palindrome(info, important_word)

