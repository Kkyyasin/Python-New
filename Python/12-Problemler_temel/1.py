"""
    Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
    """
s1 = int(input("Birinci sayıyı giriniz:"))
s2 = int(input("ikinci sayıyı giriniz:"))
s3 = int(input("Üçüncü sayıyı giriniz:"))
print("{}*{}*{}={}".format(s1, s2, s3, s1*s2*s3))
