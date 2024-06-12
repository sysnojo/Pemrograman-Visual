from tkinter import *
from PIL import Image, ImageTk

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("Boomerberg 2024")

        # Load the logo image with a transparent background
        logo_path = "C:\\Users\\ngrok\\Documents\\[43] PEMVIS 2024\\Pertemuan 13\\Mini Project\\Boomerberg\\logo.png"
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((216, 44))  # Resize the image to 216x44 pixels
        logo = ImageTk.PhotoImage(logo_img)

        # Create a label for the logo with a transparent background
        self.logo_lbl = Label(image=logo, background='#0C0C0C')
        self.logo_lbl.image = logo  # Keep a reference to avoid garbage collection
        self.logo_lbl.pack()

        # frame
        self.chart_frame = Frame(self, width=1300, height=640, background="black", bd=5, highlightcolor="white", highlightthickness=1)
        self.chart_frame.pack()
        
        # button
        self.button = Button(self.chart_frame, text="Click Me", command=self.button_click)
        self.button.place(x=600, y=300)  # Adjust the x and y coordinates as needed

        # Place the logo label at position x = 100 and y = 150

        # create frame
        
        # Pack the frame
        self.pack()

root = Tk()
root.geometry('1366x768')  # Set the window size to 1366x768
root.configure(bg="#0C0C0C")  # Set the window background color to dark gray
app = Application(master=root)
app.mainloop()
