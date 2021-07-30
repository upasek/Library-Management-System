import tkinter
import tkinter.font
from PIL import Image, ImageTk


class ReturnBook:

    def __init__(self):
        self.RB = tkinter.Frame()
        self.RB.place(x=0, y=0, width=1000, height=700)
        self.RB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("lib1.jpeg"))
        pan = tkinter.Label(self.RB, image=img, width=250, height=300)
        pan.grid(row=0, column=0)

        label = tkinter.Label(self.RB, text='Return Book', bg='black', fg='white', pady=10)
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.RB, text='Book ID', fg='white', bg='black', width=12)
        book_id.grid(row=1, column=1, sticky='NW')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        book_id_entry = tkinter.Entry(self.RB)
        book_id_entry.grid(row=1, column=1, sticky='NE')

        quit_b = tkinter.Button(self.RB, text='Quit', command=self.RB.destroy)
        quit_b.grid(row=2, column=1, sticky='NW')
        quit_b['font'] = tkinter.font.Font(size=10)

        return_b = tkinter.Button(self.RB, text='Return')
        return_b.grid(row=2, column=1, sticky='NE')
        return_b['font'] = tkinter.font.Font(size=10)

        self.RB.rowconfigure(0, weight=1)
        self.RB.rowconfigure(1, weight=1)
        self.RB.rowconfigure(2, weight=2)

        self.RB.columnconfigure(0, weight=1)
        self.RB.columnconfigure(1, weight=1)
        self.RB.columnconfigure(2, weight=1)

        self.RB.mainloop()
