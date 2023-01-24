def ekstra(func):
    def wrapper(sayılar):
        tek_sayı_o = 0
        tek_sayı_m = 0
        cift_sayı_o = 0
        cift_sayı_m = 0
        for i in sayılar:
            if i % 2 == 0:
                cift_sayı_m += 1
                cift_sayı_o += i
            else:
                tek_sayı_m += 1
                tek_sayı_o += i
        print(func(sayılar))
        print("""
              Tek Sayılar Toplamı:{}
              Tek Sayılar Sayısı:{}
              Tek Sayılar Ortalaması:{}""".format(tek_sayı_o, tek_sayı_m, tek_sayı_o/tek_sayı_m))
        print("""
              Çift Sayılar Toplamı:{}
              Çift Sayılar Sayısı:{}
              Çift Sayılar Ortalaması:{}""".format(cift_sayı_o, cift_sayı_m, cift_sayı_o/cift_sayı_m))
    return wrapper


@ekstra
def ortalama_bul(sayılar):
    sum = 0
    for i in sayılar:
        sum += i
    return sum/len(sayılar)


ortalama_bul(range(1000000))
