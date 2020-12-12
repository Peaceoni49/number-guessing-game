import sys
import random
number = random.randint(1, 20)
print("Try to guess a number (between 1 and 20) in three guesses")

guess1 = int(input("\n Enter your 1st guess; "))
if guess1 == number:
    print("You guessed it right on the 1st try you must be psychic")
    sys.exit()
elif guess1 > number: 
    print("Oh No! your guess is too high try again")
else:
    print("Oh No! your guess is too low try again")

guess2 = int(input('\n Enter your 2nd guess; '))
if guess2 == number:
    print("You guessed it one right, GOOD JOB!")
    sys.exit()
elif guess2 > number:
    print("Oh No! your guess is too high try again")
else:
    print("Oh No! your guess is too low try again")

guess3 = int(input('\n Enter your 3rd guess; '))
if guess3 == number:
    print("You guessed it right. NICE ONE!")
    sys.exit()
elif guess3 > number:
    print("Oh No! your guess is too high try again")
else:
    print("Oh No! your guess is too low try again")