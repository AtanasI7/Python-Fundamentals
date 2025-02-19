def obtain_legendary_item(materials):
    legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
    required_quantity = 250

    quantities = {"shards": 0, "fragments": 0, "motes": 0}
    junk_items = {}

    while True:
        data = materials.split()
        for i in range(0, len(data), 2):
            quantity = int(data[i])
            material = data[i + 1].lower()

            if material in quantities:
                quantities[material] += quantity

                if quantities[material] >= required_quantity:
                    print(f"{legendary_items[material]} obtained!")
                    quantities[material] -= required_quantity
                    print_remaining_materials(quantities)
                    return

            else:
                if material not in junk_items:
                    junk_items[material] = 0
                junk_items[material] += quantity

    print_remaining_materials(quantities)


def print_remaining_materials(quantities):
    print("Remaining materials:")
    for material, quantity in sorted(quantities.items()):
        print(f"{material}: {quantity}")
    exit()


def main():
    input_lines = input("Enter the input lines: ").lower()
    obtain_legendary_item(input_lines)


if __name__ == "__main__":
    main()
