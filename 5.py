proc = int(input('Введите число, равное выручке компании='))
costs = int(input('Введите число, равное издержкам компании='))
result = proc - costs
if result > 0:
    print('Прибыль')
    result = int(result)
    rent = result / proc
    print('Рентабельность=', rent)
    people = int(input('Введите число, равное количеству сотрудников='))
    proc_people = result / people
    print('Прибыль фирмы в расчёте на одного сотрудника=', proc_people)
else:
    print('Убыток')
