#1-100 arası rastgele üretilecek sayıyı kullanıcı bulmaya çalışsın. Her soru 20 puan. Aşağı yukarı ipucu olsun.
#hak bilgisini kullanıcıdan alın. Her yanlış -1 puan olsun.
from os import terminal_size
import random
puan=100

for i in range(0,5):
    rnd=random.randint(1,100)
    while(rnd!=0):
        karar= input("Geçmek için 'G' tuşlayınız, devam etmek için herhangi bir tuşa basınız: ")
        if(karar=='G'):
            rnd=0
            print(f"{4-i} soru kaldı")
            continue
        tahmin= int(input("Tahmin ediniz: "))
        print(F"CEVAP = {rnd}")
        print(F"TAHMİN = {tahmin}")
        if(karar!='G'):

            if(tahmin>rnd):
                puan-=1
                print(f"Daha küçük bir sayı girin! Kalan puanınız: {puan} ")
                

            elif(tahmin<rnd):
                
                puan-=1
                print(f"Daha büyük bir sayı girin! Kalan puanınız: {puan} ")

            elif(tahmin==rnd):
                print(f"İşte bu, başardın! Puanınız: {puan}  ")
                rnd=0
            else:
                print("BİR HATA OLUŞTU... ")