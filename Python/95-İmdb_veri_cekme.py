import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)

html_icerigi = response.content
soup = BeautifulSoup(html_icerigi, "html.parser")
liste = list()
for i, j in zip(soup.find_all("td", {"class": "titleColumn"}), soup.find_all("td", {"class": "ratingColumn imdbRating"})):
    a = i.text.split("\n")
    b = j.text.split("\n")
    liste.append([a[1], a[2], a[3], b[1]])
rating = float(input("Rating giriniz:"))
for i, j, k, z in liste:
    if float(z) >= rating:
        print(i, k, "\t\t\t", z)
        print(j)
        print("\n", "*"*50, "\n")
