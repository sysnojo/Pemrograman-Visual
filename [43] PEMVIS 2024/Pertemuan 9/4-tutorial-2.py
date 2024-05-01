import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("800x600")

# Main Frame
frame = Frame(root, background='gray', width=800, height=600)
frame.pack()

# Listbox
langs = ('Java', 'C#', 'C', 'C++', 'Javascript', 'HTML', 'PHP', "Python", "Golang")
var = Variable(value=langs)

lbFrame = Frame(frame)
lbFrame.pack(side=LEFT)
Lb1 = Listbox(lbFrame, font=12, background='green', foreground='white', bd=3, listvariable=var, selectmode=tk.EXTENDED, height=6)
Lb1.pack(expand=True, fill=tk.BOTH)

scrollbar = Scrollbar(
    lbFrame,
    orient=tk.VERTICAL,
    command=Lb1.yview
)
Lb1['yscrollcommand'] = scrollbar.set
scrollbar.pack(side=tk.RIGHT, expand=True, fill=tk.Y)

# Menu button
mbFrame = Frame(frame)
mbFrame.pack()
mb= Menubutton (mbFrame, text="Difficulty", relief=RAISED, width=15)
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu

easyVar = IntVar()
mediumVar = IntVar()
hardVar = IntVar()
mb.menu.add_checkbutton (label="Easy", variable=easyVar)
mb.menu.add_checkbutton (label="Medium", variable=mediumVar)
mb.menu.add_checkbutton (label="Hard", variable=hardVar)
mb.pack()

# Menu
# Filemenu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")
menubar.add_cascade(label="File", menu=filemenu)
# Editmenu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")
menubar.add_cascade(label="Edit", menu=editmenu)
# Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

# Message
var = StringVar()
labelMsg = Message(frame, textvariable=var, relief=RAISED)
var.set("How's it going on? How's Your Day? Do you have a friend?")
labelMsg.pack(side=BOTTOM)

# RadioButton
varVar = IntVar()
def selected():
    label.config(text="You selected " + str(varVar.get()))
R1 = Radiobutton(root, text="Banana", variable=varVar, value=1, command=selected)
R1.pack()
R2 = Radiobutton(root, text="Apple", variable=varVar, value=2, command=selected)
R2.pack()
R3 = Radiobutton(root, text="Orange", variable=varVar, value=3, command=selected)
R3.pack()
label = Label(root)
label.pack()

# Scale
def sel():
    labelScale.config(text="Value = " + str(dvar.get()))

dvar = DoubleVar()
scale = Scale(root, variable=dvar)
scale.pack(anchor=CENTER)

buttonScale = Button(root, text="Get Scale Value", command=sel)
buttonScale.pack(anchor=CENTER)
labelScale = Label(root)
labelScale.pack()

root.mainloop()
