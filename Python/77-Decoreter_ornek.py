"""1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin."""


def mukemmel_sayilar(func):
    def wrapper(sayılar):
        for i in sayılar:
            sum = 0
            for j in range(1, i):
                if i % j == 0:
                    sum += j
            if sum == i:
                print(i)
        func(sayılar)
    return wrapper


@mukemmel_sayilar
def asal_bul(sayilar):
    for i in sayilar:
        c = 1
        for j in range(2, i):
            if i % j == 0:
                c = 0
        if c == 1:
            print(i, end="   ")


asal_bul(range(1000))
