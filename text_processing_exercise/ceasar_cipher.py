def cipher():
    text = input()
    new_text = ''

    for i in text:
        a = ord(i) + 3
        new_text += chr(a)

    print(new_text)


cipher()