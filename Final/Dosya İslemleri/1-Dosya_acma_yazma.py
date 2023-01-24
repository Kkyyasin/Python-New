isimler = ["Pinkie", "Antone", "Dominic",
           "Danny", "Adolphus", "Alana", "Hershel"]
# dosya yazma
with open("dosya.txt", "w") as dosya:
    dosya.write("******* Isimler ********\n")

    for i in range(len(isimler)):
        dosya.write("\n{}-{}\n".format(i, isimler[i]))

# dosya okuma
with open("dosya.txt", "r") as dosya:
    icerik = dosya.read()
print(icerik)  # sting doner
with open("dosya.txt", "r") as dosya:
    icerik = dosya.readlines()
print(icerik)  # her satırır liste elemanı doner


# bu fonksiyon sayesind eotamatik kapanır dosya
with open("dosya2.txt", "w", encoding="utf-8") as file:
    liste = ["345", "sadas", "324a", "14", "kemal"]
    for i in liste:
        file.write("{} - ".format(i))
    print("dosya yazıldı...")
    # tell fonksiyonu yerini öğrenmeye yarar seek fonksiyonu yer değiştirmeye
with open("dosya2.txt", "r", encoding="utf-8") as file:
    a = file.read(5)  # içine ne yazılırsa okadar bayt okur
    print(file.tell())  # ve imleçin yerini gösterir
    print(a)
    file.seek(15)  # yerini değiştirdik
    b = file.read(6)  # okuma yaptırdık değiştirdiğimiz yerden itibaren
    print(b)
    print(file.tell())
