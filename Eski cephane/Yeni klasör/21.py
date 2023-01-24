def ebobbul(a, b):
    c = min(a, b)  # min degeri veri
    for i in range(c, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

    return 1


def ekokbul(a, b):
    c = min(a, b)
    while True:
        if a % c == 0 and b % c == 0:
            return c
        else:
            c += 1
    return 1


a = int(input("1-sayiyi giriniz:"))
b = int(input("2-sayiyi giriniz:"))
print("ekok:{}".format(ekokbul(a, b)),
      "ebob:{}".format(ebobbul(a, b)), sep="\n----\n")
