import tkinter as tk
from tkinter import PhotoImage

def on_closing():
    root.destroy()

root = tk.Tk()
root.title("Tkinter Widgets Canvas 1-2")
root.geometry("800x600")

# Membuat widget Canvas
canvas = tk.Canvas(root, bd=5, bg="lightgrey", confine=True, cursor="circle",
                   height=400, relief=tk.RIDGE, scrollregion=(0, 0, 500, 500),
                   width=600, xscrollincrement=10, yscrollincrement=10)
canvas.pack()

# Scrollbar horizontal dan vertikal
h_scroll = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
v_scroll = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Mengkonfigurasi scrollbar untuk canvas
canvas.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

# Membuat arc
canvas.create_arc(10, 50, 240, 210, start=0, extent=150, fill="blue")

# Membuat garis
canvas.create_line(10, 10, 200, 200, fill="red", width=3)

# Membuat oval (lingkaran)
canvas.create_oval(250, 50, 350, 150, fill="green")

# Membuat polygon (segitiga)
canvas.create_polygon(400, 10, 480, 100, 320, 100, fill="yellow", outline="black")

try:
    image = PhotoImage(file="sunshine.gif")
    canvas.create_image(50, 50, anchor=tk.NE, image=image)
except Exception as e:
    print("Image not found: ", e)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()