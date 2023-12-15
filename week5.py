# Inicialization

cart = ['999'] 

priceItem = [999]

price = 0

item = ''

option = 0



print('Welcome to the Shopping Cart Program!\n')

print('Please select one of the following: ')
print('1. Add item')
print('2. View cart')
print('3. Remove item')
print('4. Compute total')
print('5. Most high value of itens')
print('6. Quit')


while option == 0 or option > 6:
    option = int(input('Please enter an action: '))

    if option == 1:

      print('Welcome to the Shopping Cart Program!') 
      item = input('What item would you like to add?: ')
      
      if item.upper() != ' ':
          price = float(input(f"What is the price of '{item.capitalize()}'?: "))
          if item.upper() != 'END':
                cart.append(item)
                priceItem.append(price)
                option = 0
                print(f"'{item}' has been added to the cart.\n")

                print('Please select one of the following: ')
                print('1. Add item')
                print('2. View cart')
                print('3. Remove item')
                print('4. Compute total')
                print('5. Most high value of itens')
                print('6. Quit')
        
              
if option == 2:
    print('The contents of the shopping cart are: ')
    for i in range(1,len(cart)):
        print(f'{i}. {cart[i].capitalize()} - ${priceItem[i]}')

if option == 3:
    remove_item = int(input('Which item would you like to remove? '))
    if remove_item > len(cart):
        print('Sorry, that is not a valid item number.')
    else:
        cart.pop(remove_item)
        print('Item removed.')

if option == 4:
    priceItem.pop(0)
    sums = sum(priceItem)
    print(f'The total price of the items in the shopping cart is ${str(sums)}')

if option == 5:
    priceItem.pop(0)
    print(f'Most high value is: {str(max(priceItem))}')

if option == 6:
    print('Thank you. Goodbye.')
        

