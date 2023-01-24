# input string biçimde veri alır
a = input("Lütfen bir sayı giriniz:")
print("girilen değer:{}".format(a))
try:
    a = int(input("Lütfen bir sayı giriniz:"))
except ValueError:
    print("lütfen sayı giriniz")
