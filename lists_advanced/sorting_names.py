def sorting_names(data):
    sorted_names = sorted(data)
    sorted_names = sorted(sorted_names, key=lambda name: -len(name))
    print(sorted_names)

    another_sorted_names = sorted(names, key=lambda name: (-len(name), name))
    print(another_sorted_names)

names = input().split(', ')
sorting_names(names)