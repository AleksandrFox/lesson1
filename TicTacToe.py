game = dict(a = '1', b = '2', c = '3', d = '4', e = '5', f = '6', g = '7', h = '8', j = '9', )

def paint(game):
    return [f'''
     {game['g']} | {game['h']} | {game['j']}
    ---+---+---
     {game['d']} | {game['e']} | {game['f']}
    ---+---+---
     {game['a']} | {game['b']} | {game['c']}
    ''']
    

def displayBoard():
    print(paint(game)[0])
    print()

def playAgain():
    print('Хотите сыграть еще раз? (да или нет)')
    return input().lower.startswith('д')

step = 9
player1 = 'X'
player2 = 'O' 

while step != 0:
    displayBoard()
    gameIsDone = True
    while gameIsDone:
        z = input('Введите цифру :  ').lower()
        for item in game.items():
            if z == item[1]:
                game[item[0]] = player2 if step %2==0 else player1
                gameIsDone = False
                game.update()
                break
    step -=1
displayBoard()

