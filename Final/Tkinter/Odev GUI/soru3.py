import tkinter as tk


def kayıtEt():

    s = ""
    s += ad_alan.get()+"\t\t"
    s += soyad_alan.get()+"\t\t\t"
    s += numara_alan.get()+"\n"
    print(text.get(tk.END))
    text.insert(tk.END, s)


register = tk.Tk()

register.config(pady=40, padx=15,)
ad = tk.Label(text="Ad :")
ad.grid(row=0, column=0, pady=5)
soyad = tk.Label(text="Soyad :")
soyad.grid(row=1, column=0, pady=5)
numara = tk.Label(text="Numara :")
numara.grid(row=2, column=0, pady=5)
ad_alan = tk.Entry()
ad_alan.grid(row=0, column=1, padx=10, pady=5)
soyad_alan = tk.Entry()
soyad_alan.grid(row=1, column=1, padx=10, pady=5)
numara_alan = tk.Entry()
numara_alan.grid(row=2, column=1, padx=10, pady=5)
button = tk.Button(text="Kayıt Et", border=3, padx=10, pady=4, command=kayıtEt)
button.grid(row=3, column=1, pady=10)
text = tk.Text(width=50, height=20)
text.grid(row=4, column=1, pady=10)
register.mainloop()
