# course = open('couses.txt')

#  for i in course:
#     print(i)

# with open('Tema-das-aulas.txt') as files:
    
#     for i in files:
#         print(i)

#     files.close()


# colors = '            Luan Leandro Nogueira                     '


# separadas_colors = colors.strip()
# colors_separadas = colors.split()

# print(colors)

# print(f'--------------{separadas_colors}---------------')

# for cor in colors_separadas:
#     print(cor)

# with open('couses.txt') as files:
#     for file in files:
#         line_file = file.strip()

#         parts = file.split(',')

#         name_country = parts[0]
#         price = parts[1]


#         print(f'Country: {name_country} - Numbers: {price}')

# with open('real.txt') as ponto:
#     for line in ponto:
#         parts = line.split()

# with open('books.txt') as book_of_mormon:
#     for book in book_of_mormon:
#         line = book.strip()
#         print(line)

# numbers = [42, 25, 18, 83, 23, 85, 38, 2]

# numero_maior = numbers[0]

# for number in numbers:
#     if number > numero_maior:
#         numero_maior = number

# print(numero_maior)


# shopping_cart = [
#     ["Chips", 2.99],
#     ["Bread", 2.50],
#     ["Milk", 3.19],
#     ["Ice Cream", 6.99],
#     ["Cheese", 5.99],
#     ["Candy bar", 0.99]
# ]

# max_price = -1

# for item in shopping_cart:
#     price = item[1]
#     if price > max_price:
#         max_price = price

# print(max_price)

# max_price = -1
# max_product = "" # It doesn't matter what you set this to, it just needs to be declared

# for item in shopping_cart:
#     product_name = item[0] # Product name is the first part
#     price = item[1] 

#     if price > max_price:
#         # This is the new max
#         max_price = price

#         # Also save this product name as the max product
#         max_product = product_name

# print(f"The maximum price is: {max_price}")
# print(f"The product with the maximum price is: {max_product}")

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

min_age = 9999

nameAge = ''

for person in people:

    parts = person.split(' ')

    name = parts[0]
    age = int(parts[1])

    if age < min_age:
        min_age = age

        nameAge = name

print(nameAge , min_age)

line = "     text"

line.strip()

print(line)
