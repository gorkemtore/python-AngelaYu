import random
import os
from art import logo
should_playAgain="y"
def compare(guess_num,created_num):
    if guess_num>created_num:
        print("Too high")
        print("Guess again")
    elif guess_num<created_num:
        print("Too low")
        print("Guess again")
    else:
        global should_playAgain
        print("Congratulations")
        should_playAgain =input("Do u want play again? Type, 'y' or 'n': ")
        return True

def difficult_level(level_chosen):
    global right_of_life
    if level_chosen=='easy':
        right_of_life=10
    elif level_chosen=='hard':
        right_of_life=5
    
def starting():
    os.system("cls")
    print(logo)
    global create_number
    global level
    print("Welcome to the Guess Number game...")
    create_number = random.randint(1,101)
    #print(f"create num = {create_number}")
    print("Choose a level for game")
    level = input("Type 'easy' for easy level or type 'hard' for hard level: ")
    difficult_level(level)
    print(f"You have {right_of_life} attempts remaining to guess the number.")

def play_game():
    global right_of_life
    while right_of_life>0:
        guess= int(input("Guess a number: "))
        if(compare(guess,create_number)==True): break
        #compare(guess,create_number)
        right_of_life-=1
        print("")
        print(f"You have {right_of_life} attempts remaining to guess the number.")

while should_playAgain=='y':
    starting()
    play_game()


    
    

