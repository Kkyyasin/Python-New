"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
s1 = int(input("1-sayıyı giriniz:"))
s2 = int(input("2-sayıyı giriniz:"))
s3 = int(input("3-sayıyı giriniz:"))
if s1 > s2:
    if s1 > s3:
        print(s1)
    else:
        print(s3)
else:
    if s3 > s2:
        print(s3)
    else:
        print(s2)
