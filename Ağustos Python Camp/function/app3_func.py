#gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon

sayi1=10
sayi2=20
#beklenen asallar: 11,13,17,19
def asalBul(a,b):
    asalMi=True
    for i in range(a,b):
        for j in range(2,i):
                if(i%j==0):
                    asalMi=False
                    break
                
        if asalMi==True:
            print(f"{i} sayısı asaldır.")
        
        asalMi=True


            
asalBul(sayi1,sayi2)




