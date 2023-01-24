# dosya açma işlemi open ile yapılır
file = open("dosya1.txt", "w")  # ad,biçim
file.write("Merhaba\n")
file.write("\nYasin Bey")
file.close()
print("dosya yazıldı")
isimler = ["Yasin", "Mehmet", "Salih", "Tarık", "Zeynep"]
file = open("dosya1.txt", "a", encoding="utf-8")
for i in range(len(isimler)):
    file.write("\n{}-{}\n".format(i, isimler[i]))

file.close()
try:
    file = open("dosya1.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("dosya Bulunamadı")
# 1 yöntem okuma satır satır okur for dongüsyle
for i in file:
    print(i, end="")
file.close()
print("----------------------------------------------------------------")
# read fonksiyonu içine değer vermessen butun  herşeyi okur string döndürür
file = open("dosya1.txt", "r", encoding="utf-8")
içerik = file.read()
print(içerik)
içerik2 = file.read()
print(içerik2)  # içerik2 aynısı yazmaz sona geldiği için sondan okumya baslar
file.close()
print("----------------------------------------------------------------")
# readline fonksiyonu sadece tek satır okur ve imleç hareket eder
file = open("dosya1.txt", "r", encoding="utf-8")
print(file.readline())  # satır okur
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
print("----------------------------------------------------------------")
# readlines fonksiyonu her bir satır bir liste elamanı olacak şekilde listeye atar
file = open("dosya1.txt", "r", encoding="utf-8")
liste = file.readlines()
print(liste)
for i in liste:
    print(i, end="")
file.close()
