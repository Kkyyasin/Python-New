#for dongusu
sayilar=[(1,2),(3,8),(2,4)]
for x,y in sayilar:
    print(x,y)
sarkilar={
    "dolunay":"reymenn",
    "kül":"cem adrian"
}
for sarki,sanatci in sarkilar.items():
    print("sarki:{} - sanatcisi:{}".format(sarki,sanatci))
for sanatci in sarkilar.values():
    print(sanatci)
for sarki in sarkilar.keys():
    print(sarki)
sayilar2=[x for x in range(1,11)]
toplam=0
for i in sayilar2:
    toplam+=i
print(toplam)