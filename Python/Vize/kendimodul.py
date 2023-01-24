sözlük = {"kitap": "book",
          "bilgisayar": "computer",
          "programlama": "programming"}


def ara(anahtar):
    print(sözlük.get(anahtar, "Bulunmuyor"))
