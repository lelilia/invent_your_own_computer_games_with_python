# https://inventwithpython.com/invent4thed/


import random
print('Ich werde eine Münze 1000 mal werfen. Rate wie oft Kopf kommt. (Drücke Enter um zu beginnen)')
guess = int(input())
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0,1) == 1:
        heads += 1
    flips += 1

    if flips == 900:
        print('900 mal geworfen und es gab '+str(heads)+' mal Kopf.')

    if flips == 100:
        print('Bei 100 Würfen kam  Kopf '+str(heads)+' mal.')

    if flips == 500:
        print('Halbzeit und schon '+str(heads)+' mal Kopf.')

print()
print('Von 1000 Würfen waren '+str(heads)+' Kopf')
if guess > heads:
    print('Du hast '+str(guess-heads)+' zu hoch geraten.')
elif guess < heads:
    print('Du hast '+str(heads-guess)+' zu niedrig geraten')
else:
    print('Oh wow du hast genau richtig gelegen!')
