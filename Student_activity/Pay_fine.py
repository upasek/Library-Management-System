import tkinter
from tkinter import font
from datetime import datetime
import webbrowser

import DataBase_connector


class PayFine:
    def __init__(self, studentID):
        self.result = None

        self.student_ID = studentID
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
        val = [self.student_ID, "Yes"]
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
        val = [self.BookID.get(), self.student_ID]
        myc.execute(sql, val)

        al = myc.fetchall()
        all_info = list(al[0])

        date = datetime.today()
        fine_data = datetime.strftime(date, '%d/%m/%y')
        # print(all_info)
        all_info[11] = 'Yes'
        all_info[12] = fine_data

        sql = 'DELETE FROM LibraryManagementSystem.IssuedInfo WHERE bookID = %s AND studID = %s'
        val = [self.BookID.get(), self.student_ID]
        myc.execute(sql, val)

        sql = "INSERT INTO LibraryManagementSystem.HistoryOfStudent(issueID, bookID, copyNO, studID, issueDate, issueStaffID, dueDate, isBookReturn, return_date, returnStaffID, fine, isFinePaid, paymentDate, fineStaffID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = [all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5], all_info[6], all_info[7],
               all_info[8], all_info[9], all_info[10], all_info[11], all_info[12], all_info[13]]
        myc.execute(sql, val)

        DataBase_connector.my_db.commit()
