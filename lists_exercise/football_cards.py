team_A = 11
team_B = 11
cards = list(input().split(' '))

for i in set(cards):
    if 'A' in i:
        team_A -= 1

        if team_A < 7 or team_B < 7:
            break

    if 'B' in i:
        team_B -= 1

        if team_A < 7 or team_B < 7:
            break

print(f"Team A - {team_A}; Team B - {team_B}")
if team_A < 7 or team_B < 7:
    print(f"Game was terminated")