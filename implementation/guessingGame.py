import math
import random

random = 6

guess = int(input('enter your guess: '))

i=1
while i<3:
    if guess ==random:
        print('correct')
        break
    elif guess > random:
        print('too high')
        guess = int(input('enter your guess: '))
        i+=1
    else:
        print('too low')
        guess = int(input('enter your guess: '))
        i+=1
print('              ')
print('try again')
print('              ')