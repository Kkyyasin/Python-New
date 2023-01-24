import tkinter as tk
pencere = tk.Tk()
pencere.title("Test")
pencere.geometry("400x200")
button = tk.Button(pencere, text="Test",
                   foreground="red", background="yellow", padx=16, pady=6)
button.pack(side="bottom")
pencere2 = tk.Tk()
pencere2.title("Test 2")
pencere2.geometry("200x400")
pencere.mainloop()
pencere2.mainloop()
