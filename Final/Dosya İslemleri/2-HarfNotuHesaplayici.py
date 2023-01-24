
def HarfNotuVer(liste):
    newliste = []
    for i in liste:
        if i > 90:
            newliste.append("AA")
        elif i > 75:
            newliste.append("BB")
        elif i > 60:
            newliste.append("CC")
        elif i > 45:
            newliste.append("DD")
        elif i > 30:
            newliste.append("FD")
        else:
            newliste.append("FF")
    return newliste


def NotHesapla(liste):
    newliste = []
    for i in liste:
        newliste.append(int(i[1])*0.3+int(i[2])*0.2 + int(i[3])*0.5)
    return newliste


def ListeDuzenle(liste):
    newliste = []
    for i in liste:
        i = i.strip("\n")
        i = i.split(",")
        newliste.append(i)
    return newliste


try:
    with open("notlar.txt", "r", encoding="utf-8") as file:
        liste = file.readlines()
except FileNotFoundError:
    print("Dosya yoktur")
liste = ListeDuzenle(liste)
notlar = NotHesapla(liste)
harfnotlari = HarfNotuVer(notlar)

with open("Puanlar.txt", "w", encoding="utf-8") as file:
    file.write("************* Notlar **************\n\n")
    for i in range(len(liste)):
        file.write("{}-{} kisi {} not ile {} aldı.\n".format(i +
                   1, liste[i][0], notlar[i], harfnotlari[i]))
