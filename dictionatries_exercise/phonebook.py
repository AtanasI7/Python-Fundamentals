def phonebook_func(data):
    phonebook = dict()

    while '-' in data:
        data = data.split('-')
        name = data[0]
        phone_number = data[1]

        if name not in phonebook.keys():
            phonebook[name] = phone_number
        else:
            phonebook[name] = phone_number

        data = input()

    number = int(data)

    for n in range(number):
        contact = input()
        if contact in phonebook.keys():
            print(f"{contact} -> {phonebook[contact]}")

        else:
            print(f"Contact {contact} does not exist.")


info = input()
phonebook_func(info)
