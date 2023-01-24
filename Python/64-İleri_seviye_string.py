# upper ve lower ve capitalize
print("python".upper())  # sonuc:PYTHON
print("PYTHON".lower())  # sonuc:python
print("python".capitalize())  # sonuc:Python
# replace(x,y) x leri ylerle değiştirir
print("Merhbalar ne yapıyorsunuz".replace("a", "o"))
print("Merhbalar ne yapıyorsunuz".replace("ne", "napıyorsunuz"))
# starswith ve endswith neyle balnıyor yada sonlanıyır kontrol ediyor
print("python".startswith("py"))
print("python".startswith("ay"))
print("python".endswith("on"))
print("python".endswith("n"))
# split(x) liste oluşturuyor x değerine gore ayırıyor
print("Merhbalar ne yapıyorsunuz".split(" "))
# strip lstrip rstrip içine girilen karekterlerdeki değerleri siler etraftan bir şey girilmesse bosluk siler
print("              python           ".strip())
print("              python           ".lstrip())  # soldakileri siler
print("              python           ".rstrip())  # sağdakileri siler
print("..............python..............".strip("."))
# join listeden string oluşturuyor
liste = ["21", "02", "2022"]
print("/".join(liste))  # / işaretini araya alarak birleştiriyor
liste = ["T", "B", "M", "M"]
print(".".join(liste))
# count harf veya string sayar
print("merhaba dunya string".count("a"))  # a yı sayıyır
print("merhaba dunya string".count("a", 5))  # a yı 5 indesten itibaren sayıyor
# find arar bulursa index bulmassa -1 dondurur
print("merhaba skks".find("s"))  # s yi arar indes gonderir
print("merhaba skks".find("x"))  # -1 doner
print("merhaba skks".rfind("s"))  # rfind sondan arar
