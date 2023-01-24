sözlük = {}  # vya dict()
kelimeler = {"kitap": "book", "car": "araba"}
print(len(kelimeler))  # len metodu vardı
sözlük = {"kitap": "book", "bilgisayar": "computer", "programlama": "programming",
          "dil": "language", "defter": "notebook"}
# sozlukler erişme
print(sözlük["kitap"])
çeviri_tablosu = {"Ö": "O",
                  "ç": "c",
                  "Ü": "U",
                  "Ç": "C",
                  "İ": "I",
                  "ı": "i",
                  "Ğ": "G",
                  "ö": "o",
                  "ş": "s",
                  "ü": "u",
                  "Ş": "S",
                  "ğ": "g"}
for i in çeviri_tablosu:
    print(çeviri_tablosu[i])
# sozluk oge ekleme
# sozluk[anahtar]=deger
print(sözlük)
sözlük["İsim"] = "yasin"
sözlük["Yas"] = 18
print(sözlük)
# sozluklerdde değişiklik yapma
sözlük["Yas"] = 25
print(sözlük)
# sozluk metodlar
# keys()
print(*sözlük.keys())  # anahtarları liste halinde dondururu
# values()
print(*sözlük.values())  # değerleri liste halinde döndürür
# items() tupple lar halindde döndürür
print("\n", *sözlük.items())
for i, j in enumerate(sözlük.items()):
    print(i+1, *j)
# get methodu()
ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}

sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")

print(ing_sözlük.get(sorgu, "Bu kelime veritabanımızda yoktur!"))
# get almaya yer alır alamazsa hata mesajı veriri
# clear( sözlugu siler)
# copy() kopyalamaya yarara egerki kopyalamassan değerde değişir
# pop elean siler
print(sözlük)
sözlük.pop("İsim")
print(sözlük)
# update() gunceller
stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15, "Isım": 5}
yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}
# eşit anahtar kelimeleir değiştirir diğerlerini birakır
stok.update(yeni_stok)
print(stok)
