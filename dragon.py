# Das ist ein Choose your own Adventure aus https://inventwithpython.com/invent4thed/ mit genau einer Userinnen Eingabe


import random
import time


def displayIntro():
    print('''Du befindest dich in einem Land voller Drachen.
Vor dir siehst du zwei Höhlen.
In einer Höhle befindet sich ein netter Drache,
der seinen Schatz mit dir teilen wird.
In der anderen Höhle befindet sich ein hungriger Drachen,
der dich sofort aufessen wird.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('In welche Höhle willst du gehen? 1 oder 2?')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('Du näherst dich der Höhle...')
    time.sleep(2)
    print('Es ist dunkel und unheimlich...')
    time.sleep(2)
    print('Ein großer Drachen springt dich an! Er öffnet sein Maul und...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('gibt dir seinen Schatz')
    else:
        print('frisst dich auf.')

playAgain = 'ja'
while playAgain.lower() == 'ja' or playAgain.lower() == 'j':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Willst du nochmal spielen? (ja oder nein)')
    playAgain = input()
