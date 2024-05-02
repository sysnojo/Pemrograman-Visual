from tkinter import *

root = Tk()
root.title("Main Window")

m1 = PanedWindow(bg="lightblue")  # Set background color
m1.pack(fill=BOTH, expand=1)

left = Entry(m1, bd=5)
right = Entry(m1, bd=5)
up = Entry(m1, bd=5)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL, bg="lightgreen")
m1.add(m2)

top = Scale(m2, orient=HORIZONTAL)
m2.add(top)

# Custom button text
bottom = Button(m2, text="Click Me!", bg="orange")
m2.add(bottom)

root.mainloop()
