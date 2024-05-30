import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Widgets 2 (Listbox - Scale)")
root.geometry("800x600")

# Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Taekwondo")
listbox.insert(2, "Archering")
listbox.insert(3, "Polo")
listbox.pack()

# Menubutton and Menu
menu_button = tk.Menubutton(root, text="Pick a color!", relief=tk.RAISED)
menu_button.menu = tk.Menu(menu_button, tearoff=0)
menu_button["menu"] = menu_button.menu
menu_button.menu.add_checkbutton(label="Blue")
menu_button.menu.add_checkbutton(label="Red")
menu_button.pack()

# Message
message = tk.Message(root, text="Hello there!", width=200)
message.pack()

# Radiobutton
radio_var = tk.IntVar()
radio1 = tk.Radiobutton(root, text="Male", variable=radio_var, value=1)
radio2 = tk.Radiobutton(root, text="Female", variable=radio_var, value=2)
radio1.pack()
radio2.pack()

# Scale
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

root.mainloop()