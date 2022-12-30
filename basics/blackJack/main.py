from operator import index
from random import choice
from art import logo
import os
def basla():
    print(logo)
    user_cards.append(choice(cards))
    user_cards.append(choice(cards))
    print(f"    Your Cards: {user_cards}, current score: {sum(user_cards)}")
    pc_cards.append(choice(cards))
    print(f"    Computer's first card: {pc_cards[0]}")

def compare(x,y,should_playAgain):
    if x>21 and control_11==True:
        x-=10
    

    if(x>y and x>21):
        print("You went over. You lose 😭")
        
        return should_playAgain
        os.system("cls")
    elif(x<y and y>21):
        print("Opponent went over. You win 😁")
        
        return should_playAgain
        os.system("cls")
    elif x > y:
        print("Opponent went over. You win 😁")
        
        return should_playAgain
        os.system("cls")
        
                    
    elif x < y:
        print("You went over. You lose 😭")
        
        return should_playAgain
        os.system("cls")
    else:
        print("Draw!")
        
        return should_playAgain
        os.system("cls")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#compare(sum(user_cards),sum(pc_cards),should_playAgain)
control_11 = False

pc_cards = []
user_cards = []
total_users = sum(user_cards)
total_pc = sum(pc_cards)
should_playAgain="y"
play_want = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")


while should_playAgain=='y':
    user_cards.clear()
    pc_cards.clear()
    if(play_want=='y'): basla()

    while True:
        control_take_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if control_take_card =='y':
            user_cards.append(choice(cards))
            total_users = sum(user_cards)
            total_pc = sum(pc_cards)
            print(f"    Your Cards: {user_cards}, current score: {total_users}")
            print(f"    Computer's first card: {pc_cards[0]}")
            
            for card in user_cards:
                if card ==11:
                    control_11=True

        if sum(pc_cards) < 13:
            while sum(pc_cards) <13:
                pc_cards.append(choice(cards))
                total_pc = sum(pc_cards)
                

        if(control_take_card=='n'):
            if total_pc < 13:
                while total_pc <13:
                    pc_cards.append(choice(cards))
                    total_pc = sum(pc_cards)


            total_users = sum(user_cards)
            total_pc = sum(pc_cards)
            break


        
            
        """if total_users>21:
            if control_11==True:
                total_users-=10"""
        
        if total_users>21:
            #print("21'i geçtiniz ")
            break
        
        

    print(total_users)
    print(f"    Your final hand: {user_cards}, final score: {total_users}")
    print(f"    Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")

    compare(total_users,sum(pc_cards),should_playAgain)
    should_playAgain=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if(should_playAgain=='n'):
        break





    

                    
                

            
        

    

            


            
            


        








