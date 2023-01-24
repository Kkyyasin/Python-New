#break donguden cıkamızı saglar
toplam=0
while True:
    sayi=int(input("sayi giriniz:"))
    toplam+=sayi
    a=input("cıkmak icin Dur yazin devam etmek icin herhangi bir tusa basiniz:")
    if a=="Dur":
        break
print(toplam)
#contine dongu olmamıs gibi davranır for degerinde i artar ama
toplam=0
for i in range(1,100):
    if i%2==1:
        continue
    toplam+=i
print(toplam)
