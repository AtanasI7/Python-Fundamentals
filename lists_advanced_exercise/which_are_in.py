def which_are_in(needed_words, whole_text):
    special_list = list()
    for i in needed_words:
        for o in whole_text:
            if i in o:
                if i in special_list:
                    continue
                special_list.append(i)
    print(special_list)


data1 = input().split(', ')
data2 = input().split(', ')
which_are_in(data1, data2)