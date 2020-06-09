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
from time import sleep #creates delays in functions to make the layout more comfortable to look at 

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    i = random.choice(['Hey look a flying seal', 'Look it'+"'"+'s someone asleep at the wheel', 'Hey is that your long-lost brother?'])
    #Just a little extra list I wanted to add to make the game more enterntaining
    comp = random.choice(['rock','paper','scissors'])
    #Creating a small list to choose from randomly

    print('This one' + "'" + 's for all the marbles')
    user = input("Choose your weapon: ")
    if not user:
        print('Did you just not say anything, fine! I will not play with you')
        return False
    
   # if type(user) == int:
    #    print('Did you just say a number, wierdo!')
     #   return False
        

    sleep(1)
    print('Rock!')
    sleep(0.5)
    print('Paper!')
    sleep(0.5)
    print('Scissors!')
    sleep(0.5)
    print('The user chose', user)
    sleep(1)
    print('The computer chose', comp)
    sleep(1)
    print(i)
    sleep(1)

    if user == 'rock':
        print('Ha! I really chose paper--I WIN!')

    if user == 'paper':
        print('Ha! I really chose the hulk...wait we were not playing rock, paper, scissors, infinity?!')

    if user == 'scissors':
        print('Pffft I'+"'"+'m not dumb. I really chose rock--Now I got all the marbles!')


if __name__=='__main__':
    rps()

# coding: utf-8
#
# hw0pr2b.py
#
#2/5 satified
""" 
Title for your adventure:   The Quest.
Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.
"""

import time

def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
    """
    delay = 0.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    username = input("What do they call you, worthy adventurer? ")

    print()
    print("Welcome,", username, " to the Libra Complex, a labyrinth")
    print("of weighty wonders and unreal quantities...of poptarts!")
    print()

    print("Your quest: To find--and partake of--a poptart!")
    print()
    flavor = input("What flavor do you seek? ")
    if flavor == "strawberry":
        print("Wise! You show deep poptart experience.")
    elif flavor == "s'mores":
        print("The taste of the campfire: well chosen, adventurer!")
    else:
        print("Each to their own, then.")
    print()

    print("On to the quest!\n\n")
    print("A corridor stretches before you; its dim lighting betrays, to one side,")
    print("a table supporting nameless forms of inorganic bulk and, to the other,")
    print("a door ajar, leaking laughter--is that laughter?--of lab-goers.")
    time.sleep(delay)
    print()

    choice1 = input("Do you choose the table or the door? [table/door] ")
    print()
#if-else control statement here
    if choice1 == "table":
        print("As you approach the table, its hazy burdens loom ever larger, until...")
        time.sleep(delay)
        print("...they resolve into unending stacks of poptarts, foil shimmering.")
        print("You succeed, sumptuously, in sating the challenge--and your hunger.")
        print("Go well,", username, "!")

    else:  
        print("You push the door into a gathering of sagefowl, athenas, and stags alike,")
        print("all relishing their tasks. Teamwork and merriment abound here, except...")
        time.sleep(delay)
        print("...they have consumed ALL of the poptarts! Drifts of wrappers coat the floor.")
        print("Dizzy, you grasp for a pastry. None is at hand. You exhale and slip")
        print("under the teeming tide of foil as it finishes winding around you.")
        print("Farewell,", username, ".")

    print('As you sit enjoying your poptart, a small dog appears.')
    print('His name is clancy and he ask you if you would like to be in his spacecast')
    print('Do you decline is offer or ask for poptarts?')
    time.sleep(delay)
    print()

    choice2 = input('Will you ask for the poptarts or simply say no to his spacecast? [spacecast,poptarts]')
    print()
    #if-elif satified
    if choice2 == 'spacecast':
        print('He humbly asks you to sit down and talk about who you are as a person')
        print('Beginning with some ice-breakers, how you are from a race of mighty accountants and what not.')
        print('You discuss how you came to this rundown corridor as a favor to a friend who could not do so today.')
        print('Your friend was planning on flipping the location, but now you think it may not be worth their time.')
        print('Clancly look bored, do you continue the conversation or change the topic?')
        time.sleep(delay)
        print()

    elif choice2 == 'poptarts':
        print('Clancy looks at you pull out a box of poptarts')
        time.sleep(delay)
        print('Unfortunately they are not poptarts, but those one that they sell at traderjoes. And they are not the kind you like.')
        print('No, no one likes that kind of poptart. You stare in disgust at Clancey')
        print('He says, "OH! Judging me for like the TraderJoes(TM) Cinnammon Poptarts, Well I will have you know these are healthier!"')
        print('In anger clancy storm out and just a mysteriously as he came he teleports you to an unkown location where you spend the rest of your days')
        print('Farewell,', username, '.')
        print()
    
    choice3 = input('Will you continue the conversation or change it to something else? [Y/N]')

    if choice3 == 'Y':
        print('What do you talk about dear main character?[Do you talk about the current geopolitical event or How you began your love for poptarts?]')
        time.sleep(delay)
    
    #solitary if statement satified
    if choice3 == 'N':
        print('Clancy lets you drown on for another hour and then he leaves without a word')
        print('Doing this in the most obnoxious way possible!')
        print('He blows on a conch shell and instantly teleport out of sight')
        print('You begin your walk home and once you get there you notice you feel lightheaded')
        print('You fall on the street, you should have gone to your doctors appointment today, they said it was important')
        print('Farewell,', username, '.')

    choice4 = input('To simplify : [Globalevents, PoptartLove, Or something else]')
        
    if choice4 =  ('Globalevents'):
        print('Clancly takes this seriously, but seems to know little about your world culture and poilitics')
        print('He stays focused and actually pays attention to everything you say.')
        print('Facinate he promplty asks you...' + 'But WHO ASKED')
        print('You promptly leave, obviously upset')
        print('You poured your heart and soul into that topic, and that literal alien just insulted you')
        time.sleep(delay)
        print('Nothing bad happen to you,', username, ', you just learned some people can be jerks.')

    elif choice4 = ('PoptartLove'):

    else choice5 = ('Or something else'):
        print('You just spew random non-sense out of your mouth')
        print('However, that was exactly what clancy was looking for, and you sure did deliver.')
        print('Congrats, if anyone listened to that they would literally just waste their time.')
        time.sleep(delay)
        print('Get out of here,', username, ', NO ONE LIKES YOUR OR WHAT YOU HAVE TO SAY!')


    



if __name__ == '__main__':
    adventure()
