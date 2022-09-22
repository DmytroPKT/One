"""Задание максимум на 80 баллов:
Запросить у пользователя число N - ширина треугольника.
2)Вывести треугольник #2 с шириной N с помощью цикла while

*
**
***
****
*****"""

width = int(input('Enter №2 triangle width:  '))
symbol = "*"
height = 0
while height < width:
    height += 1
    print(height * symbol)
print('No2 Triangle completed')
