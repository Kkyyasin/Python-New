while True:
    işlem = input("""
                Fibonacci Bulma Programı
                
    1-Fibonacci bul
    2-Çıkış

Şeçim:""")
    if işlem == "1":

        b = 1
        a = 1
        fibonacci = [a, b]
        for i in range(10):
            a, b = b, a+b
            fibonacci.append(b)
        print(fibonacci)
