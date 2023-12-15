# the inicialization of the secret and guess word
secret_word = 'Monson'
guesses = 0

print('Welcome to the word guessing game!')

# insert the first value
guess = input('\nWhat is your guess? ')

# here starts the loop
while guess.lower() != secret_word.lower():
        guess = input('What is your guess? ')
        guesses = guesses + 1

if guess.lower() == secret_word.lower():
    guesses = guesses + 1
    print('Congratulations! You guessed it!')
    print(f'It took you {guesses} guesses')
# the end of the game