from logging import exception
from random import random
from tkinter import *
import random
from tkinter.ttk import Combobox

def GetValueOfException():
    try:
        exception_entry = int(new_exception_entry.get())
        return exception_entry
    except ValueError:
        label.config(text="Error: Invalid input in exception field")
        return None

def generate():
    ex=GetValueOfException()

    try:
        min_num = int(minCombobox.get())
        max_num = int(maxCombobox.get())
        if min_num < max_num:
            n = random.randint(min_num, max_num)
            if ex == n:
                label.config(text="Error: number = exception number")
            else:
                label.config(text=f"Generated: {n}")
        else:
            label.config(text="Error: min >= max")
    except ValueError:
        label.config(text="Error: Invalid input")

def clear_placeholder(event):
    if new_exception_entry.get() == "Exception number: ":
        new_exception_entry.delete(0, "end")


root = Tk()
root.title("Generate Random Number")
root.geometry("250x250")

label = Label(root, text="-")
label.pack(pady=10)

minCombobox = Combobox(root, values=[str(i) for i in range(1, 101)], width=10)
minCombobox.set("1")
minCombobox.pack(pady=5)

maxCombobox = Combobox(root, values=[str(i) for i in range(1, 101)], width=10)
maxCombobox.set("100")
maxCombobox.pack(pady=5)

button = Button(root, text="Generate", command=generate)
button.pack(pady=10)

new_exception_entry = Entry(root, width=30)
new_exception_entry.insert(0, "Exception number: ")
new_exception_entry.bind("<FocusIn>", clear_placeholder)
new_exception_entry.pack(pady=10)

root.mainloop()