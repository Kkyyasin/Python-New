def selamla(isim="isimsiz"):  # varsayılan atılıyor
    print("Merhaba", isim)


selamla()
selamla("Ahmet")


def bilgileri_göster(isim="yok ", soyad="yok", numara="yok"):
    print(isim, soyad, numara)


bilgileri_göster("Mehmet", "Özdemir")  # sırala veriyor
# sadece numara vermek için paremetre vermek lazım
bilgileri_göster(numara="12345")
bilgileri_göster()  # birşey yazılmassa varsayılan atanır
# end paremteri varsayılan bir boşluk ama değiştirelebilir sep paremtresi , le ayrılana boşluk ama değiştirelebilir
print("mmm", "slls", sep="*", end="\n*\n")
# Esnek sayıda değerler istediğn kadar paremetre girmeye yarar


def toplama(*a):  # a girdiğmiz kadar tupple olur
    print(a)
    t = 0
    for i in a:
        t += i
    print(t)


toplama(3, 4, 5)
toplama(3, 4, 5, 6)  # istedimiz kadar girebiliriz
