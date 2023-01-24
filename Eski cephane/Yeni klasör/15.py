import random
yazi=0
tura=0
para=["Yazi","Tura"]
atismiktari=int(input("para kac kere havaya atilsin:"))
while atismiktari>0:
    paraustu=random.choice(para)
    if paraustu=="Tura":
        tura+=1
    else:
        yazi+=1
    atismiktari-=1
print("{} tane yazi\n{} tane tura gelmistir".format(yazi,tura))