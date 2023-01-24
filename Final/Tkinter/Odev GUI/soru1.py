import tkinter as tk
pencere = tk.Tk()
label = tk.Label(text="Welcome to the Python",
                 foreground="RED", background="yellow", pady=5, padx=3)
label.pack(fill=tk.X)
button = tk.Button(text="Click me", padx=10, pady=4,
                   foreground="white", background="black")
button.pack()

pencere.mainloop()
