# faktoreyel
def faktoreyel(sayi):
    f = 1
    for i in range(2, sayi+1):
        f *= i
    return f


sayi = int(input(">>kac faktoreyel:"))
print(">>{} = {}".format(sayi, faktoreyel(sayi)))
for i in range(1, 21):
    print(">{}! = {}".format(i, faktoreyel(i)), end="\n----\n")
