from random import random
from tkinter import *
import random
def generate():
    n=random.randint(0,1000)
    label.config(text=n)

root = Tk()
root.title("Generate random number")
root.geometry("200x200")
label = Label(text="-")
label.pack()
button = Button(text="Generate", command=generate)
button.pack()

root.mainloop()
