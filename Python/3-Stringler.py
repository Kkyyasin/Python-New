# tanımlama çeşitleri
a = "Yasin"
print(a)
a = 'yasin'
print(a)
a = "aama"
print(a)
a = """
mee
aka"""
print(a)
a = "Python Dersleri"
print(a[2])
print(a[:3])
print(a[2:8])
print(a[2:11:3])
print(a[-1])  # son -1 den baslıyor
# uzunluk bulma
print(len(a))
a += "50 saat"
print(a)
print(a*3)
print(a, " ", 50, "saat")

print("Merhaba".lower())
print("merhaba dunya".split())
print("merr aja".split("r"))#girilen degerde liste gibi ayirir
yazi="Merhaba"
print(yazi.replace("a","e"))#harfleridegistermek icin kullanılır
print("merhaba %s"%(yazi))#%s formatla aynı görevi görür.

