from datetime import datetime, timedelta

## week day
current_day = datetime.now()
taxes = 0.06
discount_rate = 0.1
day_of_week = current_day.weekday()


money = input("Please enter the subtotal: ")

while money == 0:
    money = input("Please enter the subtotal: ")
    
if float(money) >= 50:
    if day_of_week == 0 or day_of_week == 2:  
        discount = float(money) * discount_rate
        money = float(money) - float(discount) 
        tax = float(money) * taxes
        total = float(money) + tax
        print(f"Discount  tax amount: {discount:.2f}")
        print(f"Sales tax amount: {tax:.2f}")
        print(f"Total: {total:.2f}")

    else:
        tax = float(money) * taxes
        total = float(money) + tax
        print(f"Sales tax amount:{tax:.2f}")
        print(f"Total:{total:.2f}")

else:
    tax = float(money) * taxes
    total = float(money) + tax
    print(f"Sales tax amount:{tax:.2f}")
    print(f"Total:{total:.2f}")




##week_day1 = datetime.now()
# someday = timedelta(days=365)
# date = week_day1 + someday
# ##weekday2 = 
##week = week_day1.weekday()


# print(f"{str(week_day1)}")
# print(f"{str(date)}")
# print(f"{str(week)}")