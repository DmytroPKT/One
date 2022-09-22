"""Задание максимум на 80 баллов:
Запросить у пользователя число N - ширина треугольника.
1)Вывести треугольник #1 с шириной N с помощью цикла while

*****
****
***
**
*"""

width = int(input('Enter №1 triangle width:  '))
symbol = "*"
while width > 0:
    print(width * symbol)
    width -= 1
print('No1 Triangle completed')
