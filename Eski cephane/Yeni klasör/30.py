dosya=open("planlar1.txt","w",encoding="utf-8")#w -ustrune yazar
dosya.write("merhhaba")
dosya.writelines(["mehvaba\n","ıoecj\n"])#lineslerde liste girilmeli
with open("planlar1.txt","w") as dosya:#aynı nlama gelir
    dosya.write("merhaba\n")
with open("planlar3.txt","a")as d:#ustune yazar
    d.writelines(["öeha\n","okxkox\n","cdmd\n"])
dosya.close()
d.close()