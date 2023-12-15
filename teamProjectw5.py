# numbers = []

# num = ''

# guess = 0
# sum = 0


# print('Enter a list of numbers, type 0 when finished.')

# while num != 0:
#     num = int(input('Enter number: '))
    
#     if num != 0:
#         numbers.append(num)
#         guess = guess + 1

# for i in numbers:
#     sum += i
    
# average = sum / guess


# print(f'The sum is: {sum}')
# print(f'The average is: {average}')
# print(f'The largest number is: ' + str(max(numbers)))


numbers = []

num = ''

guess = 0

sum = 0

print('Enter a list of numbers, type 0 when finished.')

while num != 0:
    num = int(input('Enter number: '))
    if num != 0:
        numbers.append(num)
        guess += 1

for i in numbers:
    sum += i

average = sum / guess

smallNumber = 9999999999

print(f'The sum is: {str(sum)}')
print(f'The average is: {str(average)}')
print(f'The largest number is: {str(max(numbers))}')

for i in numbers:
    if i > 0 and i < smallNumber:
        smallNumber = i

print(f'The smallest positive number is: {smallNumber}')

print("The sorted list is: ")

numList = sorted(numbers)

for i in numList:
    print(i)