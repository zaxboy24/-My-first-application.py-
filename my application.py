import tkColorChooser as tkColorChooser
import tkFont as tkFont
from Tkinter import *
import tkMessageBox as tkm

def helloCallBack():
    import __init__
def Vorgzy():
    root.destroy()

root = Tk()
root.title("My App")
root.geometry("500x300")

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
root.geometry("+{}+{}".format(x, y))


TopLabel = Label(root, text = "Hi Vorgz", bg = "grey", bd = 1 , relief = SUNKEN, height = 1, font = "System 16 bold" , fg = "red")
TopLabel.pack(fill = X)

Topframe1 = Frame(root, bg = "white")
Topframe1.pack(side = TOP, fill = X)

Topframe2 = Frame(root, bg = 'white')
Topframe2.pack(side = TOP, fill = X)

Topframe3 = Frame(root,bd = 1)
Topframe3.pack(side = TOP)

TopLabel2 = Label(Topframe2, text = "--------What can I Show you---------", bg = "White", bd = 1 , relief = SUNKEN, height = 3, font = "System 16 bold" , fg = "Black")
TopLabel2.pack(fill = X)

TopLabel3 = Label(Topframe3, text = "Click Go to Proceed Data Structure", bd = 1 , relief = SUNKEN, height = 3, bg = 'white', font = "System 14 italic" , underline = 6, fg = "black")
TopLabel3.pack()

b1 = Button(Topframe3, text = "Go", bg = "green", bd = 1, fg = "white", justify = CENTER, font = "Default 15 bold", width = 6, height = 2, command = helloCallBack)
b1.pack()
b2 = Button(Topframe3, text = "Exit", bg = "red", bd = 1, fg = "White",font = "Default 15 bold",width = 6, height = 2, command = Vorgzy)
b2.pack(side = BOTTOM)

root.mainloop()