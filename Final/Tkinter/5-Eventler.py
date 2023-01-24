import tkinter as tk


def arttir():
    value = int(lbl_value["text"])+1
    lbl_value["text"] = str(value)


def azalt():
    value = int(lbl_value["text"])-1
    lbl_value["text"] = str(value)


window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
# sutunların boyutunu ayarlar
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=azalt)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=arttir)
btn_increase.grid(row=0, column=2, sticky="nsew")  # tikcy konumu belirtir
""""n"veya"N" hücrenin üst orta kısmına hizalamak için
"e"veya"E" hücrenin sağ orta tarafına hizalamak için
"s"veya"S" hücrenin alt orta kısmına hizalamak için
"w"veya"W" hücrenin sol orta tarafına hizalamak için"""
# birleşmin egore faklı sonuçlar çıkar
# https://realpython-com.translate.goog/python-gui-tkinter/?_x_tr_sl=en&_x_tr_tl=tr&_x_tr_hl=tr&_x_tr_pto=sc

window.mainloop()
