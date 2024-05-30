print('=================Exercise#2====================')
print('--Mengambil Data dan Menampilkan Data (Part1)====')
print('===============================================')
from tkinter import *
import tkinter.messagebox

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('300x150+0+0')

        frame1 = Frame(self.root)
        frame1.grid()

        frame2 = Frame(frame1)   # frame2,3,4 diletakkan pada frame1
        frame2.grid(row=0, column=0)

        frame3 = Frame(frame1)
        frame3.grid(row=2, column=0)

        frame4 = Frame(frame1)
        frame4.grid(row=2, column=1)

        FirstNum = StringVar()
        SecondNum = StringVar()

        self.lblFirstNum = Label(frame2, text='Enter First Number')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2, text='Enter Second Number')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2, textvariable=SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()
