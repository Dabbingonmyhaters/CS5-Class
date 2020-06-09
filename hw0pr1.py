#Cristian Rosales-Cardenas
#CS5
#Day 0 (06/08/20)
#Prof Dodds

from math import *
print('Zero is ', 4+4-4-4)
print('One is ', 44/44)
print('Twelve is',sqrt(4)+(4)+(4)+sqrt(4))
print('Three is', (factorial(4)+factorial(4))/(4*4))
print('Four is', (factorial(4)-4-4)/4)
print('Sixteen is', 4*4/4*4)
print('Eighteen is', (factorial(4)+factorial(4)+factorial(4))/(4))
print('Fifteen is', 44/4+4)
print('Ten is', 44/(4+0.4))
print('Eleven is', 44/(sqrt(4)+sqrt(4)))
print('Eight is', 4**(4/4)+4)
print('Fourteen is',(4)+(4)+(4)+sqrt(4))
print('Eight is ', (factorial(4)-(4*4)))
print('Two is', (factorial(4)-(4*4))/4)
print('Twenty is', (factorial(4)-(4*4))/.4)
print('Six is', (factorial(4)+factorial(4))/(4+4))


# coding: utf-8
#
# hw0pr2a.py
#

import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    user = input("Choose your weapon: ")
    comp = random.choice(['rock','paper','scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if user == 'rock':
        print('Ha! I really chose paper--I WIN!')

    print("Better luck next time...")
