
print("Please enter the following information:")

# commands for information
last_name = input("Whats your last name? ")
name = input('Whats your name? ')
job_title = input('Describe your job title: ')
ID_number = input('ID Number: ')
email = input('Email Address: ')
phone = input('Phone number: ') 
hairColor = input('Hair Color: ')
month = input('Starting Month:: ')
eyesColor = input('Eye Color: ')
training = input('Completed additional training?: ')

# card with information
print('\nThe ID Card is: ')
print('----------------------------------------')
print(f'{last_name.upper()}, {name.capitalize()}')
print(f'{job_title.title()}')
print(f'ID: {ID_number} \n')
print(f'{email.lower()}')
print(f'{phone} \n')

# additional information
print(f'Hair: {hairColor.capitalize()}                    Eyes: {eyesColor.capitalize()}')
print(f'Month: {month.capitalize()}               Training: {training.capitalize()}')
print('----------------------------------------')