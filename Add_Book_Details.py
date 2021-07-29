import tkinter
import tkinter.font
from PIL import Image, ImageTk


class add_book:

    def __init__(self):
        self.AB = tkinter.Frame()
        self.AB.place(x=0, y=0, width=1000, height=700)
        self.AB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("lib2.jpeg"))
        pan = tkinter.Label(self.AB, image=img, width=250, height=250)
        pan.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open("lib2.jpeg"))
        pan = tkinter.Label(self.AB, image=img2, width=250, height=250)
        pan.grid(row=0, column=2)

        label = tkinter.Label(self.AB, text='Add Book Details', bg='black', fg='white', anchor='s', pady=10)
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.AB, text='Book ID', fg='white', bg='black')
        book_id.grid(row=1, column=1, sticky='W')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        book_id_entry = tkinter.Entry(self.AB)
        book_id_entry.grid(row=1, column=1, sticky='E')

        title = tkinter.Label(self.AB, text='Title', fg='white', bg='black')
        title.grid(row=2, column=1, sticky='W')
        title['font'] = tkinter.font.Font(size=15, family='Helvetica')
        title_entry = tkinter.Entry(self.AB)
        title_entry.grid(row=2, column=1, sticky='E')

        author = tkinter.Label(self.AB, text='Author', fg='white', bg='black')
        author.grid(row=3, column=1, sticky='W')
        author['font'] = tkinter.font.Font(size=15, family='Helvetica')
        author_entry = tkinter.Entry(self.AB)
        author_entry.grid(row=3, column=1, sticky='E')

        aval = tkinter.Label(self.AB, text='availability', fg='white', bg='black')
        aval.grid(row=4, column=1, sticky='W')
        aval['font'] = tkinter.font.Font(size=15, family='Helvetica')
        aval_entry = tkinter.Entry(self.AB)
        aval_entry.grid(row=4, column=1, sticky='E')

        quit_b = tkinter.Button(self.AB, text='Quit', command=self.AB.destroy)
        quit_b.grid(row=5, column=0, sticky='E')
        quit_b['font'] = tkinter.font.Font(size=10)

        add = tkinter.Button(self.AB, text='ADD', command=self.InsertDetails)
        add.grid(row=5, column=2, sticky='W')
        add['font'] = tkinter.font.Font(size=10)

        self.AB.rowconfigure(0, weight=1)
        self.AB.rowconfigure(1, weight=1)
        self.AB.rowconfigure(2, weight=1)
        self.AB.rowconfigure(3, weight=1)
        self.AB.rowconfigure(4, weight=1)
        self.AB.rowconfigure(5, weight=2)

        self.AB.columnconfigure(0, weight=1)
        self.AB.columnconfigure(1, weight=2)
        self.AB.columnconfigure(2, weight=1)

        self.AB.mainloop()

    def InsertDetails(self):
        self.checkNone()

    def checkNone(self):
        return





