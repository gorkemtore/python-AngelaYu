import os


from cgi import print_arguments
from distutils.command.clean import clean
from turtle import clear


while True:
    os.system('clear')
    asalMi=True
    sayi=int(input("Sayı girin:\t"))
    if sayi==1:
            asalMi=False
    for i in range(2,sayi):
        if(sayi%i == 0):
            asalMi=False
                
    if asalMi:
        print(f"{sayi} asaldır")
        print("*"*100)
        
    else:
        print(f"{sayi} asal değildir")
        print("*"*100)
