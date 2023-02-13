tickets = int(input('Введите количество билетов: '))
ages = []
for i in range(0, tickets):
    input_value = int(input(f'Введите возраст посетителя №{i + 1}:\n'))
    ages.append(input_value)
    def prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
    price_full = sum(map(prise, ages))
discount = int(price_full * 0.9)
if tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount, "руб.")
else:
    print('Стоимость всех билетов: ', price_full, "руб.")