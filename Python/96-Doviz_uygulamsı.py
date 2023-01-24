from urllib import response
import requests
url = "https://finans.truncgil.com/today.json"
response = requests.get(url)
print(response)
json_file = response.json()
print(json_file)
while True:
    secim = input("""
                1-Alış
                2-Satış
                3-Çıkış
                """)
    if secim == "3":
        break
    elif secim == "1":
        sec = input("""
                  1-Dolar
                  2-Euro
                  3-Çıkış""")
        if sec == "3":
            break

        elif sec == "1":
            mik = float(input("Miktar giriniz:"))
            a = float(json_file["USD"]["Alış"])
            print("Tutar:", str(mik*a))
        elif sec == "2":
            mik = float(input("Miktar giriniz:"))
            a = float(json_file["EUR"]["Alış"])
            print("Tutar:", mik*a)

    elif secim == "2":
        sec = input("""
                  1-Dolar
                  2-Euro
                  3-Çıkış""")
        if sec == "3":
            break
        elif sec == "1":
            mik = float(input("Miktar giriniz:"))
            a = float(json_file["USD"]["Satış"])
            print("Tutar:", mik*a)
        elif sec == "2":
            mik = float(input("Miktar giriniz:"))
            a = float(json_file["EUR"]["Satış"])
            print("Tutar:", mik*a)

    else:
        print("Hatalı kodlama...")
