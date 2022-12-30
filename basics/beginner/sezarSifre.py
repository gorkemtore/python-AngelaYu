from email.mime import application
from operator import index
from pydoc import doc
import sys


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','ı','ö']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
alphabet_index=[i for i in range(len(alphabet))]
print(f"Alphabet index = {alphabet_index}")
def encrypt(text,shift):


    counter=0
    for i in range(shift,len(alphabet)+shift):
        alphabet_index[counter]=i
        counter+=1

    changer= len(alphabet_index)-1
    for i in range(alphabet_index[changer-1],alphabet_index[changer-1]-shift,-1):
        #26-25 logic
        different= i-len(alphabet)+1
        alphabet_index[changer]=different
        changer-=1
        #print(alphabet_index)
        #print("*"*100)

    alphabet_new=[]
    alphabet_new.clear()
    print(f"Alfabe index= {alphabet_index}")
    for x in alphabet_index:
        alphabet_new.append(alphabet[x])
    print(f"Eskisi = {alphabet}")
    print(f"Yenisi = {alphabet_new}")

    on_text_indexs=[]
    text_letter_list=[]
    ##print(text)
    for letter in text:
        text_letter_list.append(letter)

    for letter in text_letter_list:
        on_text_indexs.append(alphabet.index(letter))

    text_new=""
    for i in range(len(text)):
        #yeni alfabenin eski indexlerini yazdırcam
        text_new+=(alphabet_new[on_text_indexs[i]])


    print(text_new)
def decode(text,shift):
    print("DECODE ÇALIŞTI..... !!!!")
    counter=0
    for i in range(len(alphabet)-shift,shift*-1-1,-1):
        alphabet_index[counter]=i
        counter-=1
    #print(f"yeni indexler = {alphabet_index}")
    
    for i in range(shift):
        alphabet_index[i]= i+len(alphabet_index)-shift
        #print(f"yeni indexler = {alphabet_index}")
    
    
    alphabet_new=[]
    for i in range(len(alphabet)):
        alphabet_new.append(alphabet[alphabet_index[i]])
    #print(f"Eskisi = {alphabet}")
    #print(f"Yenisi = {alphabet_new}")

    on_text_indexs=[]
    text_letter_list=[]
    #print(text)
    for letter in text:
        text_letter_list.append(letter)

    for letter in text_letter_list:
        on_text_indexs.append(alphabet.index(letter))

    text_new=""
    for i in range(len(text)):
        #yeni alfabenin eski indexlerini yazdırcam
        text_new+=(alphabet_new[on_text_indexs[i]])    
    print(text_new)



if direction=='encode':   
    encrypt(text,shift)
elif direction=='decode':
    decode(text,shift)
else:
    print("Hatalı giriş yaptınız tekrar deneyin")
    
