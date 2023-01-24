from  tkinter import *
#Create Window:
new_window = Tk()
new_window.title("Hello World")
new_window.geometry("300x250")
#Adding the background color:
new_window.config(bg = "red")

#new_window tells us that we are setting up something for the new window
#.config() means that we want to configure something on the screen
#bg tells that the background needs to be changed
#"red" tells us what should the background color be ; it can also be a hex code

new_window.mainloop()