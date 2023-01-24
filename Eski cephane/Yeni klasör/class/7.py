#json nasıl yazılır
import json
veriler=dict()
veriler["kullanici"]=list()
kadi=input("kullanici adi giriniz:")
passopord=input("pasaport giriniz:")
mail=input("mail giriniz:")
veriler["kullanici"].append({"kadi":kadi,"passopord":passopord,"mail":mail})
print(veriler)
for i in veriler["kullanici"]:
    print(i["kadi"])

with open("veriler.json","w") as dosya:
    json.dump(veriler,dosya)