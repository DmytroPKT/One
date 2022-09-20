# First task
width = int(input('Enter №1 triangle width:  '))
symbol = "*"
while width > 0:
    print(width * symbol)
    width -= 1

# Second task
width = int(input('Enter №2 triangle width:  '))
symbol = "*"
length = 0
while length < width:
    length += 1
    print(length * symbol)

# Third task
width = int(input('Enter №3 triangle width: '))
symbol = "*"
space_length = 0
while width > 0:
    print(" " * space_length, width * symbol, sep="")
    width -= 1
    space_length += 1

# Fourth task
width = int(input('Enter №4 triangle width: '))
symbol = "*"
space_length = 0
length = 0
while length < width:
    length += 1
    space_length = width - length
    print(" " * space_length, length * symbol, sep="")