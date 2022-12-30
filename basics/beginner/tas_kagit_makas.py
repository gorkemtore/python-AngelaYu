import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
secimler= []
secimler.append(rock)
secimler.append(paper)
secimler.append(scissors)
pc_Secim = random.randint(0,2)
oyuncu_Secim = int(input("Seçim yapın (0,1,2) "))
print(f"Oyuncumuz  Bunu Seçti : {secimler[oyuncu_Secim]}")
print(f"Bilgisayar Bunu Seçti : {secimler[pc_Secim]}")

if(oyuncu_Secim==pc_Secim):
    print("Durum berabere")
elif(oyuncu_Secim==0):
    if(pc_Secim==1):
        print("PC kazandı.")
    elif(pc_Secim==2):
        print("Oyuncu Kazandı.")
elif(oyuncu_Secim==1):
    if(pc_Secim==0):
        print("Oyuncu kazandı")
    elif(pc_Secim==2):
        print("PC kazandı")
elif(oyuncu_Secim==2):
    if(pc_Secim==0):
        print("PC kazandı")
    elif(pc_Secim==1):
        print("Oyuncu kazandı.")