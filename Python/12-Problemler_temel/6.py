"""
Problem 6
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2"""
a = int(input("1-dik kenar"))
b = int(input("2-dik kenar"))
c = (a**2+b**2)**0.5
print("Hipetonüs", c)
