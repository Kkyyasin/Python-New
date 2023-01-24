"""Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com"""


def kontrol(i):
    mail_adresleri = ["gmail.com", "yahoo.com"]
    for j in mail_adresleri:
        if i.endswith(j):
            return True
    return False


with open("C:\\Users\\User\\Desktop\\pyhton\\Python\\68-Problmlerler ileriseviye\\mailler.txt", "r", encoding="utf-8") as file:
    liste = file.readlines()
    for i in liste:
        i = i.strip("\n")
        if (i.find("@") != -1 and kontrol(i)):
            print(i)
