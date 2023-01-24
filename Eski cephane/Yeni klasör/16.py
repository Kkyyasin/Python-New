asal=list()
sayi=int(input("sayi giriniz:"))
for i in range (2,sayi):
    a=0
    for j in range(2,i):
        if i%j==0:
            a=1
    if a==0:
        asal.append(i)
print(asal)
#range(, , ) birinci balangiç ikinci son 3 adım string ifade gibi
print(list(range(0,10,2)))
print([*range(0,10,2)])
#enumarete indexli gosterir
list1=['a','b','c']
for index,harf in enumerate(list1):
    print("{index}. harf:{harf}".format(harf=harf,index=index+1))
#zip birleştirir boyutu ayni olanlar
a=[1,2,3]
b=['a','b','c']
for index,harf in zip(a,b):
    print(index,harf)