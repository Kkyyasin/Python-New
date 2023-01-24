dosya=open("uyeler.txt","a")

uyeler={
    "baskanlar":["ahmet","mehmet","salih"],
    "yardimcilari":["selin","yasin","mustafa"],
    "uyeler":["mehmet","yusuf","zeynep","sumeyye","eyup"]
}
while True:
    islem=int(input("\n1-kisi ekle \n2-kisi kaldir \n3-mevki ekle\n4-sistemden cık ve yazdir\nyapmak istediğiniz işlemi seciniz:"))
    if islem == 1:
        mevki=input("mevkisini giriniz({}):".format(list(uyeler.keys())))
        if uyeler.keys().__contains__(mevki):
           kisi=input("eklemek istediginiz kisiyi giriniz:")
           if uyeler[mevki].__contains__(kisi):  # kisini varlığnı kontrol eder
             print("{} uyesi vardir  uyelerde zaten".format(kisi))
           else:
            uyeler[mevki].append(kisi)
        else: print("{} adli mevki bulunmamaktadir".format(mevki))

    elif islem==2:
        print(uyeler)
        mevki = input("mevkisini giriniz({}):".format(list(uyeler.keys())))
        if uyeler.keys().__contains__(mevki):
             kisi = input("cıkarmak istediginiz kisiyi giriniz:")
             if uyeler[mevki].__contains__(kisi):
               uyeler[mevki].remove(kisi)
             else:
               print("{} uyesi yoktur uyelerde zaten".format(kisi))
        else:print("{} adli mevki bulunmamaktadir".format(mevki))

    elif islem == 3:
        mevki=input("eklemek istediğiniz mevkiyi giriniz:")
        uyeler[mevki] = list()
    elif islem == 4:
        break
    else:print("hatali kodlama yaptınız")
    for i in uyeler:
        print("\n{}:".format(i))
        for j in uyeler[i]:
            print(j)
print("------ UYELER ------",file=dosya)
for i in uyeler:
    print("\n{}:".format(str(i)),file=dosya)
    for j in uyeler[i]:
        print("-{}".format(str(j)),file=dosya)








