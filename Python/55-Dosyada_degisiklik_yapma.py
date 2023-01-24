with open("dosya3.txt", "w", encoding="utf-8") as file:
    isimler = ["mehmet", "salih", "yasin", "zeynep",
               "mustafa", "aslı", "kerem", "leyla", "mecnun"]
    for i in isimler:
        file.write("{}\n".format(i))
    print("yazıldı...")
# seek ve write metoduyla değişiklik yapılır
with open("dosya3.txt", "r+", encoding="utf-8") as file:  # r+ hem okuyor hem yazabiyor
    a = file.read()
    print(a)
    file.seek(10)
    # belirtilen imleçten araya yazar ama pek sağlıklı değildir
    file.write("Ahmet")
    print("yazıldı...")
with open("dosya3.txt", "a+", encoding="utf-8") as file:  # dosyanın sonudan değişiklik yapmak
    yeni_kişiler = ["aslı", "mehmet", "tarkan"]

    for i in yeni_kişiler:
        file.write("{}\n".format(i))
    print("yeni kişiler eklendi")
    file.seek(0)
    print(file.read())
with open("dosya3.txt", "r+", encoding="utf-8") as file:  # dosyanın basında değişiklik yapmak
    a = file.read()
    yeni_değer = "salih\n"
    b = yeni_değer + a
    file.seek(0)
    file.write(b)
    print("dosya basa eklendi...")
with open("dosya3.txt", "r+", encoding="utf-8") as file:  # dosyanın ortasında değişiklik yapmak
    liste = file.readlines()
    print(liste)
    # istediğmiz araya eklebiliriz burda tam ortasına ekiyoruz
    liste.insert(len(liste)//2, "Mustafa murat\n")
    print(liste)
    file.seek(0)
    file.writelines(liste)  # listeyi yazdırmaya yarar
    print("eleman ortaya eklendi...")
