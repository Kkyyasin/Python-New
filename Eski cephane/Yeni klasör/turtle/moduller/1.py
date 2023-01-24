#os modulu
import os
print(os.getcwd())#içinde buluduğumuz mevcut klasoru yazar
print(os.listdir())#klasoreni içinde bulduğu dosyaları listeler
print(os.listdir('C:\\Users'))#içine girilen klasorun içindeki dosyaları liste objesine donusturur
os.chdir('C:\\Users')#mevcut klasoru değiştirir
print(os.listdir())
os.chdir('C:\\Users\\User\\Desktop\\pyton\\Yeni klasör\\turtle\moduller')
os.mkdir('C:\\Users\\User\\Desktop\\pyton\\Yeni klasör\\turtle\moduller\\yeni_klasor')#yeni klasor olusturur
print(os.listdir())
os.rmdir('C:\\Users\\User\\Desktop\\pyton\\Yeni klasör\\turtle\moduller\\yeni_klasor')
print(os.listdir())
with open("yeni.txt","w") as dosya:
    dosya.write("merhba")#dosya olusturur
os.remove("yeni.txt")#dosya siler
