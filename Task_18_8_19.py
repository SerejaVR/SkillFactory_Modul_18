tickets = int(input('введите количество билетов '))
summa = 0
for ticket in range(tickets):
    age = int(input('введите возраст '))

    if age < 18:
        summa = summa + 0
        print('стоимость билетов', summa, 'руб')

    elif age >= 18 and age < 25:
        summa = summa + 990
        print('стоимость билетов', summa, 'руб')

    elif age >= 25:
        summa = summa + 1390
        print('стоимость билетов', summa, 'руб')

if tickets > 3:
    summa = summa * 0.9
    print('стоимость со скидкой', summa, 'руб')