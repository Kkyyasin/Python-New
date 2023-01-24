import tkinter as tk

window = tk.Tk()
window.geometry("800x600")
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()
# solo üst kose koordinatla rgirilir
label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

label3 = tk.Label(master=frame, text="I'm at (120, 20)")
label3.place(x=60, y=20)


window.mainloop()
window2 = tk.Tk()

for i in range(3):
    window2.columnconfigure(i, weight=1, minsize=75)
    window2.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window2,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window2.mainloop()
window.mainloop()
