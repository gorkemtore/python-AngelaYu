"""
open(dosyaAdi,dosyaErisme_modu)
w ==> write (dosyayı konumda oluşturur) ==> üstüne yazar, eskiyi siler
a ==> append (dosyayı konumda YOKSA oluşturur)
x ==> create (if there exist same file, it will give error)
r ==> read 

"""

with open("./file_management/newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    ##file.tell ==> cursor konumu
    # file.seek ==> cursor hangi byte'a gitsin?
    