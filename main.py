# Temp Converter

import tkinter as tk
from tkinter import LabelFrame, Button, Entry, END, messagebox

root = tk.Tk()

# Size of display:
root.geometry("1000x500")
root.title("Temperature-converter")

# Background color of display:
root.configure(bg='grey')

convert = ""
Answer = ""


# Calculation

def enable_ctf():
    entry1.config(state="normal")
    entry1.delete(0, END)

    entry2.config(state="normal")
    entry3.delete(0, END)
    entry3.config(state="readonly")

    entry3.config(state="normal")
    entry2.delete(0, END)
    entry2.config(state="readonly")

    global convert
    convert = "ctf"


def enable_ftc():
    entry2.config(state="normal")
    entry2.delete(0, END)

    entry3.config(state="normal")
    entry3.delete(0, END)
    entry3.config(state="readonly")

    entry1.config(state="normal")
    entry1.delete(0, END)
    entry1.config(state="readonly")

    global convert
    convert = "ftc"


def cal():
    try:
        global convert
        if convert == "ctf":
            temp = float(entry1.get())
            Answer = str(temp * 9 / 5 + 32)
            entry3.config(state="normal")
            entry3.delete(0, END)
            entry3.insert(0, Answer)
            entry3.config(state="readonly")
        elif convert == "ftc":
            temp = float(entry2.get())
            Answer = str((temp - 32) * 5 / 9)
            entry3.config(state="normal")
            entry3.delete(0, END)
            entry3.insert(0, Answer)
            entry3.config(state="readonly")

    except ValueError as ex:
        entry1.config(state="normal")
        entry1.delete(0, END)
        entry1.config(state="readonly")

        entry2.config(state="normal")
        entry2.delete(0, END)
        entry2.config(state="readonly")

        messagebox.showerror("Error", "Please Enter a number")


def clear():
    entry1.config(state="normal")
    entry1.delete(0, END)
    entry1.config(state="readonly")

    entry2.config(state="normal")
    entry2.delete(0, END)
    entry2.config(state="readonly")

    entry3.config(state="normal")
    entry3.delete(0, END)
    entry3.config(state="readonly")


# Creating Labels
label1 = LabelFrame(root, text="Celsius to Fahrenheit", bg="white")
label2 = LabelFrame(root, text="Fahrenheit to Celsius", bg="white")
# Buttons
b1 = Button(root, text="Activate - Celsius to Fahrenheit", command=enable_ctf, bg="yellow")
b2 = Button(root, text="Activate - Fahrenheit to Celsius", command=enable_ftc, bg="yellow")
b3 = Button(root, text="Calculate Conversion", command=cal, bg="green")
b4 = Button(root, text="Clear", command=clear, bg="orange")
b5 = Button(root, text="Exit ", command=exit, bg="red")





# Label placement and size
label1.place(x=150, y=50, width=300, height=200)
label2.place(x=550, y=50, width=300, height=200)

# Placement of entry
entry1 = Entry(label1, state="readonly")
entry1.place(x=50, y=50, width=180, height=30)
entry2 = Entry(label2, state="readonly")
entry2.place(x=50, y=50, width=180, height=30)
entry3 = Entry(root)
entry3.place(x=400, y=350, width=180, height=30)

# Placement of buttons
b1.place(x=200, y=280, width=230)
b2.place(x=600, y=280)
b3.place(x=100, y=350)
b4.place(x=700, y=350)
b5.place(x=800, y=350)

root.mainloop()
