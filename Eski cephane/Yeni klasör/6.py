#yildiz paremetreler
yazi="merhaba"
print(yazi)
print(*yazi)#yıldız paremte ayrı ayrı ayzar yani indislere ayırır
print(*yazi,sep="-")
def topla(*degerler):
    toplam=0
    for deger in degerler:
        toplam+=deger
    return  toplam




sayilar=[x for x in range(1,1001)]
print(topla(*sayilar))
sayilar1=[x for x in range( 1,100)if x%5==0]
print(sayilar1)
print(*sayilar1)
top=topla(*sayilar1)
print(top)
def goster(*args):
    for i in args:
        print(i,end="-")

goster(12,2,3)