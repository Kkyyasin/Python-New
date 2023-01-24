import tkinter as tk
"""
Muhammed Yasin Özdemir
171421005
"""


def Tablo():
    frame = tk.Frame(pencere)

    ilk_satir = ["Bodrum", "Çeşme", "Marmaris"]
    ikinci_satir = ["Yetişkin", "Çocuk",
                    "Yetişkin", "Çocuk", "Yetişkin", "Çocuk"]
    family = ["Family", 10, 5, 6, 3, 2, 1]
    deluxe = ["Deluxe", 12, 6, 8, 4, 4, 2]
    king_suit = ["King Suit", 12, 6, 8, 4, 4, 2]
    for ilk in ilk_satir:
        tk.Label(frame, text=ilk, bd=5, relief="raised").grid(
            row=0, column=ilk_satir.index(ilk)+2, pady=4, padx=8)
    for ikinci in range(len(ikinci_satir)):
        tk.Label(frame, text=ikinci_satir[ikinci], bd=5, relief="raised").grid(
            row=1, column=ikinci+1, pady=6)
    for f in range(len(family)):
        tk.Label(frame, text=family[f], bd=5, relief="raised").grid(
            row=2, column=f, pady=6)
    for d in range(len(deluxe)):
        tk.Label(frame, text=deluxe[d], bd=5, relief="raised").grid(
            row=3, column=d, pady=6)
    for k in range(len(king_suit)):
        tk.Label(frame, text=king_suit[k], bd=5, relief="raised").grid(
            row=4, column=k, pady=6)
    frame.grid(row=8, column=1, pady=6)


def ToplamTutarHesapla():
    fiyatlar = {"Bodrum": {"Yetişkin": {"Family": 10, "Deluxe": 12, "King Suit": 14}, "Cocuk": {"Family": 5, "Deluxe": 6, "King Suit": 7}}, "Çeşme": {"Yetişkin": {"Family": 6, "Deluxe": 8,
                                                                                                                                                                   "King Suit": 10}, "Cocuk": {"Family": 3, "Deluxe": 4, "King Suit": 5}}, "Marmaris": {"Yetişkin": {"Family": 2, "Deluxe": 4, "King Suit": 6}, "Cocuk": {"Family": 1, "Deluxe": 2, "King Suit": 3}}}
    toplam_tutar_entry.delete(0, "end")
    toplam_tutar_entry.insert(0, str((fiyatlar[sehir_secim.get()]["Yetişkin"][oda_tarzi_secimi.get()]*yetiskin_sayisi_text.get() +
                                      fiyatlar[sehir_secim.get()]["Cocuk"][oda_tarzi_secimi.get()]*cocuk_sayisi_text.get())*gece_sayisi_text.get()))
    return (fiyatlar[sehir_secim.get()]["Yetişkin"][oda_tarzi_secimi.get()]*yetiskin_sayisi_text.get() +
            fiyatlar[sehir_secim.get()]["Cocuk"][oda_tarzi_secimi.get()]*cocuk_sayisi_text.get())*gece_sayisi_text.get()


def Rezervasyon():
    pencere2 = tk.Tk()
    if(ad_text.get().strip() == "" and soyad_text.get().strip() == ""):
        tk.Label(pencere2, text="Lütfen ad ve soyad alanını doldurunuz...").pack(
            padx=12, pady=8)
    try:
        if(ToplamTutarHesapla() == 0):
            tk.Label(pencere2, text="Lütfen gün sayısı ve kişi sayısı alanlarını doldurunuz...").pack(
                padx=12, pady=8)
        else:
            ad = tk.Label(pencere2, text="Ad :{}".format(
                ad_text.get()), width=50)
            ad.pack(padx=12, pady=8)
            soyad = tk.Label(pencere2, text="Soyad :{}".format(
                soyad_text.get()), width=50)
            soyad.pack(padx=12, pady=8)
            iletisim = tk.Label(
                pencere2, text="İletişim :{}".format(iletisim_text.get()), width=50)
            iletisim.pack(padx=12, pady=8)
            sehir = tk.Label(pencere2, text="Şehir :{}".format(
                sehir_secim.get()), width=50)
            sehir.pack(padx=12, pady=8)
            odatarz = tk.Label(pencere2, text="Oda Tarzı :{}".format(
                oda_tarzi_secimi.get()), width=50)
            odatarz.pack(padx=12, pady=8)
            yetiskins = tk.Label(pencere2, text="Yetiskin sayısı :{}".format(
                yetiskin_sayisi_text.get()), width=50)
            yetiskins.pack(padx=12, pady=8)
            cocuk = tk.Label(pencere2, text="Çocuk sayısı :{}".format(
                cocuk_sayisi_text.get()), width=50)
            cocuk.pack(padx=12, pady=8)
            gece = tk.Label(pencere2, text="Gün sayısı :{}".format(
                gece_sayisi_text.get()), width=50)
            gece.pack(padx=12, pady=8)
            tutar = tk.Label(pencere2, text="Toplam Tutar :{}".format(
                ToplamTutarHesapla()), width=50)
            tutar.pack(padx=12, pady=8)
            mesaj = tk.Label(pencere2, text="Rezerve edildi...", width=60)
            mesaj.pack(padx=36, pady=12)
    except tk.TclError:
        pencere3 = tk.Tk()
        tk.Label(pencere3, text="Lütfen gün ve kişi sayısı alanlarını sayı giriniz...").pack(
            padx=12, pady=12)
        yetiskin_sayisi_text.set(0)
        cocuk_sayisi_text.set(0)
        gece_sayisi_text.set(0)
        pencere3.mainloop()
    pencere2.mainloop()


