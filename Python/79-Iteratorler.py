# Iterator
from pytest import raises


liste = [1, 2, 3, 4]  # liste bir iterotordur
# iterotor listede ilerlememiz saglar
iterator = iter(liste)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) eleman biter StopIteration hatası alınır
liste1 = [1, 2, 3, 4, 8, 6, 7, 8, 9]
for i in liste1:
    print(i, end="  ")  # for dongusu iteretor gibi davranıyor
ite1 = iter(liste1)
print()
while True:
    try:
        print(next(ite1), end="  ")
    except StopIteration:
        break


class Kumanda():
    def __init__(self, kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1

    def __iter__(self):
        return self  # iter objesi yapıyoz

    def __next__(self):
        self.index += 1
        if self.index < len(self.kanal_listesi):
            return self.kanal_listesi[self.index]  # kanallarda geziniyoz
        else:
            self.index = -1
            raise StopIteration  # hata gonderiyoz


kumanda = Kumanda(["Atv", "Star", "Fox"])
ite2 = iter(kumanda)  # iter ozelligi alır
print()
while True:
    try:
        print(next(ite2))
    except StopIteration:
        break
for i in ite2:
    print(i)  # iter ozelligi dongulerde dolasmamızı yazar
