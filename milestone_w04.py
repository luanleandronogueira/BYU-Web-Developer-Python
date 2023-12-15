#Inicialization of the variables

magic_word = 'lord'
magic = ''
guess = 0

# decision to play
decision = input('Do you like the World Puzzle? Yes/No: ')

# start to play 
if decision.upper() == 'YES':
    print("Let's fun with it!")

    print('Your hint is: ', end='')

    for under in magic_word:
        print(' _ ', end='')

    while magic_word != magic:
        magic = input('\nWhat is your guess? ')
        guess = guess + 1
        if len(magic) == len(magic_word):
            for position , letter in enumerate(magic):
                for position2, other_letter in enumerate(magic_word):
                    if letter.lower() == other_letter.lower():
                            if position == position2:
                                print(other_letter.upper(), end='')
                            else:
                                print(other_letter.lower(), end="")
                if letter not in magic_word:
                    print("_", end='')
            print() 
        if len(magic) != len(magic_word):
            print('Sorry, the guess must have the same number of letters as the secret word.')

    print('Congratulations! You guessed it!')
    print(f'It took you {guess} guesses') 

else:
    print("Sorry dude!")





        





    


