"""Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi"""


def okunuşu(sayı):
    birler = ["", "bir", "iki", "üç", "dört",
              "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = ["on", "yirmi", "otuz", "kırk", "elli",
             "altmış", "yetmiş", "seksen", "doksan"]
    sayı = str(sayı)
    print(onlar[int(sayı[0])-1], birler[int(sayı[1])])


for i in range(10, 100):
    okunuşu(i)
