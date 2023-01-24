#global degişken
a=10
def goster():
    a=5
    return a

print("global:{}\nfonksiyon degişkeni:{}".format(a,goster()))
#lambda tek satırda fonksiyon tanımlamamızı sağlar
tekmi=lambda sayi:sayi%2==1
print(tekmi(2),tekmi(3),sep="\n")
toplam=lambda *sayilar:sum(sayilar)#sum girilen sayilarin listedekileri toplar verir * paremetresi liste gibi alır
print(toplam(12,55,55))