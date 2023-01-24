#str fonksiyonları
yazi="Merhaba Dunya"
print(yazi.upper())#butun harfleri buyutur
print(yazi.lower())#butun harfleri kucultur
yazi2="cocuk arabaya bindi"
print(yazi2.startswith("cocuk"))
print(yazi2.startswith("k"))#neyle basladığını kontrool eder
print(yazi2.startswith("c"))
print(yazi2.startswith(("cocuk","c","k")))
print(yazi2.endswith(("i","bindi")))#neyle bittiğini kontrol eder
print(yazi2.split())#standarat olaark boşluğa gore ayırır.
yazi3="me-azkk-aooaz-sxxs"
print(yazi3.split("-"))#içine girilene gore ayırır
print(yazi2.replace("cocuk","adam"))#değiştirme yapar
print(yazi2.strip("cocuk "))#girilen ifadeyi siler,
print(yazi2.find("arabaya"))#hangi indiste basladığı numarasini verir
print(yazi2.count("a"))#kac tane olduğunu gosterir
yazi4=["merhaba","dunya"]
print(" ".join(yazi4))
print("-".join(yazi4))#listedeki string ifadeleri birleştitir
