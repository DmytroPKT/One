"""Запросить у пользователя число N - ширина треугольника.

Задание максимум на 80 баллов:

Вывести треугольник #1 с шириной N с помощью цикла while
Вывести треугольник #2 с шириной N с помощью цикла while
Задание со звездочкой:

Вывести треугольник #3 с шириной N с помощью цикла while
Вывести треугольник #4 с шириной N с помощью цикла while
1)
*****
****
***
**
*
2)
*
**
***
****
*****
3)
*****
 ****
  ***
   **
    *
4)
    *
   **
  ***
 ****
*****
"""

# First task
width = int(input('Enter №1 triangle width:  '))
symbol = "*"
while width > 0:
    print(width * symbol)
    width -= 1
print('No1 Triangle completed')
exit()

# Second task
width = int(input('Enter №2 triangle width:  '))
symbol = "*"
height = 0
while height < width:
    height += 1
    print(height * symbol)
print('No2 Triangle completed')
exit()

# Third task
width = int(input('Enter №3 triangle width: '))
symbol = "*"
space_length = 0
while width > 0:
    print(" " * space_length + width * symbol)
    width -= 1
    space_length += 1
print('No3 Triangle completed')
exit()

# Fourth task
width = int(input('Enter №4 triangle width: '))
symbol = "*"
height = 0
while height < width:
    height += 1
    space_length = width - height
    print(" " * space_length + height * symbol)
print('No4 Triangle completed')
exit()
