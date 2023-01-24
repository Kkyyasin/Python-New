"""Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri isimlere göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]"""
isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
soyadlar = ["Yılmaz", "Öztürk", "Dağdeviren",
            "Atatürk", "Dikmen", "Kaya", "Polat"]
liste = list(zip(isimler, soyadlar))
liste.sort()
for i, j in enumerate(liste):
    print(i+1, "-", j[0], j[1])
