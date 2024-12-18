from random import random
from tkinter import *
import random
from tkinter.ttk import Combobox


def generate():
    minNum = int(minCombobox.get())
    maxNum = int(maxCombobox.get())
    if minNum<maxNum:
        n=random.randint(minNum,maxNum)
        label.config(text=n)
    else:
        label.config(text="Error")

root = Tk()
root.title("Generate random number")
root.geometry("200x200")
label = Label(text="-")
label.pack()
minCombobox=Combobox(root,values=[str(i) for i in range(1,101)])
minCombobox.set("1")
minCombobox.pack()
maxCombobox=Combobox(root,values=[str(i) for i in range(1,101)])
maxCombobox.set("100")
maxCombobox.pack()
button = Button(text="Generate", command=generate)
button.pack()

root.mainloop()
