name_pople = ['Вася','Петя','Валера','Саша','Даша']
def find_person(name_user):
    x = 0
    while name_pople:
        name = name_pople.pop()
        if name == name_user:
            print(f'{name}, нашелся')
            x += 1
        else:
            print(name)
    if x == 0:
        user_name = list(name_user)
        user_name[-1] = 'у'
        user_name = ''.join(user_name)
        print(f'{user_name}, не нашли')
find_person(input('Кого вы хотите найти?: '))  # type: ignoreСа