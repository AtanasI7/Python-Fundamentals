def anonymous_threat(words):
    receiving_command = input()
    while receiving_command != '3:1':
        receiving_command = receiving_command.split(' ')
        command = receiving_command[0]

        if command == 'merge':
            start_index = receiving_command[1]
            end_index = receiving_command[2]
            if start_index.index() in len(words):
                pass




        elif command == 'divide':
            pass

data = input().split(' ')
anonymous_threat(data)

