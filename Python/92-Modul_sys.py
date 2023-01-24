import sys

# ?sys.exit() programı kapatmya yarar

"""
stdin input almaya yara
stdout çıktı vermeyi yarar
stderr hata mesajı vermeyi yarar
"""
sys.stderr.write("Bu hata mesajı")
sys.stderr.flush()  # hemen yazdırma komutu verir
sys.stdout.write("\nBu normal yazıdır.")

print(sys.argv)

for i in sys.argv:  # terminelde çalışır
    print(i)
a = sys.stdin.readline()  # input alır
print(a)
"""PS C:\Users\User\Desktop\pyhton\Python> python 92-Modul_sys.py 1 4 5 #!Bu yazılması lazım
Bu hata mesajı
Bu normal yazıdır.['92-Modul_sys.py', '1', '4', '5']
92-Modul_sys.py
1#*bunlar yazıllır 
4
5
"""
