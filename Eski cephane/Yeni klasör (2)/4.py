#baslangıc degeri ve son degeri arası çıft sayıları bulucu
baslangic=int(input("baslangic degeri giriniz:"))
son=int(input("son degeri girin:"))
for i in range(baslangic,son+1):
    if i%2==0:
        print(i)