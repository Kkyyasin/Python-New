import sqlite3

con = sqlite3.connect("Kutuphane.db")
cursor = con.cursor()


def verileri_al():
    cursor.execute("SELECT * FROM Kutuphane")  # 1 yontem
    liste = cursor.fetchall()
    for i in liste:
        print(i)


def isimleri_al():
    cursor.execute("SELECT İsim FROM Kutuphane")
    liste = cursor.fetchall()
    for i in liste:
        print(i)


isimleri_al()


def belli_ozellikte_al():
    # if kosulu gibi belli kosulu gibi
    cursor.execute("SELECT * FROM Kutuphane where Yazar='ss'")
    liste = cursor.fetchall()
    for i in liste:
        print(i)


belli_ozellikte_al()
verileri_al()
