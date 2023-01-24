import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()

window2 = tk.Tk()

frame4 = tk.Frame(master=window2, width=200, height=100, bg="red")
frame4.pack(fill=tk.Y, side=tk.LEFT)

frame5 = tk.Frame(master=window2, width=100, bg="yellow")
frame5.pack(fill=tk.Y, side=tk.LEFT)  # fill y ye gore uzatır

frame6 = tk.Frame(master=window2, width=50, bg="blue")
frame6.pack(fill=tk.Y, side=tk.LEFT)  # side konumun belirler float html gibi
window3 = tk.Tk()

frame7 = tk.Frame(master=window3, width=200, height=100, bg="red")
# expand pencere uyumlu buyumesi
frame7.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame8 = tk.Frame(master=window3, width=100, bg="yellow")
frame8.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame9 = tk.Frame(master=window3, width=50, bg="blue")
frame9.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window3.mainloop()
window2.mainloop()
window.mainloop()
