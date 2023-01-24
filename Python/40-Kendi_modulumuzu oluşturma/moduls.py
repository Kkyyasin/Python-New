programlama_dilleri = ["C", "Java", "Python", "Javascript", "C++"]


def toplama(*a):
    t = 0
    for i in a:
        t += i
    """
    Bu fonksiyon istedğimiz kadar değrei toplar döndürür
    """
    return t


def selamla():
    print("""
********************************
*   ************************   *
*      Merhaba Hoşgeldiniz     *
*   ************************   *   
******************************""")
    """Bu fonksiyon insanları selamlar
    """
