import random
import time

def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
    перед собой вы видите две пещеры. В одной из них - дружелюбный дракон, 
    который готов поделиться с вами своими сокровищами. Во второй -
    жадный и голодный дракон, который мигом вас съест. ''')
    print()

def chooseCave():
    cave = ''
    while cave not in [1, 2]:
        print('В какую пещеру вы войдете? (Нажмите клавишу 1 или 2)')
        cave = int(input())
    return cave

def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Её темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == friendlyCave:
        print('...делится с вами своими сокровищами!')
    else:
        print('...моментально вас съедает!')

playAgain = 'да'
while playAgain in {'да', 'д', 'lf', 'l'}:
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input() 