import tkinter
from tkinter import font
from PIL import Image, ImageTk
import webbrowser
from datetime import datetime
import DataBase_connector


class studentsRecords:

    def __init__(self, staffID):
        self.result = None
        self.issueID = None
        self.BookID = None

        self.staff_ID = staffID
        self.SR = tkinter.Frame()
        self.SR.place(x=0, y=0, width=1000, height=700)
        self.SR.config(bg='black')

        img = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.SR, image=img, width=250, height=300)
        panel.grid(row=1, column=0)

        img2 = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.SR, image=img2, width=250, height=300)
        panel.grid(row=1, column=2)

        label2 = tkinter.Label(self.SR, text='Student Records', bg='black', fg='white')
        label2.grid(row=0, column=1)
        label2['font'] = tkinter.font.Font(size=30, family='Helvetica')

        label = tkinter.Label(self.SR, text='Student ID', bg='black', fg='white')
        label.grid(row=1, column=1, sticky='W')
        label['font'] = tkinter.font.Font(size=20, family='Helvetica')

        self.stud_id_entry = tkinter.Entry(self.SR)
        self.stud_id_entry.grid(row=1, column=1, sticky='E')

        current_re = tkinter.Button(self.SR, text="Current Record", pady=10, width=20, activebackground='red',
                                    activeforeground='yellow', command=self.record)
        current_re.grid(row=2, column=0)

        pay_fine = tkinter.Button(self.SR, text="Pay Fine", pady=10, width=20, activebackground='red',
                                  activeforeground='yellow', command=self.Pay_fine)
        pay_fine.grid(row=2, column=1)

        history = tkinter.Button(self.SR, text="History", pady=10, width=20, activebackground='red',
                                 activeforeground='yellow', command=self.history)
        history.grid(row=2, column=2)

        back = tkinter.Button(self.SR, text="Back", pady=10, width=10, activebackground='red',
                              activeforeground='yellow', command=self.SR.destroy)
        back.grid(row=0, column=0)

        self.SR.rowconfigure(0, weight=1)
        self.SR.rowconfigure(1, weight=1)
        self.SR.rowconfigure(2, weight=1)

        self.SR.columnconfigure(0, weight=1)
        self.SR.columnconfigure(1, weight=1)
        self.SR.columnconfigure(2, weight=1)

        self.SR.mainloop()

    def history(self):
        if self.check_entry_box() and self.check_ID():
            self.BR = tkinter.Frame()
            self.BR.place(x=0, y=0, width=1000, height=700)
            self.BR.config(bg='black')

            label = tkinter.Label(self.BR, text='Student Record', bg='black', fg='white')
            label.grid(row=0, column=0)
            label['font'] = tkinter.font.Font(size=25, family='Helvetica')

            Quit = tkinter.Button(self.BR, text="Quit", pady=10, width=15, activebackground='red',
                                  activeforeground='yellow', command=self.BR.destroy)
            Quit.grid(row=2, column=1)

            self.historyTable(self.BR)

            self.BR.rowconfigure(0, weight=1)
            self.BR.rowconfigure(1, weight=4)
            self.BR.rowconfigure(2, weight=1)

            self.BR.columnconfigure(0, weight=4)
            self.BR.columnconfigure(1, weight=1)

            self.BR.mainloop()

    def Pay_fine(self):
        if self.check_entry_box() and self.check_ID():
            self.PF = tkinter.Frame()
            self.PF.place(x=0, y=0, width=1000, height=700)
            self.PF.config(bg='black')

            label = tkinter.Label(self.PF, text='Pay Fine', bg='black', fg='white')
            label.grid(row=0, column=0)
            label['font'] = tkinter.font.Font(size=25, family='Helvetica')

            label1 = tkinter.Label(self.PF, text='Issue ID', bg='black', fg='white')
            label1.grid(row=2, column=1, sticky='W')
            label1['font'] = tkinter.font.Font(size=20, family='Helvetica')

            self.issueID = tkinter.Entry(self.PF)
            self.issueID.grid(row=2, column=1, sticky='E')

            label2 = tkinter.Label(self.PF, text='Book ID', bg='black', fg='white')
            label2.grid(row=3, column=1, sticky='W')
            label2['font'] = tkinter.font.Font(size=20, family='Helvetica')

            self.BookID = tkinter.Entry(self.PF)
            self.BookID.grid(row=3, column=1, sticky='E')

            Pay_Button = tkinter.Button(self.PF, text='Pay', pady=10, width=10, activebackground='red',
                                        activeforeground='yellow', command=self.check_Entry)
            Pay_Button.grid(row=4, column=1, sticky='E')

            Quit = tkinter.Button(self.PF, text="Quit", pady=10, width=10, activebackground='red',
                                  activeforeground='yellow', command=self.PF.destroy)
            Quit.grid(row=4, column=1, sticky='W')

            self.PayFine_list(self.PF)

            self.PF.rowconfigure(0, weight=3)
            self.PF.rowconfigure(1, weight=1)
            self.PF.rowconfigure(2, weight=1)
            self.PF.rowconfigure(3, weight=1)
            self.PF.rowconfigure(4, weight=1)
            self.PF.rowconfigure(5, weight=4)

            self.PF.columnconfigure(0, weight=4)
            self.PF.columnconfigure(1, weight=1)
            self.PF.columnconfigure(2, weight=1)

            self.PF.mainloop()

    def record(self):
        if self.check_entry_box() and self.check_ID():
            self.BR = tkinter.Frame()
            self.BR.place(x=0, y=0, width=1000, height=700)
            self.BR.config(bg='black')

            label = tkinter.Label(self.BR, text='Student Record', bg='black', fg='white')
            label.grid(row=0, column=0)
            label['font'] = tkinter.font.Font(size=25, family='Helvetica')

            Quit = tkinter.Button(self.BR, text="Quit", pady=10, width=15, activebackground='red',
                                  activeforeground='yellow', command=self.BR.destroy)
            Quit.grid(row=2, column=1)

            self.recordTable(self.BR)

            self.BR.rowconfigure(0, weight=1)
            self.BR.rowconfigure(1, weight=4)
            self.BR.rowconfigure(2, weight=1)

            self.BR.columnconfigure(0, weight=4)
            self.BR.columnconfigure(1, weight=1)

            self.BR.mainloop()

    def recordTable(self, root):
        labelframe = tkinter.Frame(root, bg='black')
        labelframe.place(x=50, y=150, width=700, height=500)

        v = tkinter.Scrollbar(labelframe)
        v.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        h = tkinter.Scrollbar(labelframe, orient='horizontal')
        h.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        t = tkinter.Text(labelframe, width=15, height=30, wrap=tkinter.NONE, xscrollcommand=h.set, yscrollcommand=v.set)

        t.insert(tkinter.END, "%-15s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % (
            'Issue ID', 'Book ID', 'Copy No', 'Student ID', 'Issue Date',
            'Issue Staff ID', 'Due Date', 'Is Book Return', 'Return Date',
            'Return Staff ID', 'Fine', 'Is Fine Paid', 'Payment Date',
            'Fine Staff ID'))
        t.insert(tkinter.END, "=" * 280)
        t.insert(tkinter.END, "\n")

        # =================================================
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT * FROM LibraryManagementSystem.IssuedInfo WHERE studID=%s"
        val = [self.stud_id_entry.get()]
        myc.execute(sql, val)

        result = myc.fetchall()

        DataBase_connector.my_db.commit()
        # =================================================

        for i in result:
            t.insert(tkinter.END, "%-15s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % (
                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]))
            t.insert(tkinter.END, "-" * 280)
            t.insert(tkinter.END, "\n")

        t.pack(side=tkinter.TOP, fill=tkinter.X)

        v.config(command=t.yview)
        h.config(command=t.xview)

    def PayFine_list(self, root):
        labelframe = tkinter.Frame(root, bg='black')
        labelframe.place(x=50, y=150, width=500, height=500)

        v = tkinter.Scrollbar(labelframe)
        v.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        h = tkinter.Scrollbar(labelframe, orient='horizontal')
        h.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        t = tkinter.Text(labelframe, width=15, height=30, wrap=tkinter.NONE, xscrollcommand=h.set, yscrollcommand=v.set)

        t.insert(tkinter.END, "%-15s%-20s%-20s%-20s\n" % ('Issue ID', 'Book ID', 'Book Name', 'Fine'))
        t.insert(tkinter.END, "=" * 60)
        t.insert(tkinter.END, "\n")

        # =================================================
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT issueID, bookID, fine FROM LibraryManagementSystem.IssuedInfo WHERE studID=%s AND isBookReturn=%s"
        val = [self.stud_id_entry.get(), "Yes"]
        myc.execute(sql, val)

        self.result = myc.fetchall()

        DataBase_connector.my_db.commit()
        # =================================================
        list_bookName = []

        for i in self.result:
            myc = DataBase_connector.my_db.cursor()
            sql = 'SELECT Title from LibraryManagementSystem.BooksDetails WHERE BookID=%s'
            val = [str(i[1])]
            myc.execute(sql, val)
            re = myc.fetchall()

            DataBase_connector.my_db.commit()
            # print(re)
            list_bookName.append(re[0][0])

        # print(list_bookName)
        j = 0
        for i in self.result:
            t.insert(tkinter.END, "%-15s%-20s%-20s%-20s\n" % (i[0], i[1], list_bookName[j], i[2]))
            t.insert(tkinter.END, "-" * 60)
            t.insert(tkinter.END, "\n")
            j += 1

        t.pack(side=tkinter.TOP, fill=tkinter.X)

        v.config(command=t.yview)
        h.config(command=t.xview)

    def historyTable(self, root):
        labelframe = tkinter.Frame(root, bg='black')
        labelframe.place(x=50, y=150, width=700, height=500)

        v = tkinter.Scrollbar(labelframe)
        v.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        h = tkinter.Scrollbar(labelframe, orient='horizontal')
        h.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        t = tkinter.Text(labelframe, width=15, height=30, wrap=tkinter.NONE, xscrollcommand=h.set, yscrollcommand=v.set)

        t.insert(tkinter.END, "%-15s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % (
            'Issue ID', 'Book ID', 'Copy No', 'Student ID', 'Issue Date',
            'Issue Staff ID', 'Due Date', 'Is Book Return', 'Return Date',
            'Return Staff ID', 'Fine', 'Is Fine Paid', 'Payment Date',
            'Fine Staff ID'))
        t.insert(tkinter.END, "=" * 280)
        t.insert(tkinter.END, "\n")

        # =================================================
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT * FROM LibraryManagementSystem.HistoryOfStudent WHERE studID=%s"
        val = [self.stud_id_entry.get()]
        myc.execute(sql, val)

        result = myc.fetchall()

        DataBase_connector.my_db.commit()
        # =================================================

        for i in result:
            t.insert(tkinter.END, "%-15s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % (
                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]))
            t.insert(tkinter.END, "-" * 280)
            t.insert(tkinter.END, "\n")

        t.pack(side=tkinter.TOP, fill=tkinter.X)

        v.config(command=t.yview)
        h.config(command=t.xview)

    def check_ID(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT student_ID FROM LibraryManagementSystem.StudentLoginInfo"
        myc.execute(sql)
        x = myc.fetchall()
        DataBase_connector.my_db.commit()

        li = [i[0] for i in x]

        if self.stud_id_entry.get() in li:
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

            label2 = tkinter.Label(window, text='Please enter valid Student ID.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def check_entry_box(self):
        if self.stud_id_entry.get():
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

            label2 = tkinter.Label(window, text='Please enter Student ID.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def check_Entry(self):
        if self.issueID.get() and self.BookID.get():
            issue_ID = self.issueID.get()
            book_ID = self.BookID.get()

            # print(self.result)

            t = False
            for i in self.result:
                if str(issue_ID) == str(i[0]) and str(book_ID) == str(i[1]):
                    t = True

            if t:
                self.open_page()
            else:
                window = tkinter.Tk()
                window.title("Library Management System")
                window.geometry("300x100-530-250")
                window.config(bg="black")
                window['pady'] = 5

                label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
                label.pack(side='top')
                label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

                label2 = tkinter.Label(window, text='Please enter Valid information.', bg='black', fg='white')
                label2.pack(side='top')

                # ok button for destroy frame
                ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                    command=window.destroy)
                ok.pack(side='bottom', anchor='n')
                ok['font'] = tkinter.font.Font(size=15)

                window.minsize(300, 100)
                window.maxsize(300, 100)
                window.mainloop()

        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-250")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please enter all information.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def open_page(self):
        webbrowser.open_new(r"https://www.paypal.com/paypalme/kiranupase123")
        self.DeleteInfo()

    def DeleteInfo(self):
        myc = DataBase_connector.my_db.cursor()

        sql = 'SELECT * FROM LibraryManagementSystem.IssuedInfo WHERE bookID = %s AND studID = %s'
        val = [self.BookID.get(), self.stud_id_entry.get()]
        myc.execute(sql, val)

        al = myc.fetchall()
        all_info = list(al[0])

        date = datetime.today()
        fine_data = datetime.strftime(date, '%d/%m/%y')
        # print(all_info)
        all_info[11] = 'Yes'
        all_info[12] = fine_data
        all_info[13] = self.staff_ID

        sql = 'DELETE FROM LibraryManagementSystem.IssuedInfo WHERE bookID = %s AND studID = %s'
        val = [self.BookID.get(), self.stud_id_entry.get()]
        myc.execute(sql, val)

        sql = "INSERT INTO LibraryManagementSystem.HistoryOfStudent(issueID, bookID, copyNO, studID, issueDate, issueStaffID, dueDate, isBookReturn, return_date, returnStaffID, fine, isFinePaid, paymentDate, fineStaffID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = [all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5], all_info[6], all_info[7],
               all_info[8], all_info[9], all_info[10], all_info[11], all_info[12], all_info[13]]
        myc.execute(sql, val)

        DataBase_connector.my_db.commit()
