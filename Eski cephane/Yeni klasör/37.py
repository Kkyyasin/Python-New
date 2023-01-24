kisiler=["mehmet","MEhmet","  saLih","zeynep","ZEynep","saLih"]
a=list()
for kisi in kisiler:
    a.append(kisi.lower().strip().capitalize())
b=set(a)
for i in b:
 if  a.count(i)>1:
     print(i)
def reverse(param):
    a=param
    b=list()
    while a>0:

        b.append(a%10)
        a//=10

    toplam=0
    for i in range(len(b)):
        toplam+=(10**(len(b)-i-1))*b[i]
    return toplam
print(reverse(1224))
sayi=int(input("sayi giriniz:"))
print(reverse(sayi))

