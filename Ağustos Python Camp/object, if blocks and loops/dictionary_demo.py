kacOgrenci=int(input("Kaç öğrenci girilecek? : "))
ogrNo=''
ogrAd=''
ogrSoyad=''
ogrTel=''
ogrenciler = {
        ogrNo : {
            'ad':ogrAd,
            'soyad':ogrSoyad,
         'telefon':ogrTel
     }
}
ogrenciler.clear()
for i in range(0,kacOgrenci):
    print("--------------------")
    ogrNo=input("Öğrenci no giriniz: ")
    ogrAd=input("Ad: ")
    ogrSoyad=input("Soyad: ")
    ogrTel=input("Telefon: ")
    
    ogrenciler[i] = {
        ogrNo : {
            'ad':ogrAd,
            'soyad':ogrSoyad,
         'telefon':ogrTel
     } 
}
    print(ogrenciler[i])

print(ogrenciler)
print(''.center(100,"*"))

girilenOgr = input("İstediğiniz öğrencinin numarası = ")
print(ogrenciler[0][girilenOgr])