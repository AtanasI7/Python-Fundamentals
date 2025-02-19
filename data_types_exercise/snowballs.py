num_snowball = int(input())
best_snowball = 0
best_weight = 0
best_time = 0
best_quality = 0

for snowball in range(1, num_snowball + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    current_snowball = int((weight / time_needed) ** quality)
    if best_snowball < current_snowball:
        best_snowball = current_snowball
        best_weight = weight
        best_time = time_needed
        best_quality = quality

    else:
        pass

print(f"{best_weight} : {best_time} = {best_snowball} ({best_quality})")