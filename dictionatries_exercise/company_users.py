def company_names():
    data = input()
    companies = dict()
    condition = False

    while True:
        if data == 'End':
            condition = True
            break

        data = data.split(' -> ')
        company = data[0]
        employee_id = data[1]

        if company not in companies.keys():
            companies[company] = []

        if employee_id not in companies[company]:
            companies[company].append(employee_id)

        data = input()

    if condition:
        for key, value in companies.items():
            print(key)
            for i in value:
                print(f"-- {i}")


company_names()

