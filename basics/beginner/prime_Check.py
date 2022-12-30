#Write your code below this line 👇
def prime_checker(number):
    asalMi=True
    for i in range(2,number):
        if number%i ==0:
            asalMi=False
            break
    if asalMi:
        print("Asal")
    else: print("Değil")
        





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
number= int(input("Check this number: "))
prime_checker(number)
