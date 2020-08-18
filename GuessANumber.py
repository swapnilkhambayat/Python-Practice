import random as ra
count = 0
guess = 0
nm = ra.randint(1,10)
print('Guess a number between 1 and 10')

while nm != guess:
    count += 1
    guess = input(f'Enter guess #{count}:')  
    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
        continue

    if guess < nm:
        print('Your guess is too low, try again!')
    elif guess > nm:
        print('Your guess is too high, try again!')
    
else:
    print(f'You guessed it in {count} tries!')