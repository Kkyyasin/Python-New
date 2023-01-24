# break döngüden çıkmaya yarıyor
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
for i in range(10):
    print(i)
    if(7 == i):
        break
while True:
    isim = input(
        "Çıkmak için q ya basınız yazdırmak için herhangi bir tuşa basınız")
    if isim == "q":
        break
    print("Merhaba")
# contine
for i in range(10):
    if i == 3 or i == 5:
        continue
    print(i)
