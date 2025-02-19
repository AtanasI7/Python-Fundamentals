def printing(special_mat, trash_mat, special_item):
    print(f"{special_item} obtained!")
    for key, value in special_mat.items():
        print(f"{key}: {value}")
    for key, value in trash_mat.items():
        print(f"{key}: {value}")


def farming():
    special_mat_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
    trash_mat_dict = {}
    condition = False

    while True:
        data = input().lower().split(' ')

        for quantity, matertial in zip(data[0::2], data[1::2]):
            quantity = int(quantity)

            if matertial in special_mat_dict.keys():
                special_mat_dict[matertial] += quantity
                if special_mat_dict[matertial] >= 250:
                    special_mat_dict[matertial] -= 250
                    special_item = ''
                    if matertial == 'shards':
                        special_item = 'Shadowmourne'
                    elif matertial == 'fragments':
                        special_item = 'Valanyr'
                    elif matertial == 'motes':
                        special_item = 'Dragonwrath'
                    printing(special_mat_dict, trash_mat_dict, special_item)
                    condition = True
                    break

            elif matertial not in trash_mat_dict.keys():
                trash_mat_dict[matertial] = quantity

            else:
                trash_mat_dict[matertial] += quantity

        if condition:
            break

farming()



