"""
Задание 3:

Программа с помощью библиотеки random генерирует случайное число от 1 до 10, задача пользователя угадать это число за 3
попытки. В случае если пользователь указал больше загаданного числа, то нужно вывести "Бери меньше" и наоборот.

На экране должно быть:

Попытка #1: <ввод тут>

Бери меньше

Попытка #2: <ввод тут>

Бери больше

Попытка #3: <ввод тут>

Ты угадал!"""

import random

random_number = random.randint(1, 10)
attempts = 1

input_number = int(input('''Welcome to the annual lottery!
You have to guess a random number from 1 to 10.
You only have 3 attempts!
Attempt No''' + str(attempts) + '. Enter a number: '))

for attempts in range(2, 4):

    if input_number > random_number:
        print('Take less')
        input_number = int(input('Attempt No' + str(attempts) + '. Enter a number: '))

    elif input_number < random_number:
        print('Take more')
        input_number = int(input('Attempt No' + str(attempts) + '. Enter a number: '))

if input_number == random_number:
    print('YOU WON!!!!!!!!!!!!!!!111111111')

else:
    print('YOU LOSE!!!!!!!!!!!!1111111')
