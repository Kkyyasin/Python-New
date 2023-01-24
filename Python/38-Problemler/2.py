"""Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;"""


def ebob_bul(a, b):
    eb = 1
    if a > b:
        c = b
    else:
        c = a
    for i in range(1, c+1):
        if a % i == 0 and b % i == 0:
            if i > eb:
                eb = i
    print("{} ile {} ebobu:".format(a, b), eb)


ebob_bul(24, 8)
