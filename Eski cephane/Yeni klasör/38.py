from os import *
#https://python-istihza.yazbel.com/standart_moduller/os.html os modulu windows klosore ayarları için

def delete_files():

    sliste = [".aaa", ".bbc", ".asw"]
    for f in listdir():
     a=f[len(f)-4:]
     print(a)
     if sliste.__contains__(a):
         remove(f)

delete_files()
