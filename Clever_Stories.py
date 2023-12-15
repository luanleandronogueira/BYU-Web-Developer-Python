# inicial information

print('\nPlease enter the following:\n') 

# Input of elements of the story

adjective = input('Adjective: ')
animal = input('Animal: ')
verb1 = input('Verb 1: ')
exclamation = input('Exclamation: ')
verb2 = input('Verb 2: ')
verb3 = input('Verb 3: ')

# extra variables in the story
reaction = input('Reaction: ')
adjective2 = input('Adjetive 2: ')



# The story

print('\nYour story is:\n')

print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {verb2} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb3}')
print('right in front of my family.\n')

# aditional details of story
print(f'After this, all my family started to laugh about me. And I {reaction},')
print(f'things like this always make me feel {adjective2}!\n')

