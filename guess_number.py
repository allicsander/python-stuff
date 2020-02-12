secret_number = 23
guess = None 
while guess != secret_number:
    guess = input('Enter a number: ')
    guess = int(guess) 
    if guess > secret_number:
        print('Too high.')
    if guess < secret_number:
        print('Too low.')
print('You got it!')