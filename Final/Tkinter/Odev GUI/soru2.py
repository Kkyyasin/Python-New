import tkinter as tk


def buttonfonk():
    label.config(text=entry.get())


pencere = tk.Tk()
pencere.geometry("640x480")
pencere.title("Soru 2")
label = tk.Label(text="Yazı...",
                 padx=12, pady=4)
label.pack(pady=4)
entry = tk.Entry()
entry.pack(pady=4)
button = tk.Button(text="Yazı değiştir", background="black",
                   foreground="white", padx=6, pady=3, command=buttonfonk)
button.pack(pady=8)
pencere.mainloop()
