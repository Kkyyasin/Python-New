from urllib import response
from matplotlib.pyplot import text
import requests  # İnternetten veri cekmemizi yarar
from bs4 import BeautifulSoup  # Daha guzel gorunmesini sağşallr
url = "https://www.sabihagokcen.aero/yolcu-ve-ziyaretciler/ucus-bilgi-ekrani"
response = requests.get(url)  # veriyi ceker
print(response)  # <Response [200]> bu bilgiler çekildiği anlamına geliyor
html_icerigi = response.content
# print(html_icerigi)    #?html icerini yazdırır
# html parçalanır daha guzel gozukmesi saplanır
soup = BeautifulSoup(html_icerigi, "html.parser")
# print(soup) #?Daha guzel yazdırı ama fazla oduğu için yorum satırı
# print(soup.prettify)   #*Buda aynı işi yapar
# print(soup.text) #*sadece text yazar
"""for i in soup.find_all("a"):#*liste halinde a etiketlerini alır
    print(i.text)#*a etiketleri içindeki yazılarrı alır
    print(i)#*a etiketi alır
    print(i.get("href"))#*sadece href ozelligini alır class ta olabilir mesela
    print("*"*30)
"""
print(soup.find("a"))  # *tek alır

# boyle class idd vs girilebilir
for i in soup.find_all("table", {"class": "feedtable"}):

    if i.text.find("PEGASUS") != -1:
        print(i.text)
