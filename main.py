from gui import logo,stages
from list import words
import random
import os
def start_game ():
    random_word=random.choice(words).lower()
    lenght=len(random_word)
    word=[]
    for letter in random_word:
        word.append("_")
    print(logo)
    print(random_word)
    print(word)
    lifes=5
    game_end= False
    def refresher ():
        os.system("cls")
        print(logo)
        print(word)
        print(stages[lifes])

    while not game_end:
        guess=input("guess a letter\n").lower()
        if guess in random_word:
            if not guess in word:
                for n in range(lenght):
                    if random_word[n]==guess:
                        word[n]=guess
                refresher()
            else:
                refresher()
                print(f"This letter '{guess}' is exist. ")
            if not "_" in word:
                game_end=True
                print("You win, good job 😍😍😍")
        else:
            lifes-=1
            refresher()
            if lifes==0:
                game_end=True
                print("You Lose, try agin 😄😄😄")
play_agin="y"
while play_agin=="y":
    start_game()
    play_agin=input("To play again press Y, to exit press any key\n").lower()
    os.system("cls")
    