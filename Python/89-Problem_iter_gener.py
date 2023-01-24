""""Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın."""


class Kareler():
    def __init__(self, max=0):
        self.max = max
        self.sayi = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi <= self.max:
            sonuc = self.sayi**2
            self.sayi += 1
            return sonuc
        else:
            self.sayi = 0
            raise StopIteration


kare = Kareler(10)
for i in kare:
    print(i, end="   ")

"""1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın.
"""


def asal_mı(sayi):
    for i in range(2, (sayi//2)+1):
        if sayi % i == 0:
            return False
    return True


def asal_generator(sayi):
    for i in range(1, sayi):
        if asal_mı(i):
            yield i


g = asal_generator(1000)
print(g)
ite = iter(g)
print(next(ite))
for i in ite:
    print(i, end="   ")
