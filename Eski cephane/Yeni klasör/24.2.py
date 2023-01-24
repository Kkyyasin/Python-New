def asal(sayi):
    for i in range(2,sayi):
        if sayi%i==0:
            return "asal degil"
    if sayi==1:
        return "asal degil"
    return "asal"
while True:
    sayi=int(input("1-sayi giriniz:\n2-cıkmak icin 0 a basınız:"))
    if sayi==0:
        break
    else:
        print(">>>{} sayisi {}".format(sayi,asal(sayi)))
