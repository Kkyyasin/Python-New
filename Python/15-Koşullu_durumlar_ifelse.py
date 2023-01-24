a = 2  # block 1
if a == 2:
    print("Block 2")  # block 2
print("Block 1")  # block 1
# blocklar çıkıntılarla ayarlanır
if a == 3:
    print("Block 2")  # block 2
print("Block 1")  # block 1
# if
"""if (kosul):
        #if blogu kosul sağlanırsa çalışır.
"""
yas = int(input("yasınızı giriniz:"))
if yas < 18:
    print("Mekana giremezsiniz")
else:
    print("Mekana girebilirsin")
# if -elif-else çoklu koşullarda kullnılır.
islem = int(input("İşlem giriniz"))
if islem == 1:
    print("1 secildi")
elif islem == 2:
    print("2 secildi")
elif islem == 3:
    print("3 secildi")
elif islem == 4:
    print("4 secildi")
elif islem == 5:
    print("5 secildi")
elif islem == 6:
    print("6 secildi")
elif islem == 7:
    print("7 secildi")
elif islem == 8:
    print("8 secildi")
elif islem == 9:
    print("9 secildi")
elif islem == 0:
    print("0 secildi")
else:
    print("Rakam secilmedi")
