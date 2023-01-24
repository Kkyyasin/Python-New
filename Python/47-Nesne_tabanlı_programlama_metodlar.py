class Yazılımcı():
    def __init__(self, name, surname, num, maas, diller):
        self.name = name
        self.surname = surname
        self.num = num
        self.maas = maas
        self.diller = diller

    def bilgileri_göster(self):
        print("""
        Yazılımcı Özellikleri
    
    Ad:{}
    
    Soyad:{}
    
    Numara:{}
    
    Maas:{}
    
    Bildiği diller:{}      
              
              """.format(self.name, self.surname, self.num, self.maas, self.diller))

    def zam_yap(self, zam_yuzdesi):
        self.maas = self.maas*((100+zam_yuzdesi)/100)
        print("Maaşa zam yapıldı")

    def dil_ekle(self, dil):
        self.diller.append(dil)
        print("Dil eklendi...")


yazılımcı = Yazılımcı("Yasin", "özdemir", 171421005, 4000, [
                      "Python", "Java", "Javascript", "C"])
yazılımcı.bilgileri_göster()
yazılımcı.zam_yap(20)
yazılımcı.dil_ekle("C++")
yazılımcı.bilgileri_göster()
