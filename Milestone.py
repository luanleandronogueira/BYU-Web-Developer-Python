# food's price 
child_food = float(input("What is the price of a child's meal?: "))
adult_food = float(input("What is the price of an adult's meal?: "))

# how many people are
qt_child = float(input("How many children are there?: "))
qt_adult = float(input("How many adults are there?: "))


# Taxes
tax = float(input("What is the sales tax rate?: "))

# fixed price drink
drink = 1.99

# drink
qt_drink = float(input('Do you want any drink? (price is $1.99) If no, insert 0: '))
 
resultDrink = drink * qt_drink

# formulas
price_food_children = child_food * qt_child
price_food_adult = adult_food * qt_adult

subtotal = price_food_adult + price_food_children + resultDrink

# tax fomula
taxResult =  (tax * subtotal) / 100

# total 
total = subtotal + taxResult 

print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${taxResult:.2f}")
print(f"Total: ${total:.2f}\n")

payment = float(input('What is the payment amount? '))
# change formula
change = payment - total
print(f'Change: ${change:.2f}\n')
