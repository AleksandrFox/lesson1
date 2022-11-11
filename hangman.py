import random
import re
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
     O  |
        |
        |
       ===''','''
    +---+
     O  |
     |  |
        |
       ===''','''
    +---+
     O  |
    /|  |
        |
       ===''','''
    +---+
     O  |
    /|\ |
        |
       ===''','''
    +---+
     O  |
    /|\ |
    /   |
       ===''','''
    +---+
     O  |
    /|\ |
    / \ |
       ===''']
words = 'аист акула бабун баран барсук бобр бык верблюд волк воробей ворон выдра голубь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай черепаха пума семка скунс собака тигр тритон тюлень утка форель хорек ястреб ящереца'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
            
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже назвали эту букву. Назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess

def playAgain():
    print('Хотите сыграть еще раз? (да или нет)')
    return input().lower.startswith('д')

print('В И С И Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = all(secretWord[i] in correctLetters for i in range(len(secretWord)))

        if foundAllLetters:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('Вы исчерпали все попытки!\nНеугаданно букв:' + str(len(missedLetters)) + 'и угаданно букв:' + str(len(correctLetters)) + '. Было загаданно слово"' + secretWord + '".')
                gameIsDone = True
            
            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(words)
                else:
                    break