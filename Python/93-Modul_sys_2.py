import sys
# ?Kok bulma


def kok_bulma(a, b, c):
    delta = ((b**2)-4*a*c)
    if (delta < 0):
        sys.stdout.write("Kok yoktur\n.")
        sys.stdout.flush()
    else:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        return (x1, x2)


if len(sys.argv) == 4:  # dosya adı,a,b,c
    print("Kok Bulma", kok_bulma(
        int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))  # !String alır terminalden cevirmek lazım
else:
    sys.stderr.write("eleman sayısı yanlış")
    sys.stderr.flush()
"""PS C:\Users\User\Desktop\pyhton\Python> python 93-Modul_sys_2.py 1 -2 1
Kok Bulma (1.0, 1.0)
PS C:\Users\User\Desktop\pyhton\Python> """
