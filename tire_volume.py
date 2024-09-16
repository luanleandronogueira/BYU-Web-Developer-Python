## Import
import math 
from datetime import datetime

## receiving the values
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

## get the local time
current_date_and_time = datetime.now()

## calculate with the formula 
volume = math.pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter) / 10000000000

# save the informations in volumes.txt
with open("volumes.txt", mode="a") as file:
    file.write(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}\n\n")

## print the result o liters
print(f"The approximate volume is {volume:.2f} liters")


