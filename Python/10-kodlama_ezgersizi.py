# Oyuncu Kaydetme
ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı")
takım = input("Oyuncunun Takımı:")
bilgiler = [ad, soyad, takım]
print("Bilgiler Kaydediliyor ...")
print("""
Oyuncu
Adı:{}
Soyadı:{}
Takımı:{}""".format(*bilgiler)
      )
