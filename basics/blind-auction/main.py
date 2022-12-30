import os
import art
# os.system("cls")
# HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program")
auctioneers = {}
control_isThere_auctioneers = True
while control_isThere_auctioneers:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))

    auctioneers[name] = bid

    print()
    if (input("Is there another bidders? Yes or No: ")).lower()=="no":
        print("Bitti")
        control_isThere_auctioneers=False
    else:
        os.system("cls")
result=0
result_name = ""
for x in auctioneers:
    if result<auctioneers[x]:
        result=auctioneers[x]
        result_name=x

        
print(f"{result_name} won, with ${result}!")
