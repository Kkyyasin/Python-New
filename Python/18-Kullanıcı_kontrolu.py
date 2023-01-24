print("""************************************************************
KUllanıcı Girişi
****************************************************************""")
while True:
    sys_kullanıcı_adı = "kkyyasin"
    sys_parolo = "190356"
    kullanıcı_adı = input("Kullanıcı adını giriniz:")
    paralo = input("Paralo giriniz:")
    if kullanıcı_adı == sys_kullanıcı_adı:
        if paralo == sys_parolo:
            print("Hoşgeldiniz")
            break
        else:
            print("hatali paralo")
    else:
        print("Hatali kullancı adı")
