import tkinter
import tkinter.font
from PIL import Image, ImageTk


class Delete_Book:

    def __init__(self):
        self.DB = tkinter.Frame()
        self.DB.place(x=0, y=0, width=1000, height=700)
        self.DB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("lib1.jpeg"))
        pan = tkinter.Label(self.DB, image=img, width=250, height=300)
        pan.grid(row=0, column=0)

        label = tkinter.Label(self.DB, text='Delete Book', bg='black', fg='white', pady=10)
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.DB, text='Book ID', fg='white', bg='black', width=12)
        book_id.grid(row=1, column=1, sticky='NW')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        book_id_entry = tkinter.Entry(self.DB)
        book_id_entry.grid(row=1, column=1, sticky='NE')

        quit_b = tkinter.Button(self.DB, text='Quit', command=self.DB.destroy)
        quit_b.grid(row=2, column=1, sticky='NW')
        quit_b['font'] = tkinter.font.Font(size=10)

        delete_b = tkinter.Button(self.DB, text='Delete')
        delete_b.grid(row=2, column=1, sticky='NE')
        delete_b['font'] = tkinter.font.Font(size=10)

        self.DB.rowconfigure(0, weight=1)
        self.DB.rowconfigure(1, weight=1)
        self.DB.rowconfigure(2, weight=2)

        self.DB.columnconfigure(0, weight=1)
        self.DB.columnconfigure(1, weight=1)
        self.DB.columnconfigure(2, weight=1)

        self.DB.mainloop()
