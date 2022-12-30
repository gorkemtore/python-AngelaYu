"""1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol
 eden python uygulamasını yapınız.

** Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır."""

# isim=input("İsminiz: ")
# yas = int(input("Yaşınız: "))
# egitim = input("Eğitim durumunuz: ")

# if yas>=18 and egitim == "Lise" or egitim=="Üniversite":
#     print("Ehliyet alabilirisinz.")
# else:
#     print("Ehliyet alma hakkınız yoktur.")


"""
2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına
 karşılık gelen not bilgisini yazdıran python uygulamasını yapınız.

0 -24 => 0

25-44 => 1

45-54 => 2

55-69 => 3

70-84 => 4

85-100 => 5"""
# yazili1= float(input("1. Yazılı Notunuz: "))
# yazili2= float(input("2. Yazılı Notunuz: "))
# sozlu = float(input("Sözlü Sınav Notunuz: "))
# ort = (yazili1+yazili2+sozlu)/3

# if ort >=0 and ort <= 24:
#     print("Rakam notu = 0")
# elif ort>24 and ort<=44:
#     print("Rakam notu = 1")
# elif ort>44 and ort <=54:
#     print("Rakam notu = 2")
# elif ort>54 and ort<=69:
#     print("Rakam notu = 3")
# elif ort>69 and ort<=84:
#     print("Rakam notu = 4")
# elif ort>84 and ort<=100:
#     print("Rakam notu = 5")
# else:
#     print("Bir hata oluştu.")


"""3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayan python
 uygulamasını yapınız.

1. Bakım => 1. yıl
2. Bakım => 2. yıl
3. Bakım => 3. yıl
** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
*** datetime modülünü kullanmanız gerekiyor. (simdi) - (2018/8/1) => gün
"""

# from dataclasses import dataclass
# import datetime
# tct = input("Trafiğe çıkış tarihi giriniz (Y/A/G) : ")
# tct = tct.split("/")
# trafigeCikis = datetime.datetime(int(tct[0]),int(tct[1]),int(tct[2]))
# sure = datetime.datetime.now() - trafigeCikis
# gun=sure.days

# if gun >=0 and gun<=365:
#     print("1. bakım")
# elif gun >365 and gun <=365*2:
#     print("2. bakım")
# elif gun>365*2 and gun <=365*3:
#     print("3. bakım")


"""4- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol eden python uygulamasını yapınız."""
# sayi = int(input("Sayı girin: "))
# if sayi %2== 0 and sayi>0 :
#     print("Pozitif ve çift")
# else: 
#     print("Pozitif ve çift değil.")

"""5- Email ve parola bilgileri ile giriş kontrolü yapınız.

email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('password: ')"""

# email = 'email@sadikturan.com'
# password = 'abc123'
# girilenEmail = input('email: ')
# girilenPassword = input('password: ')
# if email==girilenEmail:
#     if password==girilenPassword:
#         print("Giriş başarılı...")
#     else:
#         print("Şifre yanlış...")
# else:
#     print("E-mail yanlış...")


"""6- Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.
"""
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# if a>=b and a>=c:
#     print(f"En büyük {a}")
# elif b>=a and b>=c:
#     print(f"En büyük {b}")
# elif c>=a and c>=b:
#     print(f"En büyük {c}")


"""7- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayan python uygulamasını yapınız.

Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.

b-) Finalden 70 alındığında ortalamanın önemi olmasın.

"""
# vize1= float(input("1. Vize Notunuz: "))
# vize2= float(input("2. Vize Notunuz: "))
# final = float(input("Final Sınav Notunuz: "))
# ort = ((vize1+vize2)*0.6)+(final*0.4)
# if ort >= 50 and final>=50:
#     print("Başarılı")
# elif ort<50 and final>=70:
#     print("Başarılı")
# else: 
#     print("Başarısız...")

"""8- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayan python uygulamasını yapınız.

Formül: (Kilo / boy uzunluğunun karesi)

Aşağıdaki tabloya göre kişi hangi gruba girmektedir.

0-18.4 => Zayıf

18.5-24.9 => Normal

25.0-29.9 => Fazla Kilolu

30.0-34.9 => Şişman (Obez)"""

# name = input('adınız: ')
# kg = float(input('kilonuz: '))
# hg = float(input('boyunuz: '))

# index = (kg) / (hg ** 2)
# if index >= 0 and index <18.5:
#     print(f"Zayıf. İndexiniz: {index}")
# elif index>=18.5 and index<25:
#     print(f"Normal. İndexiniz: {index}")
# elif index >=25 and index<30:
#     print(f"Şişman. İndexiniz: {index}")
# elif index>=30 and index<35:
#     print(f"Obez. İndexiniz: {index}")
# else: print("Aralık dışı")

"""
Girilen bir sayı 0-100 arasında mı hesaplayın.
"""
# sayi = int(input("Sayı giriniz: "))
# if(sayi>0 and sayi<=100):
#     print("Sayı 0-100 arasında. ")
# else:
#     print("Aralık dışı")



