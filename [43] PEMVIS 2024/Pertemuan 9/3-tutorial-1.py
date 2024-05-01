import tkinter as tk
from tkinter import messagebox, Button, Checkbutton, Label, Entry, IntVar

# Frame
frame = tk.Tk()
frame.geometry("700x700")

# Button
def helloCallBack():
    msg = messagebox.askquestion("Greet", "Are You Feeling Good Today?")
def secretCallBack():
    msg = messagebox.showinfo("Secret", "A lobster blood is always blue....")
def tipCallBack():
    msg = messagebox.showinfo("Tip", "Impossible is nothing.")

B = Button(frame, font=15, text="Click Me!", command=helloCallBack, background='green', foreground='white')
C = Button(frame, font=15, text="Click for a Secret!", command=secretCallBack, background='red', foreground='white')
D = Button(frame, font=15, text="Click for a Tip!", command=tipCallBack, background='black', foreground='white')
B.place(x=50, y=50)
C.place(x=150, y=50)
D.place(x=300, y=50)

# Checkbox (Checkbutton)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(frame, text="Orange", variable=CheckVar1, onvalue=1, offvalue=0, height=3, bd=5, foreground="orange", font=15)
C2 = Checkbutton(frame, text="Biru", variable=CheckVar2, onvalue=1, offvalue=0, height=3, bd=5, foreground="blue", font=15)
C1.place(x=50, y=300)
C2.place(x=150, y=300)

# Label
L1 = Label(frame, text="Nama Anda Siapa?", font=20)
L2 = Label(frame, text="Mobil Anda Warna Apa?", font=20)
L1.place(x=50, y=200)
L2.place(x=50, y= 300)

# Entry
E1 = Entry(frame, bd=5, font=20, background='green', foreground='white')
E1.place(x=200, y=200)

frame.mainloop()