"""Problem 5
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)"""


def pisagor(sayı):
    liste = list()
    for i in range(1, sayı+1):
        for j in range(1, sayı+1):
            c = (i**2+j**2)**0.5
            if (c == int(c)):
                liste.append((i, j, int(c)))
    return liste


for i in pisagor(100):
    print(i)
