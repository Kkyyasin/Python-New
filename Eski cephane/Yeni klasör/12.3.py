sozluk=dict()
for i in range(0,2):
    ingilizce=input("ingilizce kelime giriniz:")
    turkce=input("turkce karşılığını giriniz:")
    sozluk[ingilizce]=turkce
print(sozluk)
for i in sozluk:
    print("{}:{}".format(i,sozluk[i]))



