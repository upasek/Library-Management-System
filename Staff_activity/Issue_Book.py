import tkinter
import string
import random
from datetime import datetime
import tkinter.font
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from dateutil.relativedelta import relativedelta
import DataBase_connector


class IssueBook:

    def __init__(self, staffID):
        self.issueID = None
        self.sId = staffID
        self.IB = tkinter.Frame()
        self.IB.place(x=0, y=0, width=1000, height=700)
        self.IB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("Images/lib1.jpeg"))
        pan = tkinter.Label(self.IB, image=img, width=250, height=250)
        pan.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open("Images/lib1.jpeg"))
        pan = tkinter.Label(self.IB, image=img2, width=250, height=250)
        pan.grid(row=0, column=2)

        label = tkinter.Label(self.IB, text='Issue Book', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.IB, text='Book ID', fg='white', bg='black')
        book_id.grid(row=1, column=1, sticky='WN')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.book_id_entry = tkinter.Entry(self.IB)
        self.book_id_entry.grid(row=1, column=1, sticky='EN')

        copy_no = tkinter.Label(self.IB, text='Copy No.', fg='white', bg='black')
        copy_no.grid(row=2, column=1, sticky='WN')
        copy_no['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.copy_no_entry = tkinter.Entry(self.IB)
        self.copy_no_entry.grid(row=2, column=1, sticky='EN')

        stud_id = tkinter.Label(self.IB, text='Student ID', fg='white', bg='black')
        stud_id.grid(row=3, column=1, sticky='WN')
        stud_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.stud_id_entry = tkinter.Entry(self.IB)
        self.stud_id_entry.grid(row=3, column=1, sticky='EN')

        issueDate = tkinter.Label(self.IB, text='Issue Date', fg='white', bg='black')
        issueDate.grid(row=4, column=1, sticky='WN')
        issueDate['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.issueDate_entry = DateEntry(self.IB, width=19, background='darkblue', foreground='white', borderwidth=2)
        self.issueDate_entry.grid(row=4, column=1, sticky='EN')

        date_after_month = datetime.today() + relativedelta(months=1)
        date = datetime.strftime(date_after_month, '%d/%m/%y')

        dueDate = tkinter.Label(self.IB, text='Due Date', fg='white', bg='black')
        dueDate.grid(row=5, column=1, sticky='WN')
        dueDate['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.dueDate_entry = tkinter.Entry(self.IB)
        self.dueDate_entry.insert(0, date)
        # self.returnDate_entry = DateEntry(self.IB, width=19, background='darkblue', foreground='white', borderwidth=2)
        # self.returnDate_entry.insert(0, date)
        self.dueDate_entry.grid(row=5, column=1, sticky='EN')

        quit_b = tkinter.Button(self.IB, text='Quit', command=self.IB.destroy)
        quit_b.grid(row=6, column=0, sticky='NE')
        quit_b['font'] = tkinter.font.Font(size=10)

        issue_b = tkinter.Button(self.IB, text='Issue', command=self.check_info)
        issue_b.grid(row=6, column=2, sticky='NW')
        issue_b['font'] = tkinter.font.Font(size=10)

        self.IB.rowconfigure(0, weight=1)
        self.IB.rowconfigure(1, weight=1)
        self.IB.rowconfigure(2, weight=1)
        self.IB.rowconfigure(3, weight=1)
        self.IB.rowconfigure(4, weight=1)
        self.IB.rowconfigure(5, weight=1)
        self.IB.rowconfigure(6, weight=1)

        self.IB.columnconfigure(0, weight=1)
        self.IB.columnconfigure(1, weight=1)
        self.IB.columnconfigure(2, weight=1)

        self.IB.mainloop()

    def check_info(self):
        if self.book_id_entry.get() and self.copy_no_entry.get() and self.stud_id_entry.get() and self.issueDate_entry.get() and self.dueDate_entry.get():
            if self.studentID() and self.BookID() and self.isBookAvailable():
                self.insertInfo()

        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-250")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please Enter all information.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def generate(self):
        x = string.digits
        y = string.ascii_uppercase
        ID = random.choice(y)
        ID += random.choice(x)

        temp = ''.join(random.choice(y) for _ in range(2))
        ID += temp

        temp = ''.join(random.choice(x) for _ in range(4))
        ID += temp
        # ============================
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT issueID from LibraryManagementSystem.IssuedInfo"
        myc.execute(sql)

        result = myc.fetchall()

        DataBase_connector.my_db.commit()
        # ============================

        li = [i[0] for i in result]

        if ID in li:
            self.generate()
        else:
            return ID

    def studentID(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT student_ID FROM LibraryManagementSystem.StudentLoginInfo"
        myc.execute(sql)
        result = myc.fetchall()
        DataBase_connector.my_db.commit()

        x = []
        for i in result:
            x.append(i[0])

        if self.stud_id_entry.get() in x:
            return True
        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-250")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Student ID not registered.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def BookID(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT BookID FROM LibraryManagementSystem.BooksDetails"
        myc.execute(sql)
        result = myc.fetchall()
        DataBase_connector.my_db.commit()

        x = []
        for i in result:
            x.append(i[0])

        if self.book_id_entry.get() in x:
            return True
        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-250")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Enter valid Book ID.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def isBookAvailable(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT Available_copies FROM LibraryManagementSystem.BooksDetails WHERE BookID=%s"
        val = [self.book_id_entry.get()]
        myc.execute(sql, val)
        result = myc.fetchall()
        DataBase_connector.my_db.commit()

        if result[0][0] != 0:
            return True
        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-250")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Book is not available', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def insertInfo(self):
        self.issueID = self.generate()
        myc = DataBase_connector.my_db.cursor()

        sql = "INSERT INTO LibraryManagementSystem.IssuedInfo(issueID, bookID, copyNO, studID, issueDate, issueStaffID, dueDate) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        val = [self.issueID, self.book_id_entry.get(), self.copy_no_entry.get(), self.stud_id_entry.get(),
               self.issueDate_entry.get(), self.sId, self.dueDate_entry.get()]
        myc.execute(sql, val)

        sql = "SELECT Available_copies FROM LibraryManagementSystem.BooksDetails WHERE BookID=%s"
        val = [self.book_id_entry.get()]
        myc.execute(sql, val)
        v = myc.fetchall()

        sql = "UPDATE LibraryManagementSystem.BooksDetails SET Available_copies=%s WHERE (BookID = %s AND sr_no <> %s)"
        val = [v[0][0]-1, self.book_id_entry.get(), 0]
        myc.execute(sql, val)

        if v[0][0]-1 == 0:
            sql = "UPDATE LibraryManagementSystem.BooksDetails SET Availability=%s WHERE (BookID = %s AND sr_no <> %s)"
            val = ['No', self.book_id_entry.get(), 0]
            myc.execute(sql, val)

        DataBase_connector.my_db.commit()

        # =============================================================================

        self.Swindow = tkinter.Tk()
        self.Swindow.title("Library Management System")
        self.Swindow.geometry("300x100-530-250")
        self.Swindow.config(bg="black")
        self.Swindow['pady'] = 20

        label = tkinter.Label(self.Swindow, text='Book Issued Successfully!', bg="black", fg='white')
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
        self.IB.destroy()
