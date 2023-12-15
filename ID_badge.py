
print("Please enter the following information:")

# receive information
last_name = input("Whats your last name? ")
name = input('Whats your name? ')
job_title = input('Describe your job title: ')
ID_number = input('ID Number: ')
email = input('Email Address: ')
phone = input('Phone number: ') 

# Card with information
print('\nThe ID Card is: ')
print('----------------------------------------')
print(f'{last_name.upper()}, {name.capitalize()}')
print(f'{job_title.title()}')
print(f'ID: {ID_number} \n')
print(f'{email.lower()}')
print(f'{phone}')
print('----------------------------------------')