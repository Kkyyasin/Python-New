def not_hesapla(satır):
    satır = satır[:-1]  # \n siliyoz
    liste = satır.split(',')
    note = float(liste[1])*0.3+float(liste[2])*0.3+float(liste[3])*0.4
    return [liste[0], note]


not_listesi = list()
with open("ogrenci_not_listesi.txt", "r", encoding="utf-8") as file:
    for i in file:
        not_listesi.append(not_hesapla(i))
max = 0
max_i = 0
min = 100
min_i = 0
for i in range(len(not_listesi)):
    print("\n{}-{}\nNot:{}\n".format(i+1,
          not_listesi[i][0], not_listesi[i][1]))
    if max < not_listesi[i][1]:
        max = not_listesi[i][1]
        max_i = i
    if min > not_listesi[i][1]:
        min = not_listesi[i][1]
        min_i = i
print("\n\\nEn yuksek alana kişi:{}\nEn dusuk alan kişi:{}\n".format(
    not_listesi[max_i][0], not_listesi[min_i][0]))
with open("not_listesi.txt", "w", encoding="utf-8") as file:
    for i in range(len(not_listesi)):
        file.write("\n{}-{}\nNot:{}\n".format(i+1,
                                              not_listesi[i][0], not_listesi[i][1]))
with open("kalan.txt", "w", encoding="utf-8") as file:
    for i in range(len(not_listesi)):
        if not_listesi[i][1] <= 50:
            file.write("\n{}-{}\nNot:{}\n".format(i+1,
                                                  not_listesi[i][0], not_listesi[i][1]))
with open("gecenler.txt", "w", encoding="utf-8") as file:
    for i in range(len(not_listesi)):
        if not_listesi[i][1] > 50:
            file.write("\n{}-{}\nNot:{}\n".format(i+1,
                                                  not_listesi[i][0], not_listesi[i][1]))
with open("harf_notu.txt", "w", encoding="utf-8") as file:
    for i in range(len(not_listesi)):
        if not_listesi[i][1] > 85:
            file.write("\n{}-{}\nHarf Notu:AA\n".format(i+1,
                                                        not_listesi[i][0]))
        elif not_listesi[i][1] > 75:
            file.write("\n{}-{}\nHarf Notu:BA\n".format(i+1,
                                                        not_listesi[i][0]))
        elif not_listesi[i][1] > 65:
            file.write("\n{}-{}\nHarf Notu:BB\n".format(i+1,
                                                        not_listesi[i][0]))
        elif not_listesi[i][1] > 55:
            file.write("\n{}-{}\nHarf Notu:CB\n".format(i+1,
                                                        not_listesi[i][0]))
        elif not_listesi[i][1] > 45:
            file.write("\n{}-{}\nHarf Notu:CC\n".format(i+1,
                                                        not_listesi[i][0]))
        elif not_listesi[i][1] > 35:
            file.write("\n{}-{}\nHarf Notu:DD\n".format(i+1,
                                                        not_listesi[i][0]))
        elif not_listesi[i][1] > 0:
            file.write("\n{}-{}\nHarf Notu:FF\n".format(i+1,
                                                        not_listesi[i][0]))
        else:
            file.write("\n{}-{}\nHarf Notu:Yok\n".format(i+1,
                                                         not_listesi[i][0]))
