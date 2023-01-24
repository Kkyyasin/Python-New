import sqlite3

# veri tabanına bağlanıyor yoksa oluşturuyor
con = sqlite3.connect("Kutuphane.db")
cursor = con.cursor()  # imlec olusturuyor kontrol için


def tablo_olustur():
    # CREATE TABLE Kutuphane (İsim TEXT,Yazar TEXT,Sayfa sayısı INT) if no exits yoksa oluşturuyor varsa üstüne yazıyor
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Kutuphane (İsim TEXT,Yazar TEXT,Sayfa_Sayısı INT)")
    con.commit()  # sqlite yeniliyor veriyi gonderiyor


tablo_olustur()
con.close()  # veri tabanına bağlantıyı kesiyor
