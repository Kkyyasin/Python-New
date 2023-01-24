#input fonksiyonu string gönderir
def kupal(sayi):
    return sayi**3
sayi=int(input("sayi giriniz:"))
print("{} sayinin kupu :{}".format(sayi,kupal(sayi)))
