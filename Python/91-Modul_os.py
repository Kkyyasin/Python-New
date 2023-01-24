# işletim sistemin modulu
import datetime
import os

print(os.getcwd())  # modulu dizinini gosteri
# os.chdir("C:/Users/user/Desktop") dizini değiştirir
# os.listdir() dizindeki dosyaları listeler
"""for i in os.listdir():
    print(i, end="  ")"""
# os.mkdir("Deneme1")  # klasor olusturur
# os.makedirs("Deneme2/Deneme3")  # iç içe klosar olusur
# os.rmdir("Deneme2/Deneme3")  # deneme2 altındaki deneme3 siler
# os.removedirs("Deneme2/Deneme3") # deneme2 ve deneme3 silinir
# os.rename("test.txt", "test2.txt") #test adını test2 adıyla değitirir
print(os.stat("kalan.txt"))  # text dosyasını ozelliklerini erişilir
print(datetime.datetime.fromtimestamp(
    os.stat("kalan.txt").st_mtime).ctime())  # değiştirme zamanı
# os.walk klasor yolu,klasor ismi ,dosya ismi diye ayırır listeye atar generetordur
for klasor_yolu, klasor_ismi, dosya_ismi, in os.walk("C:\\Users\\User\\Desktop\\pyhton\\Python"):
    """ print(klasor_yolu)
     print(klasor_ismi)
     print(dosya_ismi)
     print("*"*100)"""
    for j in dosya_ismi:
        if j.endswith(".txt"):
            print(j)
# ? Birçok os fonksiyonu vardır
