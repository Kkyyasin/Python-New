import tkinter as tk

window = tk.Tk()


def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)


def handle_click(event):
    print("The button was clicked!")


def handler_mouseclick(event):
    print("The Mouse was clicked!")


button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)  # hanle kodları var ona gore mouse
button.pack()
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)
window.bind("<Button-1>", handler_mouseclick)  # mouseun sol tusu

window.mainloop()
