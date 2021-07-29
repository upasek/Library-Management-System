import tkinter
from tkinter import font
from PIL import Image, ImageTk


class UpdateDetails:

    def __init__(self):
        self.UB = tkinter.Frame()
        self.UB.place(x=0, y=0, width=1000, height=700)
        self.UB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("lib1.jpeg"))
        pan = tkinter.Label(self.UB, image=img, width=250, height=400)
        pan.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open("lib1.jpeg"))
        pan = tkinter.Label(self.UB, image=img2, width=250, height=400)
        pan.grid(row=0, column=2)

        label = tkinter.Label(self.UB, text='Update Book Details', bg='black', fg='white', pady=10)
        label.grid(row=0, column=1, sticky='N')
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.UB, text='Book ID', fg='white', bg='black', width=12)
        book_id.grid(row=0, column=1, sticky='W')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        book_id_entry = tkinter.Entry(self.UB)
        book_id_entry.grid(row=0, column=1, sticky='E')

        quit_b = tkinter.Button(self.UB, text='Quit', command=self.UB.destroy)
        quit_b.grid(row=0, column=1, sticky='SW')
        quit_b['font'] = tkinter.font.Font(size=10)

        searchB = tkinter.Button(self.UB, text='Search')
        searchB.grid(row=0, column=1, sticky='SE')
        searchB['font'] = tkinter.font.Font(size=10)

        self.UB.rowconfigure(0, weight=1)
        self.UB.rowconfigure(1, weight=1)
        self.UB.rowconfigure(2, weight=1)

        self.UB.columnconfigure(0, weight=1)
        self.UB.columnconfigure(1, weight=1)
        self.UB.columnconfigure(2, weight=1)

        self.UB.mainloop()
