# hem ikiye hem hem uce bolunebilen sayilari liste objesinde tutma
sayilar = list()
for i in range(1, 100000):
    if i % 2 == 0 and i % 3 == 0:
        sayilar.append(i)
# list compersinle ile
sayilar1 = [x for x in range(1, 100000) if x % 2 == 0 and x % 3 == 0]
if sayilar1 == sayilar:
    print("esit")
kisiler = ["mustafa", "merve", "yasin"]
m_baslayan = [x for x in kisiler if x[0] == "m"]
print(m_baslayan)
