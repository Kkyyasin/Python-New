"""Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın."""
liste = ["345", "sadas", "324a", "14", "kemal"]
for i in liste:
    try:
        print(int(i))
    except ValueError:
        pass
