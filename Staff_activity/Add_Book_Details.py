import tkinter
import tkinter.font
from PIL import Image, ImageTk
import DataBase_connector


class add_book:

    def __init__(self):

        self.AB = tkinter.Frame()
        self.AB.place(x=0, y=0, width=1000, height=700)
        self.AB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open('Images/lib2.jpeg'))
        pan = tkinter.Label(self.AB, image=img, width=250, height=250)
        pan.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open('Images/lib2.jpeg'))
        pan = tkinter.Label(self.AB, image=img2, width=250, height=250)
        pan.grid(row=0, column=2)

        label = tkinter.Label(self.AB, text='Add Book Details', bg='black', fg='white', anchor='s', pady=10)
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.AB, text='Book ID', fg='white', bg='black')
        book_id.grid(row=1, column=1, sticky='W')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.book_id_entry = tkinter.Entry(self.AB)
        self.book_id_entry.grid(row=1, column=1, sticky='E')

        title = tkinter.Label(self.AB, text='Title', fg='white', bg='black')
        title.grid(row=2, column=1, sticky='W')
        title['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.title_entry = tkinter.Entry(self.AB)
        self.title_entry.grid(row=2, column=1, sticky='E')

        author = tkinter.Label(self.AB, text='Author', fg='white', bg='black')
        author.grid(row=3, column=1, sticky='W')
        author['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.author_entry = tkinter.Entry(self.AB)
        self.author_entry.grid(row=3, column=1, sticky='E')

        aval = tkinter.Label(self.AB, text='availability', fg='white', bg='black')
        aval.grid(row=4, column=1, sticky='W')
        aval['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.aval_entry = tkinter.Entry(self.AB)
        self.aval_entry.grid(row=4, column=1, sticky='E')

        copies = tkinter.Label(self.AB, text='Number of copies', fg='white', bg='black')
        copies.grid(row=5, column=1, sticky='W')
        copies['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.copies_entry = tkinter.Entry(self.AB)
        self.copies_entry.grid(row=5, column=1, sticky='E')

        quit_b = tkinter.Button(self.AB, text='Quit', command=self.AB.destroy)
        quit_b.grid(row=6, column=0, sticky='E')
        quit_b['font'] = tkinter.font.Font(size=10)

        add = tkinter.Button(self.AB, text='ADD', command=self.InsertDetails)
        add.grid(row=6, column=2, sticky='W')
        add['font'] = tkinter.font.Font(size=10)

        self.AB.rowconfigure(0, weight=1)
        self.AB.rowconfigure(1, weight=1)
        self.AB.rowconfigure(2, weight=1)
        self.AB.rowconfigure(3, weight=1)
        self.AB.rowconfigure(4, weight=1)
        self.AB.rowconfigure(5, weight=1)
        self.AB.rowconfigure(6, weight=2)

        self.AB.columnconfigure(0, weight=1)
        self.AB.columnconfigure(1, weight=2)
        self.AB.columnconfigure(2, weight=1)

        self.AB.mainloop()

    def InsertDetails(self):
        if self.book_id_entry.get() and self.title_entry.get() and self.author_entry.get() and self.aval_entry.get() and self.copies_entry.get():
            try:
                myc = DataBase_connector.my_db.cursor()
                sql = "INSERT INTO LibraryManagementSystem.BooksDetails(BookID, Title, Author, Availability, TotalCopies, Available_copies) VALUES(%s, %s, %s, %s, %s, %s)"
                val = [self.book_id_entry.get(), self.title_entry.get(), self.author_entry.get(), self.aval_entry.get(), self.copies_entry.get(), self.copies_entry.get()]

                myc.execute(sql, val)

                DataBase_connector.my_db.commit()

                self.successful()

            except ValueError:
                self.window = tkinter.Tk()
                self.window.title("Library Management System")
                self.window.geometry("300x100-530-250")
                self.window.config(bg="black")
                self.window["pady"] = 15

                label = tkinter.Label(self.window, text="Please enter correct Info!", bg="black", fg='white')
                label.pack()

                self.window.minsize(300, 100)
                self.window.maxsize(300, 100)

                self.window.after(2500, self.window.destroy)

                self.window.mainloop()

        else:
            self.warning()

    def successful(self):
        self.Swindow = tkinter.Tk()
        self.Swindow.title("Library Management System")
        self.Swindow.geometry("300x100-530-250")
        self.Swindow.config(bg="black")
        self.Swindow['pady'] = 20

        label = tkinter.Label(self.Swindow, text='Book Added Successfully!', bg="black", fg='white')
        label.pack()

        ok = tkinter.Button(self.Swindow, text="OK", activebackground='#FFA500',
                            command=self.refresh)
        ok.pack(side='bottom', anchor='n')
        ok['font'] = tkinter.font.Font(size=15)

        self.Swindow.minsize(300, 100)
        self.Swindow.maxsize(300, 100)

        # self.window.after(2500, self.window.destroy)

        self.Swindow.mainloop()

    def refresh(self):
        self.Swindow.destroy()
        self.AB.destroy()

    def warning(self):
        self.window = tkinter.Tk()
        self.window.title("Library Management System")
        self.window.geometry("300x100-530-250")
        self.window.config(bg="black")
        self.window['pady'] = 5

        label = tkinter.Label(self.window, text="WARNING!", bg='black', fg='white')
        label.pack(side='top')
        label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

        label2 = tkinter.Label(self.window, text='Please Enter all information.', bg='black', fg='white')
        label2.pack(side='top')

        # ok button for destroy frame
        ok = tkinter.Button(self.window, text="OK", activebackground='#FFA500',
                            command=self.window.destroy)
        ok.pack(side='bottom', anchor='n')
        ok['font'] = tkinter.font.Font(size=15)

        self.window.minsize(300, 100)
        self.window.maxsize(300, 100)
        self.window.mainloop()
