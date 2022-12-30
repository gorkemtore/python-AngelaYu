liste =["1","2","5a","10b", "abc","10","50"]

#listedeki sayısal değerleri bulunuz
# import re
# def SayisalBul():
#     for deger in liste:
        
#         if not re.search("[_@$]",deger) and not re.search("[a-z]",deger) and not re.search("[A-Z]",deger):
#             print(deger)
        
# SayisalBul()




#kullanıcı 'q' girmedikçe her input sayısal olsun. aksi durumda hata mesajı versin
# import re
# def VeriGir(girilen):
    
#     if(girilen=="q"):
#         print("q girdiniz ve bitti")
#     else:
#         try:
#             VeriGir(girilen)
#         except Exception as ex:
#             if re.search("[a-z]",girilen) or re.search("[A-Z]",girilen) or re.search("[\s]",girilen) or re.search("[_@$]",girilen):
#                     print("İstenen karakter dışında veri girdiniz: ")

# while True:
#     girilen = input("Veri girin: ")
#     VeriGir(girilen)
#     if(girilen=="q"): break
    





#girilen paraloda türkçe karakter olmasın
# from logging import exception
# import re
# def turkceKontrol(pwd):
#     if not re.search("[İ,ş,ğ,ç,ö,ü]",pwd):
#         print("Parolanız oluşturuldu.")
#     else:
#         print("Türkçe karakter kullanmayınız...")

# turkceKontrol(input("Şifre girin: "))
