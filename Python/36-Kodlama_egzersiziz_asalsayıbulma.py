# Asal sayı bulma
def asal_bul(sayı):
    c = 1
    for i in range(2, sayı):
        if sayı % i == 0:
            c = 0
    if c == 0 or sayı == 1:
        print("Asal sayı değildir")
    else:
        print("Asal saydır")


while True:
    secim = int(input("secim: "))
    if secim == -1:
        break
    else:
        asal_bul(secim)
