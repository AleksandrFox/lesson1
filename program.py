game = dict(a = '1', b = '2', c = '3', d = '4', e = '5', f = '6', g = '7', h = '8', j = '9', )
jrt = True
while jrt:
    z = input('   :  ')
    for item in game.items():
        if z == item[1]:
            game[item[0]] = 'X' 
            jrt = False
            break
print(game)
