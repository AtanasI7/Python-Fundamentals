def softuni_parking_lot():
    number = int(input())
    parking_lot = dict()

    for i in range(1, number + 1):
        data = input().split(' ')
        command = data[0]
        username = data[1]

        if command == 'register':
            plate_number = data[2]

            if username not in parking_lot.keys():
                parking_lot[username] = plate_number
                print(f"{username} registered {plate_number} successfully")

            elif username in parking_lot.keys():
                print(f"ERROR: already registered with plate number {plate_number}")

        elif command == 'unregister':
            if username in parking_lot.keys():
                print(f"{username} unregistered successfully")
                parking_lot.pop(username)
            else:
                print(f"ERROR: user {username} not found")

    for key, value in parking_lot.items():
        print(f"{key} => {value}")


softuni_parking_lot()


