from tkinter import *

# root frame
root = Tk()
root.geometry("800x600")

# ScrollFrame
scroll_frame = Frame(root)
scroll_frame.pack(side=TOP)
scrollbar = Scrollbar(scroll_frame)
scrollbar.pack(side=RIGHT, fill=Y)

lang_list = ('C', 'C++', 'C#', 'Python', 'Javascript', 'Java', 'SQL', 'PHP', 'HTML', 'CSS', 'Assembly')

show_list = Listbox(scroll_frame, yscrollcommand = scrollbar.set )
for idx in range(len(lang_list)):
   show_list.insert(END, "This is " + lang_list[idx] + " Language")
   
show_list.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = show_list.yview )

# TextFrame
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

# SpinboxFrame 
spinbox_frame = Frame(root)
spinbox_frame.pack(side=TOP)
w = Spinbox(spinbox_frame, from_=10, to=100)
w.pack()

# Labelframe
labelframe = LabelFrame(root, text="Hello my name is John, today is sunny!")
labelframe.pack(fill="both", expand="yes")
left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

# mainloop
mainloop()