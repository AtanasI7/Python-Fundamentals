lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
money = 0
broken_shield_counter = 0


for match in range(1, lost_fights + 1):
    if match % 2 == 0:
        money += helmet_price

    if match % 3 == 0:
        money += sword_price

    if match % 6 == 0:
        broken_shield_counter += 1
        money += shield_price

    if broken_shield_counter == 2:
        broken_shield_counter = 0
        money += armor_price

print(f"Gladiator expenses: {money:.2f} aureus")
