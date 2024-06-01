from tkinter import *

print('====================Exercise#1======================')
print('=== Mencetak data dari entry widget dengan button===')
print('====================================================')

root = Tk()
root.geometry('400x200')

def Cetakdata():
    teks= entry1.get()
    print(teks)
    return None

entry1 = Entry(root, width=20)
entry1.pack()

Button(root, text = "Cetak Data", command=Cetakdata).pack()

root.mainloop()