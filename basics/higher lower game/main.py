from queue import Empty
from art import logo,vs
from game_data import data
from random import randint,choice
from os import system
datas_main = data
selected_A=""
selected_B=""
guess=""
count_B=0
count_A=0
score=0
should_continue =True
def change():
    """
    Changes selected_A with selected_B
    """
    global selected_A,selected_B,count_A,count_B
    selected_A =selected_B
    selected_B=""
    count_A,count_B=count_B,count_A
    count_B=0
    # print(f"Yeni count A ={count_A} yeni count B = {count_B}")
    print("*"*100)
    selected_B=""
def select():
    global selected_A, selected_B,count_B
    print(vs)
    selected_B = choice(datas_main)
    count_B = selected_B['follower_count']
    datas_main.remove(selected_B)
    print(f"Against B: {selected_B['name']}, {selected_B['description']} from {selected_B['country']} ")    
def wrong_Choose():
    global should_continue
    change()
    should_continue=False
    print(f"Sorry, that's wrong. Final score : {score}.")
def compare():
    global score, guess,should_continue,selected_B
    if guess=='A':
        if count_A>count_B:
            score+=1
            #change()
            system("cls")
            #print(selected_A)
            print(logo)
            print(f"You are right! Current score : {score}.")            
        else: wrong_Choose()
    elif guess=='B':
        if count_B>count_A:
            score+=1
            change()
            system("cls")
            print(selected_B)
            print(logo)
            print(f"You are right! Current score : {score}.")            
        else: wrong_Choose()
    else:
        print("Wrong typing")
        should_continue=False
def start():
    global count_A,selected_A
    print(logo)
    print("")
    selected_A = choice(datas_main)
    count_A = selected_A['follower_count']
    datas_main.remove(selected_A)

start()
while should_continue: 
    print(f"Compare A: {selected_A['name']}, {selected_A['description']} from {selected_A['country']} ")
    select()
    guess = input("Who has more followers? Type 'A' or 'B': ")
    compare()



