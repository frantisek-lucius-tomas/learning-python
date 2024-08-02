# this is a quess the number game.
import random

secretNumber = random.randint(1, 20)
print('i am thinking of a number between 1 and 20')

# ask the plater to guess 6 times
for guessesTaken in range(1, 7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('your number is to low')
    elif guess > secretNumber:
        print('your number is to high')
    else:
        break # this condition is the correct guess

if guess == secretNumber:
    print('good job, you guesses my number in ' + str(guessesTaken) + ' guesses')
else: 
    print('nope, the number I was thinking of was ' + str(secretNumber))
