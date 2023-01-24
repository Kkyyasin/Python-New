# generatorler bellekte yer kaplamaz
# generetor fonsiyon gereksizbellek kullanımını onler
# gentorler
def kare_all():
    for i in range(1, 10):
        yield i**2  # generetor tanımlamada yer alır bellekte yer kaplanmaz birsey olusmaz


generetor = kare_all()
print(generetor)
ite = iter(generetor)
print(next(ite))
print(next(ite))
for i in ite:
    print(i)  # degerler yazılır yok olur yukardaki yielde erisilir
generetor2 = (i*3 for i in range(10))
ite2 = iter(generetor2)
for i in ite2:
    print(i)
# cok deger basıcaksak sadece gostermek için mantıklı ve bellekte yer kaplamaz


def carpim_tablosu():  # bosuna bellek işgal edilmez
    for i in range(1, 11):
        for j in range(1, 11):
            yield "{}x{}={}".format(i, j, i*j)


generetor2 = carpim_tablosu()
ite3 = iter(generetor2)
for i in ite3:
    print(i)
# range generatordur
