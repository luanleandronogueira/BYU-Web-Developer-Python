from datetime import datetime
import math

# def print_time(task_name):
#     print('task complete')
#     print(datetime.now())
#     print()
    
# first_name = 'Susan'
# print_time('Parameters')

# for x in range(0,10):
#     print(x)
# print_time('Parameters')
# # end def

# def show_message(message):
#     Message = message
#     print(Message)
#     print(Message.upper())
#     print(Message.lower())
#     return Message

# my_message = input('What is your message? ')

# my_message_function = show_message(my_message)

# square = int(input('What is the square area? '))

# square_function = square_area(square)

# print(f'The area of the square is {square_function}')

# Function do calculate the square area
def square_area(number):
    Number = number * number
    return Number

# Function do calculate the rectangle area
def rectangule_area(lenght, width):
    # Variables
    rectangule_calculate_area = lenght * width

    # return of the area
    return rectangule_calculate_area

# Function do calculate the Circle area
def circle_area(radius):
    # Variables
    circle_area = (radius ** 2) * 3.14
    # return of the area
    return circle_area

# input the numbers
# length_area = int(input('What is the lenght area? '))
# width_area = int(input('What is the width area? '))

# rectangule_function = rectangule_area(length_area, width_area)

# # show the result
# print(f'The area of the rectangule is {rectangule_function}')


# Raidus = int(input('What is the circle area? '))

# Raidus_function = circle_area(Raidus)

# print(f'The area of the rectangule is {Raidus_function}')


def display_numbers(x, y):
    return 10

x = 3
y = 4
x = display_numbers(x, y)

print(x)




    