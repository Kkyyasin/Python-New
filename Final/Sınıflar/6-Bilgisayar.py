class Resulation():
    def __init__(self, en, boy):
        self.en = en
        self.boy = boy

    def __str__(self):
        return "{}x{} piksel".format(self.en, self.boy)

    def __len__(self):
        return self.en*self.boy

    def __eq__(self, other):
        if isinstance(other, Resulation):
            return self.en == other.en and self.boy == other.boy
        return False


class Monitor():
    def __init__(self, model, uretici, resulation):
        self.model = model
        self.uretici = uretici
        self.resulation = resulation
        self.m_durum = "Kapali"

    def __str__(self):
        return "*********** MONITOR **************\nModel: {}\nUretici: {}\nResulation: {}".format(self.model, self.uretici, self.resulation.__str__())

    def MonitorKapat(self):
        self.m_durum = "Kapali"
        print("Monitor Kapanıyır")

    def MonitorAc(self):
        self.m_durum = "Acik"
        print("Monitor aciliyor...")


class Kasa():
    def __init__(self, model, uretici, malzeme):
        self.model = model
        self.uretici = uretici
        self.malzeme = malzeme
        self.pc_durum = "Kapali"

    def __str__(self):
        return "*********** KASA **************\nModel:{}\nUretici:{}\nMalzeme:{}".format(self.model, self.uretici, self.malzeme)

    def BilgisayariBaslat(self):
        self.pc_durum = "Acik"
        print("Bilgisayar başlatılıyor...")

    def BilgisayariKapat(self):
        self.pc_durum = "Kapat"
        print("Bilgisayar kapaniyor...")


class Anakart():
    def __init__(self, model, uretici, yuva_sayisi, isletim_sistemi):
        self.model = model
        self.uretici = uretici
        self.yuva_sayisi = yuva_sayisi
        self.isletim_sistemi = isletim_sistemi

    def __str__(self):
        return "*********** ANAKART**************\nModel :{}\nUretici :{}\nYuva Sayisi :{}\nIsletim Sistemi :{}".format(self.model, self.uretici, self.yuva_sayisi, self.isletim_sistemi)

    def __len__(self):
        return self.yuva_sayisi


class PC():
    def __init__(self, marka, model, anakart, monitor, kasa):
        self.marka = marka
        self.model = model
        self.anakart = anakart
        self.monitor = monitor
        self.kasa = kasa

    def __str__(self):
        return """
                {0} {1}\n
    Anakart :{2}\n
    Monitor :{3}\n
    Kasa :{4}\n
""".format(self.marka, self.model, self.anakart, self.monitor,  self.kasa)


kasa = Kasa("Asus RTX", "Asus", "Çelik")
resulation = Resulation(1920, 1080)
monitor = Monitor("Samsung 456", "Samsung", resulation)
anakart = Anakart("Intel İ7", "Intel", 16, "Windows 11")
pc = PC("Monster", "Abra A5", anakart, monitor, kasa)

print(pc)
print(pc.anakart.__len__())
kasa.BilgisayariBaslat()
kasa.BilgisayariKapat()
monitor.MonitorAc()
monitor.MonitorKapat()
