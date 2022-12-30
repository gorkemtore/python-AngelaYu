from asyncore import read


with open("./file_management/newfile.txt","r+",encoding="utf-8") as file: #r+ = okuma+yazma
    file.write("selamın aleyküm")
    print(file.read())
    
    