def Reset():
    ad_text.set("")
    soyad_text.set("")
    iletisim_text.set("")
    yetiskin_sayisi_text.set(0)
    cocuk_sayisi_text.set(0)
    gece_sayisi_text.set(0)
    toplam_tutar.set(0)
    sehir_secim.set(sehirler[0])
    oda_tarzi_secimi.set(oda_tarzi_secenekleri[0])


def Exit():
    pencere.destroy()


pencere = tk.Tk()
pencere.title("Otel Rezervasyon Sistemi")
pencere.geometry("800x600")
baslik = tk.Label(pencere, text="Otel Rezervasyon Sistemi")
baslik.config(font=("bold", 18))
baslik.grid(row=0, column=1, pady=12)
ad_alan = tk.Label(pencere, text="Ad :", width=18)
ad_alan.grid(row=1, column=0, pady=6)
ad_text = tk.StringVar()
ad_entry = tk.Entry(width=40, textvariable=ad_text)
ad_entry.grid(row=1, column=1)
soyad_alan = tk.Label(pencere, text="Soyad :", width=18)
soyad_alan.grid(row=2, column=0, pady=6)
soyad_text = tk.StringVar()
soyad_entry = tk.Entry(width=40, textvariable=soyad_text)
soyad_entry.grid(row=2, column=1)
iletisim_alan = tk.Label(pencere, text="İletişim :")

iletisim_alan.grid(row=3, column=0, pady=6)
iletisim_text = tk.StringVar()
iletisim_entry = tk.Entry(width=40, textvariable=iletisim_text)
iletisim_entry.grid(row=3, column=1)
sehirler = ["Bodrum", "Çeşme", "Marmaris"]
sehir_secim = tk.StringVar()
sehir_secim.set(sehirler[0])
for secenek in sehirler:
    tk.Radiobutton(pencere, text=secenek,
                   variable=sehir_secim, value=secenek).grid(row=4, column=sehirler.index(secenek), pady=6)
oda_tarzi_alan = tk.Label(text="Oda Tarzı :")
oda_tarzi_alan.grid(row=5, column=0)
oda_tarzi_secenekleri = ["Family", "Deluxe", "King Suit"]
oda_tarzi_secimi = tk.StringVar()
oda_tarzi_secimi.set(oda_tarzi_secenekleri[0])
oda_tarzi_secim_menu = tk.OptionMenu(
    pencere, oda_tarzi_secimi, *oda_tarzi_secenekleri)
oda_tarzi_secim_menu.grid(row=5, column=1, pady=6)
kisi_sayisi_alan = tk.Label(text="Yetişkin / Çocuk sayısı :", width=18)
kisi_sayisi_alan.grid(row=6, column=0)
yetiskin_sayisi_text = tk.IntVar()
yetiskin_sayisi_entry = tk.Entry(pencere, textvariable=yetiskin_sayisi_text)
yetiskin_sayisi_entry.grid(row=6, column=1, pady=6)
cocuk_sayisi_text = tk.IntVar()
cocuk_sayisi_entry = tk.Entry(pencere, textvariable=cocuk_sayisi_text)
cocuk_sayisi_entry.grid(row=6, column=2, pady=6)
gece_sayisi_alan = tk.Label(text="Kaç gecelik tatil :", width=18)
gece_sayisi_alan.grid(row=7, column=0)
gece_sayisi_text = tk.IntVar()
gece_sayisi_entry = tk.Entry(pencere, textvariable=gece_sayisi_text)
gece_sayisi_entry.grid(row=7, column=1, pady=6)
Tablo()
toplam_tutar_alan = tk.Label(text="Toplam Tutar :", width=18)
toplam_tutar_alan.grid(row=9, column=0, pady=6)
toplam_tutar = tk.IntVar()
toplam_tutar_entry = tk.Entry(pencere, textvariable=toplam_tutar)
toplam_tutar_entry.grid(row=9, column=1, pady=6)
total_button = tk.Button(pencere, text="Tutar Hesapla",
                         command=ToplamTutarHesapla, padx=12, pady=6)
try:
    total_button.grid(row=10, column=0, pady=6)
    rezervasyon_button = tk.Button(
        pencere, text="Rezervasyon", command=Rezervasyon, padx=12, pady=6)
    rezervasyon_button.grid(row=10, column=1, pady=6)
except:
    pencere3 = tk.Tk()
    tk.Label(text="Lütfen gün ve kişi sayısı alanlarını sayı giriniz...").pack(
        padx=12, pady=12)
    pencere3.mainloop()
reset_button = tk.Button(text="Reset", command=Reset, padx=12, pady=6)
reset_button.grid(row=10, column=2, pady=6)
exit_button = tk.Button(text="Exit", command=Exit, padx=12, pady=6)
exit_button.grid(row=10, column=3, pady=6)
pencere.mainloop()
