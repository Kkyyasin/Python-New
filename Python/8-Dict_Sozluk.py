sözlük1 = {"bir": 1, "iki": 2, 3: "elma"}
print(sözlük1)
print(type(sözlük1))
print(sözlük1["bir"])
a = {"bir": [1, 2, 3], 2: [4, 5, 5]}
print(a["bir"][0])
print(a[2])
print(sözlük1.keys())  # anahtarları alır
print(sözlük1.values())  # cevapları alır
print(sözlük1.items())  # her bir elemanı demtler alır
for i, j in sözlük1.items():
    print(i, j)
