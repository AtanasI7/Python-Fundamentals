import re


def decipher(words):
    hidden = words.split(' ')
    new_list = list()
    for word in hidden:
        only_nums = re.findall(r'\d+|\D+', str)
        new_list.extend([s for s in only_nums if s.strip()])

    print(new_list)

code = input()
decipher(code)