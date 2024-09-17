## Import
import math 
from datetime import datetime

## prices
value1 = '$100.00'
value2 = '$250.00'
value3 = '$350.00'

## receiving the values
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

## get the local time
current_date_and_time = datetime.now()

## calculate with the formula 
volume = math.pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter) / 10000000000

## conditions of price and size
if volume < 30:
    ## print the result o liters
    print(f"The approximate volume is {volume:.2f} liters")
    print(f"The price of this tire is {value1}")
    buy = input('Do you want to buy this tire? YES/NO: ').upper()
    if buy == 'YES':
        phone = input('Insert your phone number: ')
        # save the informations in volumes.txt
        with open("volumes.txt", mode="a") as file:
            file.write(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}, {value1}, {phone}\n\n")
            
elif volume >= 30 and volume <= 49:
    ## print the result o liters
    print(f"The approximate volume is {volume:.2f} liters")
    print(f"The price of this tire is {value2}")
    buy = input('Do you want to buy this tire? YES/NO: ').upper()
    if buy == 'YES':
        phone = input('Insert your phone number: ')
        # save the informations in volumes.txt
        with open("volumes.txt", mode="a") as file:
            file.write(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}, {value2}, {phone}\n\n")
            
else:
    ## print the result o liters
    print(f"The approximate volume is {volume:.2f} liters")
    print(f"The price of this tire is {value3}")
    buy = input('Do you want to buy this tire? YES/NO: ').upper()
    if buy == 'YES':
        phone = input('Insert your phone number: ')
        # save the informations in volumes.txt
        with open("volumes.txt", mode="a") as file:
            file.write(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}, {value3}, {phone}\n\n")            
    

## end of the program
print(f"Thank you!! Bye")


