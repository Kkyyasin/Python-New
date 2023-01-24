import tkinter as tk
pencere = tk.Tk()
pencere.geometry("1080x920")
# Label yazı alanı
label = tk.Label(pencere, text="Yazı...", foreground="red",
                 background="#84A2FE", width=20, height=8)
label.pack(pady=10)

# entry textfield demek
entry = tk.Entry(width=60, foreground="#44A514", background="blue", border=3)
entry.pack(pady=10)
# Text box
text_box = tk.Text(width=60, height=20)
text_box.pack(pady=10)
# button
button = tk.Button(width=40, height=4, background="black",
                   text="ok", fg="white")
button.pack()

pencere2 = tk.Tk()
pencere2.geometry("640x480")
frame1 = tk.Frame(pencere2, width=200, height=400, background="red")
frame1.pack()
label3 = tk.Label(master=frame1, text="frame1", font=18)
label3.pack()
pencere.mainloop()
pencere2.mainloop()
