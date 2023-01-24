note = float(input("Notunuzu giriniz:"))
if note > 100 or note < 0:
    print("gecersiz note")
elif note >= 90:
    print("AA")
elif note >= 75:
    print("BA")
elif note >= 60:
    print("BB")
elif note >= 40:
    print("CC")
elif note >= 25:
    print("DD")

else:
    print("FF")
