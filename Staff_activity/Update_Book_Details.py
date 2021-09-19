import tkinter
from tkinter import font
from PIL import Image, ImageTk
import DataBase_connector


class UpdateDetails:

    def __init__(self):
        self.book_entry = None
        self.title_entry = None
        self.author_entry = None
        self.aval_entry = None

        self.UB = tkinter.Frame()
        self.UB.place(x=0, y=0, width=1000, height=700)
        self.UB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("Images/lib1.jpeg"))
        pan = tkinter.Label(self.UB, image=img, width=250, height=400)
        pan.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open("Images/lib1.jpeg"))
        pan = tkinter.Label(self.UB, image=img2, width=250, height=400)
        pan.grid(row=0, column=2)

        label = tkinter.Label(self.UB, text='Update Book Details', bg='black', fg='white', pady=10)
        label.grid(row=0, column=1, sticky='N')
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.UB, text='Book ID', fg='white', bg='black', width=12)
        book_id.grid(row=0, column=1, sticky='W')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.book_id_entry = tkinter.Entry(self.UB)
        self.book_id_entry.grid(row=0, column=1, sticky='E')

        quit_b = tkinter.Button(self.UB, text='Quit', command=self.UB.destroy)
        quit_b.grid(row=0, column=1, sticky='SW')
        quit_b['font'] = tkinter.font.Font(size=10)

        searchB = tkinter.Button(self.UB, text='Search', command=self.checkinfo)
        searchB.grid(row=0, column=1, sticky='SE')
        searchB['font'] = tkinter.font.Font(size=10)

        self.UB.rowconfigure(0, weight=1)
        self.UB.rowconfigure(1, weight=1)
        self.UB.rowconfigure(2, weight=1)

        self.UB.columnconfigure(0, weight=1)
        self.UB.columnconfigure(1, weight=1)
        self.UB.columnconfigure(2, weight=1)

        self.UB.mainloop()

    def checkinfo(self):
        if self.book_id_entry.get():

            myc = DataBase_connector.my_db.cursor()
            sql = "SELECT BookID FROM LibraryManagementSystem.BooksDetails"

            myc.execute(sql)

            result = myc.fetchall()

            li = []
            for i in result:
                li.append(i[0])

            DataBase_connector.my_db.commit()

            self.update(li)

        else:
            self.window = tkinter.Tk()
            self.window.title("Library Management System")
            self.window.geometry("300x100-530-400")
            self.window.config(bg="black")
            self.window['pady'] = 5

            label = tkinter.Label(self.window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(self.window, text='Please Enter Book ID.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(self.window, text="OK", activebackground='#FFA500',
                                command=self.window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            self.window.minsize(300, 100)
            self.window.maxsize(300, 100)
            self.window.mainloop()

    def update(self, li):
        if self.book_id_entry.get() in li:
            self.updateDetails()
        else:
            self.window = tkinter.Tk()
            self.window.title("Library Management System")
            self.window.geometry("300x100-530-400")
            self.window.config(bg="black")
            self.window['pady'] = 5

            label = tkinter.Label(self.window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(self.window, text='Please Enter Valid Book ID.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(self.window, text="OK", activebackground='#FFA500',
                                command=self.window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            self.window.minsize(300, 100)
            self.window.maxsize(300, 100)
            self.window.mainloop()

    def updateDetails(self):

        # ====================
        val_b = self.book_id_entry.get()

        myc = DataBase_connector.my_db.cursor()

        sql = "SELECT BookID, Title, Author, Availability, TotalCopies FROM LibraryManagementSystem.BooksDetails WHERE BookID = %s"
        val = [val_b]

        myc.execute(sql, val)

        result = myc.fetchall()

        DataBase_connector.my_db.commit()

        # ====================

        self.UF = tkinter.Frame()
        self.UF.place(x=0, y=0, width=1000, height=700)
        self.UF.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("Images/lib2.jpeg"))
        pan = tkinter.Label(self.UF, image=img, width=250, height=250)
        pan.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open("Images/lib2.jpeg"))
        pan = tkinter.Label(self.UF, image=img2, width=250, height=250)
        pan.grid(row=0, column=2)

        label = tkinter.Label(self.UF, text='Update Book Details', bg='black', fg='white', anchor='s', pady=10)
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.UF, text='Book ID', fg='white', bg='black')
        book_id.grid(row=1, column=1, sticky='W')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.book_entry = tkinter.Entry(self.UF)
        self.book_entry.insert(0, result[0][0])
        self.book_entry.grid(row=1, column=1, sticky='E')

        title = tkinter.Label(self.UF, text='Title', fg='white', bg='black')
        title.grid(row=2, column=1, sticky='W')
        title['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.title_entry = tkinter.Entry(self.UF)
        self.title_entry.insert(0, result[0][1])
        self.title_entry.grid(row=2, column=1, sticky='E')

        author = tkinter.Label(self.UF, text='Author', fg='white', bg='black')
        author.grid(row=3, column=1, sticky='W')
        author['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.author_entry = tkinter.Entry(self.UF)
        self.author_entry.insert(0, result[0][2])
        self.author_entry.grid(row=3, column=1, sticky='E')

        aval = tkinter.Label(self.UF, text='availability', fg='white', bg='black')
        aval.grid(row=4, column=1, sticky='W')
        aval['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.aval_entry = tkinter.Entry(self.UF)
        self.aval_entry.insert(0, result[0][3])
        self.aval_entry.grid(row=4, column=1, sticky='E')

        copies = tkinter.Label(self.UF, text='Total Number of copies', fg='white', bg='black')
        copies.grid(row=5, column=1, sticky='W')
        copies['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.copies_entry = tkinter.Entry(self.UF)
        self.copies_entry.insert(0, result[0][4])
        self.copies_entry.grid(row=5, column=1, sticky='E')

        cancel = tkinter.Button(self.UF, text='cancel', command=self.UF.destroy)
        cancel.grid(row=6, column=0, sticky='E')
        cancel['font'] = tkinter.font.Font(size=10)

        update = tkinter.Button(self.UF, text='Update', command=self.check_info_in_entry)
        update.grid(row=6, column=2, sticky='W')
        update['font'] = tkinter.font.Font(size=10)

        self.UF.rowconfigure(0, weight=1)
        self.UF.rowconfigure(1, weight=1)
        self.UF.rowconfigure(2, weight=1)
        self.UF.rowconfigure(3, weight=1)
        self.UF.rowconfigure(4, weight=1)
        self.UF.rowconfigure(5, weight=1)
        self.UF.rowconfigure(6, weight=2)

        self.UF.columnconfigure(0, weight=1)
        self.UF.columnconfigure(1, weight=2)
        self.UF.columnconfigure(2, weight=1)

        self.UF.mainloop()

    def check_info_in_entry(self):
        if self.book_entry.get() and self.title_entry.get() and self.author_entry.get() and self.aval_entry.get() and self.copies_entry.get():
            self.UpdateFromDB()
        else:
            self.window = tkinter.Tk()
            self.window.title("Library Management System")
            self.window.geometry("300x100-530-400")
            self.window.config(bg="black")
            self.window['pady'] = 5

            label = tkinter.Label(self.window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(self.window, text='Please Enter All Information.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(self.window, text="OK", activebackground='#FFA500',
                                command=self.window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            self.window.minsize(300, 100)
            self.window.maxsize(300, 100)
            self.window.mainloop()

    def UpdateFromDB(self):
        myc = DataBase_connector.my_db.cursor()

        sql = "UPDATE LibraryManagementSystem.BooksDetails SET BookID = %s, Title = %s, Author = %s, Availability = %s, TotalCopies = %s WHERE BookID = %s"
        val = [self.book_entry.get(), self.title_entry.get(), self.author_entry.get(), self.aval_entry.get(), self.copies_entry.get(), self.book_id_entry.get()]

        myc.execute(sql, val)

        DataBase_connector.my_db.commit()

        self.successful()

    def successful(self):
        self.Swindow = tkinter.Tk()
        self.Swindow.title("Library Management System")
        self.Swindow.geometry("300x100-530-250")
        self.Swindow.config(bg="black")
        self.Swindow['pady'] = 20

        label = tkinter.Label(self.Swindow, text='Book Updated Successfully!', bg="black", fg='white')
        label.pack()

        ok = tkinter.Button(self.Swindow, text="OK", activebackground='#FFA500',
                            command=self.refresh)
        ok.pack(side='bottom', anchor='n')
        ok['font'] = tkinter.font.Font(size=15)

        self.Swindow.minsize(300, 100)
        self.Swindow.maxsize(300, 100)

        self.Swindow.mainloop()

    def refresh(self):
        self.Swindow.destroy()
        self.UF.destroy()
        self.UB.destroy()
