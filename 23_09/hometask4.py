"""
Задания со звездочкой:

Задание 4:

Вывести на экран таблицу умножения от 1 до 10 с помощью двух циклов for.
"""
for first_digit in range(1, 11):
    print('\n')
    for second_digit in range(1, 11):
        result = first_digit * second_digit
        print(f'{first_digit} * {second_digit} = {result}')
exit()
