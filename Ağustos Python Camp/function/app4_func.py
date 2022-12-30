#gönderilen sayının tam bölenlerini listeleyen fonksiyon
bolenList =[]
def bolenBul(sayi):
    bolenList.clear()
    for i in range(1,sayi):
        if sayi%i == 0:
            bolenList.append(i)
    print(f"Girdiğiniz {sayi} sayısını tam bölenlerin listesi: {bolenList} şeklindedir.")
    

bolenBul(20)
bolenBul(124)