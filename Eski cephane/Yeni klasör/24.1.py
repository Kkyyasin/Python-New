#sayini tam bolenlerini bulma
def bolenleri(sayi):
    bolen=list()
    for i in range(1,sayi):
        if sayi%i==0:
            bolen.append(i)
    return bolen
print(*bolenleri(20),sep="-")
a=bolenleri(20).copy()
print(a)
b=bolenleri(20).clear()
print(b)
c=bolenleri(20).index(5)#girilen değeri hangi indiste olgunu gosterir
print(c)
d=bolenleri(20).__contains__(5)#varlığını kontrol eder
print(d)
e=bolenleri(20).count(3)#varsa 1 girilen sayi yoksa 0 gonderir __contains__ gibi
print(e)
g=bolenleri(20)
g.sort(reverse=True)
print(g)
f=[1,7,8,2]
f.sort(reverse=True)
print(f)
def ekok(a,b):
    c = a*b
    for i in range(c,max(a,b),-1):
        if i%a==0 and i%b==0:
            c=i
    return c


print(ekok(6,8))
