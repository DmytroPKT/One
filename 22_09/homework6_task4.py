"""Запросить у пользователя число N - ширина треугольника.
Задание со звездочкой:
4)Вывести треугольник #4 с шириной N с помощью цикла while

    *
   **
  ***
 ****
*****
"""
width = int(input('Enter №4 triangle width: '))
symbol = "*"
height = 0
while height < width:
    height += 1
    space_length = width - height
    print(" " * space_length + height * symbol)
print('No4 Triangle completed')
