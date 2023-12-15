# first_number = int(input('What is the first number? '))
# second_number = int(input('What is the second number? '))

# if first_number > second_number:
#     print('The first number is greater')
#     print('The numbers are not equal')
#     print('The second number is not greater')

# elif first_number < second_number:
#     print('The first number is not greater')
#     print('The numbers are not equal')
#     print('The second number is greater')

# else:
#     print('The first number is not greater')
#     print('The numbers are equal')
#     print('The second number is not greater ')

# favorite_animal = 'bear'
# animal = str(input('\nWhat is your favorite animal? '))

# if animal.lower() == favorite_animal:
#     print("That's my favorite animal too!")

# else:
#     print('That one is not my favorite.')

# Loans conditions

large_loan = int(input('How large is the loan? '))

credit_hist = int(input('How good is your credit history? '))

income = int(input('How high is your income? '))

large_payment = int(input('How large is your down payment? '))

liberation = False

if large_loan >= 5:
   if credit_hist >= 7 and income >= 7:
        liberation = True
elif credit_hist >= 7 or income >= 7:
        if large_payment >= 5:
            liberation = True
        else:
            liberation = False
   
else:
    if large_loan < 5:
        if large_loan < 4:
            liberation = False
        elif large_loan == 4:
            if income >= 7 or large_payment >= 7:
                liberation = True
            elif income >= 4 and large_payment >= 4:
                liberation = True
        else:
            liberation = False

if liberation:
    print('Yes') 
else:
    print('No!')




 
            





   



