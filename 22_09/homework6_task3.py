"""Запросить у пользователя число N - ширина треугольника.
Задание со звездочкой:
3)Вывести треугольник #3 с шириной N с помощью цикла while

*****
 ****
  ***
   **
    *"""

width = int(input('Enter №3 triangle width: '))
symbol = "*"
space_length = 0
while width > 0:
    print(" " * space_length + width * symbol)
    width -= 1
    space_length += 1
print('No3 Triangle completed')
