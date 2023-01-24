# decaroter
import re


def yaziyazdır(fonk):
    def yıldızla():
        print("-------___-------")
        fonk()
    return yıldızla


@yaziyazdır
def yazi():
    print("merhaba")


yazi()


def topla(fonk):
    return 5+fonk


@topla
def toplam():
    return 5


toplam()
