def tam_bolenleri(sayı):
    liste = list()
    for i in range(1, sayı+1):
        if sayı % i == 0:
            liste.append(i)
            liste.append("-")
    liste.pop()
    return liste


while True:
    secim = int(input("secim: "))
    if secim == 0:
        break
    else:
        print(secim, "sayısını tam bolenleri:", *tam_bolenleri(secim))
