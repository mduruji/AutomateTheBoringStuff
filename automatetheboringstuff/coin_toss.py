"""
Debugging Coin Toss
The following program is meant to be a simple coin toss guessing game.
The player gets two guesses (it’s an easy game). However, the program has several bugs in it.
Run through
"""

import random
guess = ''
sides = ('tails', 'heads',)
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = sides[toss]
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
