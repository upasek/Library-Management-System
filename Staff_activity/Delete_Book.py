import tkinter
import tkinter.font
from PIL import Image, ImageTk
import DataBase_connector


class Delete_Book:

    def __init__(self):
        self.DB = tkinter.Frame()
        self.DB.place(x=0, y=0, width=1000, height=700)
        self.DB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("Images/lib1.jpeg"))
        pan = tkinter.Label(self.DB, image=img, width=250, height=300)
        pan.grid(row=0, column=0)

        label = tkinter.Label(self.DB, text='Delete Book', bg='black', fg='white', pady=10)
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.DB, text='Book ID', fg='white', bg='black', width=12)
        book_id.grid(row=1, column=1, sticky='NW')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.book_id_entry = tkinter.Entry(self.DB)
        self.book_id_entry.grid(row=1, column=1, sticky='NE')

        quit_b = tkinter.Button(self.DB, text='Quit', command=self.DB.destroy)
        quit_b.grid(row=2, column=1, sticky='NW')
        quit_b['font'] = tkinter.font.Font(size=10)

        delete_b = tkinter.Button(self.DB, text='Delete', command=self.checkinfo)
        delete_b.grid(row=2, column=1, sticky='NE')
        delete_b['font'] = tkinter.font.Font(size=10)

        self.DB.rowconfigure(0, weight=1)
        self.DB.rowconfigure(1, weight=1)
        self.DB.rowconfigure(2, weight=2)

        self.DB.columnconfigure(0, weight=1)
        self.DB.columnconfigure(1, weight=1)
        self.DB.columnconfigure(2, weight=1)

        self.DB.mainloop()

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

            self.Delete(li)

        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-400-300")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please Enter Book ID', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def Delete(self, li):
        if self.book_id_entry.get() in li:
            myc = DataBase_connector.my_db.cursor()
            sql = "DELETE FROM LibraryManagementSystem.BooksDetails WHERE BookID = %s"
            val = [self.book_id_entry.get()]

            myc.execute(sql, val)

            DataBase_connector.my_db.commit()

            # ======================

            self.Mwindow = tkinter.Tk()
            self.Mwindow.title("Library Management System")
            self.Mwindow.geometry("300x100-400-300")
            self.Mwindow.config(bg="black")
            self.Mwindow['pady'] = 20

            label = tkinter.Label(self.Mwindow, text='Book Deleted Successfully!', bg="black", fg='white')
            label.pack()

            ok = tkinter.Button(self.Mwindow, text="OK", activebackground='#FFA500',
                                command=self.refresh)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            self.Mwindow.minsize(300, 100)
            self.Mwindow.maxsize(300, 100)

            # self.window.after(2500, self.window.destroy)

            self.Mwindow.mainloop()

        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-400-300")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please Enter Valid Book ID', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def refresh(self):
        self.Mwindow.destroy()
        self.DB.destroy()
