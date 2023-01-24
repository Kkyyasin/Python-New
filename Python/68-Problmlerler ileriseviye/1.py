"""Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın."""
metin = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
kume = set()
for i in metin:
    kume.add(i)
for i in kume:
    print("{} harfi {} defa gecer".format(i, metin.count(i)))
