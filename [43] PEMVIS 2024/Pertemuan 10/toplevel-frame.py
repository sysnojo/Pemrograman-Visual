from tkinter import *

root = Tk()
root.title("Root Window")
top = Toplevel()
top.title("Second Window")


# TextFrame root
text_frame = Frame(root)
text_frame.pack(side=TOP)
text = Text(text_frame, height=2, width=40)
text.insert(INSERT, "Hello World! ")
text.insert(END, "Goodbye World!")
text.pack()
text.tag_add("hello_text", "1.0", "1.5")
text.tag_add("world_text", "1.6", "1.12")
text.tag_add("goodbye_text", "1.13", "1.20")
text.tag_config("hello_text", background="yellow", foreground="green")
text.tag_config("world_text", background="green", foreground="white")
text.tag_config("goodbye_text", background="red", foreground="blue")

# TextFrame root
text_frame_2 = Frame(top)
text_frame_2.pack(side=TOP)
text_2 = Text(text_frame_2, height=2, width=40)
text_2.insert(INSERT, "Hello World! ")
text_2.insert(END, "Goodbye World!")
text_2.pack()
text_2.tag_add("hello_text_2", "1.0", "1.5")
text_2.tag_add("world_text_2", "1.6", "1.12")
text_2.tag_add("goodbye_text_2", "1.13", "1.20")
text_2.tag_config("hello_text_2", background="yellow", foreground="green")
text_2.tag_config("world_text_2", background="green", foreground="white")
text_2.tag_config("goodbye_text_2", background="red", foreground="blue")


top.mainloop()