import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Widgets 3 (Scrollbar - tkMessageBox)")
root.geometry("800x600")

def show_message():
    messagebox.showinfo("Halo Selamat Pagi!")

# Scrollbar and Text
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(root, wrap=tk.NONE, yscrollcommand=scrollbar.set)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=text.yview)

# Toplevel
top = tk.Toplevel()
top.title("Toplevel Window")
tk.Label(top, text="This is a toplevel window").pack()

# Spinbox
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# PanedWindow
paned_window = tk.PanedWindow(root)
left = tk.Label(paned_window, text="Left Pane")
paned_window.add(left)
right = tk.Label(paned_window, text="Right Pane")
paned_window.add(right)
paned_window.pack(fill=tk.BOTH, expand=True)

# LabelFrame
label_frame = tk.LabelFrame(root, text="LabelFrame", padx=10, pady=10)
label_frame.pack(padx=10, pady=10)
tk.Label(label_frame, text="Inside LabelFrame").pack()

# tkMessageBox
tk.Button(root, text="Hello THere!", command=show_message).pack()

root.mainloop()