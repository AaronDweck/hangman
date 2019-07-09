from time import *
import random
easy = ['active','apple','angry','phone','salt','toilet','math','cake','future','goat','butter','wierd']
medium = ['goodbye','butterfly','english','wizard','doctor','reading','avatar','pokemon','hamster','rocket','online','python','controller']
hard = ['hello','welcome','goodnight','science','download','academy','password','clickbait','defualt','upgrade','describe',]
def game ():
    print('''                                ________________
                                   /                \\
                                  |   welcome to     |
                                  |     HANGMAN!     |
                                  | EASY MEDIUM HARD |
                                   \________________/
             ''')
    hangman_board = ['''
    /--------\\
             |
             |
             |
             |
             |
             |
    _________|___''','''
    /--------\\
       |     |
             |
             |
             |
             |
             |
    _________|___''','''
    /--------\\
       |     |
       o     |
             |
             |
             |
             |
    _________|___''','''
    /--------\\
       |     |
       o     |
       |     |
             |
             |
             |
    _________|___''','''
    /--------\\
       |     |
       o     |
      /|     |
             |
             |
             |
    _________|___''','''
    /--------\\
       |     |
       o     |
      /|\    |
             |
             |
             |
    _________|___''','''
    /--------\\
       |     |
       o     |
      /|\    |
             |
             |
             |
    _________|___''','''
    /--------\\
       |     |
       o     |
      /|\    |
       |     |
             |
             |
    _________|___''','''
    /--------\\
       |     |
       o     |
      /|\    |
       |     |
      /      |
             |
    _________|___''','''
    /--------\\
       |     |
       o     |
      /|\    |
       |     |
      / \    |
             |
    _________|___''']
    level = input('pick level easy medium or hard ')
    if level == 'easy':
        (random.shuffle(easy))
        word = (random.choice(easy))
    elif level == 'medium' :
        word = (random.choice(medium))
    elif level == 'hard':
        word = (random.choice(hard))
    else:
        print ('THAT WAS NOT ONE OF YOUR CHOICES!!')
    correct = []
    incorrect = []

    def board ():
        print(hangman_board[len(incorrect)])
        for i in word:
            if i in correct:
                print(i, end= ' ')
            else:
                print('_', end=' ')
        print('\n\n')
        print('*****missed letters*****')
        for i in incorrect:
            print(i, end=' ')
        print('\n************************')

    def user_guess ():
        while True:
            guess = input('guess a letter\n')
            if guess in correct or guess in incorrect:
                print ('you already guessed that letter')
            elif len(guess) > 1:
                print ('please enter only one letter at a time')
            elif guess.isnumeric():
                print('please enter only letters')
            elif len(guess) == 0:
                print('please enter a letter')
            else:
                break
        if guess in word:
            correct.append(guess)
        else:
            incorrect.append(guess)

    def winning_and_losing():
        if len(incorrect) > 8:
            return'game over'
        for i in word:
            if i not in correct:
                return'not a win'
        return'win'
    while True:
        board()
        user_guess()
        win_condition = winning_and_losing()

        if win_condition == 'game over':
            print ('GAME OVER!!!! the word is %s' % word) 
            new_game = input('do you want to play again [y/n]')
            if new_game == 'y':
                game()
            else:
                print('thanks for playing good bye')
                sleep(1)
                break
            
        elif win_condition == 'win':
            print('YOU WIN!!!!!! the word is %s' % word)
            new_game = input('do you want to play again [y/n]')
            if new_game == 'y':
                game()
            else:
                print('thanks for playing good bye')
                sleep(1)
                break
    
game ()        
