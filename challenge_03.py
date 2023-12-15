# grade = int(input('Insert your grade: '))

# if grade >= 90:
#     letter = "A"
# elif grade >= 80:
#     letter = 'B'
# elif grade >= 70:
#     letter = "C"
# elif grade >= 60:
#     letter = "D"
# else:
#     letter = "F"

# sign = ""

# result = grade % 10

# if result <= 3:
#    sign = "-"
#    print(f'{letter} ' + f'{sign}')
# if result >= 7:
#     sign = "+"
#     print(f'{letter} ' + f'{sign}')


# Insert the grade
grade = int(input('Insert your grade: '))

# how to calculate the grade A, A+ and A-
if grade >= 90 and grade <= 100:
    if grade >= 90 and grade <= 93:
        print('Congrats you got an "A - "')
    elif grade >= 94 and grade <= 97:
        print('Congrats you got an "A + "')
    else:
        print('Congrats you got an "A"')



# how to calculate the grade B, B+ and B-
if grade >= 80 and grade <= 89:
    if grade >= 80 and grade <= 83:
        print('Congrats you got an "B - "')
    elif grade >= 84 and grade <= 87:
        print('Congrats you got an "B + "')
    else:
        print('Congrats you got an "B"')

#how to calculate the grade C, C+ and C-
if grade >=70 and grade <= 79:
    if grade >=70 and grade <= 73:
        print('Congrats you got an "C - "')
    elif grade >= 74 and grade <= 77:
        print('Congrats you got an "C + "')
    else:
        print('Congrats you got an "C"')

# how to calculate the grade D, D+ and D-
if grade >= 60 and grade <= 69:
    if grade >= 60 and grade <= 63:
        print('Congrats you got an "D - "')
    elif grade >= 64 and grade <= 67:
        print('Congrats you got an "D + "')
    else:
        print('Congrats you got an "D"')

# how to calculate the grade A, A+ and A-
if grade <= 59:
    print('You got a "F"')
