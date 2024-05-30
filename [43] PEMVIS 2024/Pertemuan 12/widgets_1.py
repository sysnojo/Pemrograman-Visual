import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Widgets 1 (Button - Label)")
root.geometry("800x600")

def show_message():
    messagebox.showinfo("Halo Selamat Pagi!")

# Button
btn = tk.Button(root, text="Click Me!", command=show_message)
btn.pack()

# Canvas
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.create_line(0, 0, 200, 100)
canvas.create_oval(50, 20, 150, 80, fill="blue")
canvas.pack()

# Checkbutton
chk_var1 = tk.IntVar()
chk_var2 = tk.IntVar()
chk1 = tk.Checkbutton(root, text="Discipline", variable=chk_var1)
chk2 = tk.Checkbutton(root, text="Smart", variable=chk_var2)
chk1.pack()
chk2.pack()

# Entry
entry = tk.Entry(root)
entry.pack()

# Frame
frame = tk.Frame(root, bg="lightgrey", bd=2, relief=tk.SUNKEN)
frame.pack(pady=10)
tk.Label(frame, text="Inside Frame").pack()

# Label
label = tk.Label(root, text="Created by John", fg="blue")
label.pack()

root.mainloop()