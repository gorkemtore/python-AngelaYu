#gönderilen bir kelimeyi istenilen kadar ekrana yazdıran uygulama
kelime=input("Kelime girin:\t")
tekrar = int(input("Tekrar sayısı:\t"))


def yazdir(x):
    for i in range(tekrar):
        print(x)

yazdir(kelime)

