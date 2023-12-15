# books = []

# books.append(input('Insert a book: '))
# books.append("1 Nephi")
# books.append("2 Nephi")
# books.append("Jacob")
# books.append("Enos")


# for book in books:
#     print(book)

# itens = [1, 3, 6]

# zero = 0 

# for item in itens:
#     zero += item
#     print(zero)

# print()
# print('Resultad é: ' + str(zero))

# friends = []

# names = ''

# close = 'end'

# while names != close:
#     names = input('Your friends are: ')
#     if names != close:
#         friends.append(names)

# print(f'\nYour friends are: ')

# for friend in friends:
#     print(friend)


# preco = float(input('Preço da passagem: '))

# quant_familia = int(input('Quantidade de membros incluindo você: '))

# a_pagar = preco * quant_familia

# membros = []

# membro = ''

# while membro != 'fim':
#     membro = input('Nome do membro da Caravana: ')
#     if membro != 'fim':
#         membros.append(membro)

# for nome in membros:
#     print(f'{nome} R$ {str(preco)}')

# print(f'Total à pagar: R$ {str(a_pagar)}')


# number_books = ['book of mormon', 'bible', 'pearl of great price', 'D&C']

# book = len(number_books)

# print(book)

# for i in range(len(number_books)):
#     number_books[i]
#     print(f'{i} {number_books}')

# friends = []
# numbers = []

# name = ''

# num = ''

# while name != 'end' and num != 'end':
#     name = input("Whats the name of the friend: ")
#     num = str(input("Whats the cel of the friend: "))
#     if name != 'end' and num != 'end':
#         friends.append(name)
#         numbers.append(num)

# for i in range(len(friends)):
#     name = friends[i]
#     num = numbers[i]

#     print(name.capitalize() , num)

itens = []

item = ''

while item != 'end':
    item = input('Please enter the items of the shopping list (type: quit to finish): ')
    if item != 'end':
        itens.append(item)

print('\nThe shopping list is: ') 

for i in range(len(itens)):
    
    print(f'{itens[i].capitalize()}')

print('\nThe shopping list with indexes is: ') 

for i in range(len(itens)):
    print(f'{i}. {itens[i].capitalize()}')

changes = int(input('\nWhich item would you like to change? ' ))
new_item = input('What is the new item? ')

itens.pop(changes)
itens.append(new_item)

print('\nThe shopping list with indexes is: ')

for i in range(len(itens)):
   print(f'{i}. {itens[i].capitalize()}') 














