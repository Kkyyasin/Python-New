"""Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın."""
km_litre = float(input("Aracınız Kilometre ne kadar yakıt harcıyor"))
km = float(input("Kaç kilometre yol Yaptınız"))
fiyat = km_litre*km
print("Ödemeniz gereken miktar :", fiyat)
