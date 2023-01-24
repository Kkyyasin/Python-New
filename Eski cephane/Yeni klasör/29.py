dosya=open("planlar.txt","r",encoding="utf-8")
print(dosya.read(5))#dosyayı string gibi okur \n ler dahil
dosya.seek(0)#dosyayı başlama yerini belirtir
print(dosya.read(15))
print(dosya.tell())#dosyanın nerde olduğunu soyler
dosya.seek(0)
print(dosya.read())
dosya.seek(0)
print(dosya.readline())#satırı okur sadece
print(dosya.readlines())##liste objesi donusturur
print(dosya.tell())
dosya.close()

