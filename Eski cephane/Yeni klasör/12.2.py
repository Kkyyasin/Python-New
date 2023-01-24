gerilim=float(input("gerilim degerini giriniz:"))
direnc=float(input("direnç degerini giriniz :"))
while True:
    if direnc==0:
       direnc=float(input("direnç degerini giriniz 0 olamaz:"))
    else:break
akim=gerilim/direnc
print("akım: {}".format(akim))