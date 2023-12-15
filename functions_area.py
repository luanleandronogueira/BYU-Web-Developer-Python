# Function do calculate the square area
def square_area(number):
    # Variables
    Number = number * number
    # return of the area
    return Number

# Function do calculate the rectangle area
def rectangule_area(lenght, width):
    # Variables
    rectangule_calculate_area = lenght * width

    # return of the area
    return rectangule_calculate_area

# Function do calculate the circle area
def circle_area(radius):
    # Variables
    circle_area = (radius ** 2) * 3.14
    # return of the area
    return circle_area


choose = ''

while choose.lower() != 'quit':
    choose = input("What shape do you have? ")

    if choose.lower() == 'circle':

        Raidus = int(input('What is the circle area? '))

        Raidus_function = circle_area(Raidus)

        print(f'The area of the rectangule is {Raidus_function}')
    
    if choose.lower() == 'rectangule':

        # input the numbers
        length_area = int(input('What is the lenght area? '))
        width_area = int(input('What is the width area? '))

        rectangule_function = rectangule_area(length_area, width_area)

        # show the result
        print(f'The area of the rectangule is {rectangule_function}')

    
    if choose.lower() == 'square':
        
        square = int(input('What is the square area? '))

        square_function = square_area(square)

        print(f'The area of the square is {square_function}')

print('Thank You!')
        



