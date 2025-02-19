def capitals_yes(countries, capitals):
    countries = countries.split(', ')
    capitals = capitals.split(', ')

    result = zip(countries, capitals)
    for i in result:
        print(f"{i[0]} -> {i[1]}")

    # result = dict(zip(countries, capitals))
    # for key, value in result.items():
    #     print(f"{key} -> {value}")

data = input()
info = input()

capitals_yes(data, info)
