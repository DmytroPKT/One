"""
Задание 2:

Вывести таблицу умножения на 3 с помощью цикла for.

На экране должно быть:

3*1=3

3*2=6

3*3=9

3*4=12

3*5=15

3*6=18

3*7=21

3*8=24

3*9=27

3*10=30
"""

value = 3

for first_digit in range(1, 11):
    result = first_digit * value
    print(f'{first_digit} * {value} = {result}')

exit()
