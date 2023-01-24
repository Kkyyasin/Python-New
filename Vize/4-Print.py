print("Merhaba")  # 3 dekilde de tanılanbilir
print('Merhaba')
print("""
      Merhaba""")
print('Yasin\'in de notlar')  # Kacıs bitit aynı tırnak kullanırsa konur
print("""
[H]=========HARMAN========[-][o][x]
|                                 |
|     Programa Hoşgeldiniz!       |
|           Sürüm 0.8             |
|    Devam etmek için herhangi    |
|       bir düğmeye basın.        |
|                                 |
|=================================|
""")  # 3 tırnakla boyle kullanım olabilir
# print paremetreler
# sep
# virguller arası ne olacağına karar verir default boslukur
print("Merhaba", "Yasin")
print("Merhaba", "Yasin", sep="-")
print("bir", "iki", "üç", "dört", "on dört", sep=" " + "mumdur" + " ")
# end print in sonda ne yapacağına karar verir default \n dir
print("TBMM", end=".\n")
print("Yasin", end="")
print("Mhem")
print(*"YAsin", sep="-")  # indis indis ayırır
a = 5
print("{} yazdırıldı".format(a))  # boylede yapılabilri
