print(35)
print(3.14)
print("yasin")
a = 4
b = 5
print(a+b)
print(a, b)
print("Not:", a*5+b*10)
# , bosluklu + boskluksuz
# \n alt satıra gec
print("Merhaba\nNasılsın\niyimisin")
# \t tab kadar bosluk
print("Merhaba\t\tNasılsın")
print("""1-Ahmet
2-Mehmet""")
# type() türünü bulur
print(type(3.14))
print(type(3))
print(type("mam"))
# sep paremetresi
print(15, 44, 55, 22, sep="/")
print("Ahmet", "Mehmet", sep="\n")
# * paremetresi boslukla ayırıyor
print(*"Python")
print(*"TBMM", sep=".", end="\n-\n")

# Formatlama
a = 3
b = 4
print("{}+{}={}".format(a, b, a+b))
print("{1} {0} {2}".format("Ahmet", "Mehmet", 55))
# formatlar Pyformat sitesi
