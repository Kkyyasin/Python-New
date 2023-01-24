# 3 un kuvvetleri
class Kuvvet3():
    def __init__(self, max=0):
        self.max = max
        self.kuvvet = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.kuvvet <= self.max:
            sonuc = 3**self.kuvvet
            self.kuvvet += 1
            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration


kuvvet = Kuvvet3(10)
for i in kuvvet:
    print(i, end="   ")
# fibonnaci generator


def fibonacci():
    a = 1
    b = 1
    yield a
    yield b
    while True:
        a, b = b, a+b

        yield b  # sayı istediğimiz kadar olusmamızı saglar


for i in fibonacci():
    if i > 1000:
        break
    print(i)
