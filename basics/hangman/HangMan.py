#Step 1 
import random
import art_hangman
import hangman_words

word_list = hangman_words.word_list
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(f"Cevap: {chosen_word}")
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
entried_letter_b4 =[]
chosen_len = len(chosen_word)
spaces=""

art =art_hangman.stages
life_art=len(art)-1
for i in chosen_word:
    spaces+="_"
print(spaces)
life=7 #CAN HAKKI
kacTaneVar=0
while(life>=0):
    man="" 
    num_index=0
    guess = input("Input a letter: ")
    guess.lower()
    entried_letter_b4.append(guess)   

    for letter in chosen_word:
        
        if letter == guess:
            kacTaneVar+=1
            spaces=list(spaces)
            spaces[num_index]=guess
            
            
        num_index+=1
     

    #BURASI BOŞLUK DOLDURUYOR.  
    for i in range(chosen_len):
        if spaces[i]=="_":
            man+="_"
        else:
            man+=spaces[i]
        
    if(man==chosen_word):
        print("KAZANDINIZ TEBRİKLER!")
        break
    print(man)
    if(kacTaneVar!=0):
        print(f"Girdiğiniz harften {kacTaneVar} adet var.")
        kacTaneVar=0
    else:
        print("Girdiğiniz harf yok.")
        life-=1
        
        if(life==-1):
            print("*"*60)
            print("GAME OVER!")
        else:
            print(f"Kalan canınız = {life}")
            print(art[life_art])
            art.remove(art[life_art])
            life_art-=1



#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
