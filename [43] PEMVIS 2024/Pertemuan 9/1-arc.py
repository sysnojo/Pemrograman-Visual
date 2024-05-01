import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, bg='blue', height=550, width=550)

coord = 10, 50, 240, 240
coord2 = 10, 390, 200, 200
coord3 = 600, 50, 400, 400

arc = C.create_arc(coord, start=0, extent=250, fill='red')
arc2 = C.create_arc(coord2, start=120, extent=250, fill='green')
arc3 = C.create_arc(coord3, start=90, extent = 110, fill='yellow')

C.pack()
top.mainloop()