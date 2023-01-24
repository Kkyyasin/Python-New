from json import*
with open("veriler.json","r") as dosya:
    veriler=load(dosya)
print(veriler)