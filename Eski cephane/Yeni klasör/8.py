#tuple veri tipi
a=(1,2,3,"ahmet")#liste gibi ama değiştirilemez
print(a)
yazi="merhaba"
yazi=tuple(yazi)#string tupple a dönüşür
yeni=(1,2,3,"merhaba","yasin","yasin","yasin")
print("{} indiste bulunur ".format(str(yeni.index("merhaba"))))#index sayisin gösterir hangisinde olduğunu
print(yeni.count("yasin"))#tuple kaç tane bulunduğu sayisini gösterir eleman
print(yeni.__contains__("merhaba"))#girilen değerin varlığını kontrol eder
print(yeni.__contains__("ahmet"))
a=yeni.count(4)
print(a)