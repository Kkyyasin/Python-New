
def Permutasyon(s, konum):
    print(s[konum], end="")
    for i in s:
        if not (i == s[konum]):
            print(i, end="")
    print(end=" ")
    if konum == len(s)-1:
        return
    else:
        Permutasyon(s, konum+1)


def Permutasyon2(s, konum):
    print(s[konum], end="")
    for i in s:
        if not (i == s[konum]):
            print(i, end="")
    print(end=" ")
    print(s[konum], end="")
    for i in range(len(s)-1, -1, -1):
        if not (s[i] == s[konum]):
            print(s[i], end="")
    print(end=" ")
    if konum == len(s)-1:
        return
    else:
        Permutasyon2(s, konum+1)


Permutasyon("XYZ", 0)
print()
Permutasyon2("XYZ", 0)
