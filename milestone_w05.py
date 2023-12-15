# Inicialization

cart = ['999'] 

priceItem = [999]

price = 0

item = ''

print('Welcome to the Shopping Cart Program!\n')

# here starts the loop
while item.upper() != 'END':
      item = input('What item would you like to add?: ')
      if item.upper() != 'END':
         price = input(f"What is the price of '{item}'?: ")
      if item.upper() != 'END':
         cart.append(item)
         priceItem.append(price)
         print(f"'{item}' has been added to the cart.")

print('\nThe contents of the shopping cart are:')

# here print the list
for i in range(1,len(cart)):
    print(i, cart[i], priceItem[i])


removePop = int(input('\nWhich item would you like to remove?: '))

cart.pop(removePop)
priceItem.pop(removePop)
print('Item removed.')

for i in range(1,len(cart)):
    print(i, cart[i], priceItem[i])



