import tkinter
import tkinter.font
from PIL import Image, ImageTk
from datetime import datetime
import DataBase_connector


class ReturnBook:

    def __init__(self, s_ID):
        self.staffID = s_ID
        self.RB = tkinter.Frame()
        self.RB.place(x=0, y=0, width=1000, height=700)
        self.RB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("Images/lib1.jpeg"))
        pan = tkinter.Label(self.RB, image=img, width=250, height=300)
        pan.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open("Images/lib1.jpeg"))
        pan2 = tkinter.Label(self.RB, image=img2, width=250, height=300)
        pan2.grid(row=0, column=2)

        label = tkinter.Label(self.RB, text='Return Book', bg='black', fg='white', pady=10)
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        stud_id = tkinter.Label(self.RB, text='Student ID', fg='white', bg='black')
        stud_id.grid(row=1, column=1, sticky='NW')
        stud_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.stud_id_entry = tkinter.Entry(self.RB)
        self.stud_id_entry.grid(row=1, column=1, sticky='NE')

        book_id = tkinter.Label(self.RB, text='Book ID', fg='white', bg='black')
        book_id.grid(row=2, column=1, sticky='NW')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.book_id_entry = tkinter.Entry(self.RB)
        self.book_id_entry.grid(row=2, column=1, sticky='NE')

        quit_b = tkinter.Button(self.RB, text='Quit', command=self.RB.destroy, width=5)
        quit_b.grid(row=3, column=0, sticky='NE')
        quit_b['font'] = tkinter.font.Font(size=12)

        next_b = tkinter.Button(self.RB, text='Next', width=5, command=self.check_info)
        next_b.grid(row=3, column=2, sticky='NW')
        next_b['font'] = tkinter.font.Font(size=12)

        self.RB.rowconfigure(0, weight=1)
        self.RB.rowconfigure(1, weight=1)
        self.RB.rowconfigure(2, weight=1)
        self.RB.rowconfigure(3, weight=2)

        self.RB.columnconfigure(0, weight=1)
        self.RB.columnconfigure(1, weight=1)
        self.RB.columnconfigure(2, weight=1)

        self.RB.mainloop()

    def check_info(self):

        if self.stud_id_entry.get() and self.book_id_entry.get():
            if self.studID() and self.bookID():
                self.search_id_in_DB()
        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-250")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please enter all information', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def search_id_in_DB(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT issueID FROM LibraryManagementSystem.IssuedInfo WHERE bookID=%s AND studID=%s"
        val = [self.book_id_entry.get(), self.stud_id_entry.get()]
        myc.execute(sql, val)
        x = myc.fetchall()
        DataBase_connector.my_db.commit()

        if len(x) != 0:
            self.find_difference_in_date()
        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("350x130-500-250")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            text = 'This student with student ID ' + self.stud_id_entry.get() + ' \nhas not issued any book of Book ID ' + self.book_id_entry.get()

            label2 = tkinter.Label(window, text=text, bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", width=10, activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(350, 130)
            window.maxsize(350, 130)
            window.mainloop()

    def studID(self):
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

            label2 = tkinter.Label(window, text='Student id not valid', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def bookID(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT bookID FROM LibraryManagementSystem.BooksDetails"
        myc.execute(sql)
        x = myc.fetchall()

        sql = "SELECT bookID FROM LibraryManagementSystem.IssuedInfo"
        myc.execute(sql)
        y = myc.fetchall()
        DataBase_connector.my_db.commit()

        li = [i[0] for i in x]
        li += [i[0] for i in y]

        if self.book_id_entry.get() in li:
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

            label2 = tkinter.Label(window, text='Book id not valid', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def find_difference_in_date(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT * FROM LibraryManagementSystem.IssuedInfo WHERE bookID=%s AND studID=%s"
        val = [self.book_id_entry.get(), self.stud_id_entry.get()]
        myc.execute(sql, val)
        x = myc.fetchall()
        DataBase_connector.my_db.commit()

        da = datetime.today()
        date = datetime.strptime(str(x[0][6]), '%d/%m/%y')
        actual_return_date = datetime.strftime(date, '%d/%m/%Y')
        today_date = datetime.strftime(da, '%d/%m/%Y')

        # actual_return_date = '30/08/2021'
        # today_date = '15/09/2021'
        # print(actual_return_date)
        # print(today_date)

        difference = get_diff().getDifference(actual_return_date, today_date)
        # print(difference)

        # difference = 11

        # if difference is less than or equal to zero then simply return book
        # or if difference is greater than zero then take fine from student
        if difference <= 0:
            returnBook_NoFine(x[0], self.staffID, self.RB)
        else:
            return_with_fine(x[0], self.staffID, self.RB, difference)


class returnBook_NoFine:

    def __init__(self, all_info, staffID, frame):
        self.RB = frame
        self.Rwindow = tkinter.Tk()
        self.Rwindow.title("Library Management System")
        self.Rwindow.geometry("400x600-484-100")
        self.Rwindow.config(bg="skyblue")
        self.Rwindow['pady'] = 5

        label = tkinter.Label(self.Rwindow, text="Issued information", bg='skyblue', fg='black', width=15)
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=5, family='Helvetica', weight='bold')

        info_name = ['Issue ID', 'Book ID', 'Copy NO.', 'Student ID', 'Issue Date', 'Issue Staff ID', 'Due Date']

        for i in range(7):
            label = tkinter.Label(self.Rwindow, text=info_name[i], bg='skyblue', fg='black', width=15)
            label.grid(row=i+1, column=1, sticky='W')
            label['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')

            label2 = tkinter.Label(self.Rwindow, text=all_info[i], bg='skyblue', fg='black', width=15)
            label2.grid(row=i+1, column=1, sticky='E')
            label2['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

        # ok button for destroy frame
        return_b = tkinter.Button(self.Rwindow, text="Return", activebackground='#FFA500',
                                  command=lambda: self.Delete_info_DB(all_info, staffID))
        return_b.grid(row=8, column=1)
        return_b['font'] = tkinter.font.Font(size=15)

        # configure row
        self.Rwindow.rowconfigure(0, weight=2)
        for i in range(1, 8):
            self.Rwindow.rowconfigure(i, weight=1)
        self.Rwindow.rowconfigure(8, weight=2)

        self.Rwindow.columnconfigure(0, weight=1)
        self.Rwindow.columnconfigure(1, weight=4)
        self.Rwindow.columnconfigure(2, weight=1)

        self.Rwindow.minsize(400, 600)
        self.Rwindow.maxsize(400, 600)
        self.Rwindow.mainloop()

    def Delete_info_DB(self, info, staffID):
        all_info = [i for i in info]
        date = datetime.today()
        return_date = datetime.strftime(date, '%d/%m/%y')
        all_info[7] = 'Yes'
        all_info[8] = return_date
        all_info[9] = staffID

        # ==============================================================================================================

        myc = DataBase_connector.my_db.cursor()

        sql = 'DELETE FROM LibraryManagementSystem.IssuedInfo WHERE bookID = %s AND studID = %s'
        val = [all_info[1], all_info[3]]
        myc.execute(sql, val)

        sql = "INSERT INTO LibraryManagementSystem.HistoryOfStudent(issueID, bookID, copyNO, studID, issueDate, issueStaffID, dueDate, isBookReturn, return_date, returnStaffID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = [all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5], all_info[6], all_info[7], all_info[8], all_info[9]]
        myc.execute(sql, val)

        sql = 'SELECT Available_copies FROM LibraryManagementSystem.BooksDetails WHERE BookID=%s'
        myc.execute(sql, [all_info[1]])
        x = myc.fetchall()

        Available_copies = x[0][0]

        if Available_copies == 0:
            sql = 'UPDATE LibraryManagementSystem.BooksDetails SET Availability = %s, Available_copies = %s WHERE BookID = %s'
            val = ['YES', 1, all_info[1]]
            myc.execute(sql, val)
        else:
            sql = 'UPDATE LibraryManagementSystem.BooksDetails SET Available_copies = %s WHERE BookID = %s'
            val = [Available_copies + 1, all_info[1]]
            myc.execute(sql, val)

        DataBase_connector.my_db.commit()

        # ==============================================================================================================

        self.window = tkinter.Tk()
        self.window.title("Library Management System")
        self.window.geometry("300x100-530-250")
        self.window.config(bg="black")
        self.window['pady'] = 20

        label = tkinter.Label(self.window, text='Book return Successfully!', bg="black", fg='white')
        label.pack()

        ok = tkinter.Button(self.window, text="OK", activebackground='#FFA500',
                            command=self.refresh)
        ok.pack(side='bottom', anchor='n')
        ok['font'] = tkinter.font.Font(size=15)

        self.window.minsize(300, 100)
        self.window.maxsize(300, 100)

        # self.window.after(2500, self.window.destroy)

        self.window.mainloop()

    def refresh(self):
        self.window.destroy()
        self.Rwindow.destroy()
        self.RB.destroy()


class return_with_fine:

    def __init__(self, all_info, staffID, frame, difference):
        self.RB = frame
        self.RFwindow = tkinter.Tk()
        self.RFwindow.title("Library Management System")
        self.RFwindow.geometry("450x600-459-100")
        self.RFwindow.config(bg="skyblue")
        self.RFwindow['pady'] = 5

        if 0 <= difference <= 10:
            fine = 50
        elif 11 <= difference <= 30:
            fine = 100
        else:
            fine = 200

        label = tkinter.Label(self.RFwindow, text="Issued information", bg='skyblue', fg='black', width=15)
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=5, family='Helvetica', weight='bold')

        info_name = ['Issue ID', 'Book ID', 'Copy NO.', 'Student ID', 'Issue Date', 'Issue Staff ID', 'Due Date']

        for i in range(7):
            label = tkinter.Label(self.RFwindow, text=info_name[i], bg='skyblue', fg='black', width=15)
            label.grid(row=i + 1, column=1, sticky='W')
            label['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')

            label2 = tkinter.Label(self.RFwindow, text=all_info[i], bg='skyblue', fg='black', width=15)
            label2.grid(row=i + 1, column=1, sticky='E')
            label2['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

        # fine label
        label = tkinter.Label(self.RFwindow, text='Fine', bg='skyblue', fg='black', width=15)
        label.grid(row=8, column=1, sticky='W')
        label['font'] = tkinter.font.Font(size=10, family='Helvetica', weight='bold')

        label2 = tkinter.Label(self.RFwindow, text=str(fine), bg='skyblue', fg='black', width=15)
        label2.grid(row=8, column=1, sticky='E')
        label2['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

        # ok button for destroy frame
        return_w_fine = tkinter.Button(self.RFwindow, text="Return With Fine", activebackground='#FFA500', width=15, command=lambda: self.Delete_info_with_fine(all_info, staffID, fine))
        return_w_fine.grid(row=9, column=1, sticky='W')
        return_w_fine['font'] = tkinter.font.Font(size=15)

        only_return = tkinter.Button(self.RFwindow, text="Return Only", activebackground='#FFA500', width=15, command=lambda: self.update_info(all_info, staffID, fine))
        only_return.grid(row=9, column=1, sticky='E')
        only_return['font'] = tkinter.font.Font(size=15)

        # configure row
        self.RFwindow.rowconfigure(0, weight=2)
        for i in range(1, 9):
            self.RFwindow.rowconfigure(i, weight=1)
        self.RFwindow.rowconfigure(9, weight=2)

        self.RFwindow.columnconfigure(0, weight=1)
        self.RFwindow.columnconfigure(1, weight=4)
        self.RFwindow.columnconfigure(2, weight=1)

        self.RFwindow.minsize(450, 600)
        self.RFwindow.maxsize(450, 600)
        self.RFwindow.mainloop()

    def Delete_info_with_fine(self, info, staffID, fine):
        all_info = [i for i in info]
        date = datetime.today()
        return_date = datetime.strftime(date, '%d/%m/%y')
        all_info[7] = 'Yes'
        all_info[8] = return_date
        all_info[9] = staffID
        all_info[10] = fine
        all_info[11] = 'Yes'
        all_info[12] = return_date
        all_info[13] = staffID

        # ==============================================================================================================

        myc = DataBase_connector.my_db.cursor()

        sql = 'DELETE FROM LibraryManagementSystem.IssuedInfo WHERE bookID = %s AND studID = %s'
        val = [all_info[1], all_info[3]]
        myc.execute(sql, val)

        sql = "INSERT INTO LibraryManagementSystem.HistoryOfStudent(issueID, bookID, copyNO, studID, issueDate, issueStaffID, dueDate, isBookReturn, return_date, returnStaffID, fine, isFinePaid, paymentDate, fineStaffID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = [all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5], all_info[6], all_info[7],
               all_info[8], all_info[9], all_info[10], all_info[11], all_info[12], all_info[13]]
        myc.execute(sql, val)

        sql = 'SELECT Available_copies FROM LibraryManagementSystem.BooksDetails WHERE BookID=%s'
        myc.execute(sql, [all_info[1]])
        x = myc.fetchall()

        Available_copies = x[0][0]

        if Available_copies == 0:
            sql = 'UPDATE LibraryManagementSystem.BooksDetails SET Availability = %s, Available_copies = %s WHERE BookID = %s'
            val = ['YES', 1, all_info[1]]
            myc.execute(sql, val)
        else:
            sql = 'UPDATE LibraryManagementSystem.BooksDetails SET Available_copies = %s WHERE BookID = %s'
            val = [Available_copies + 1, all_info[1]]
            myc.execute(sql, val)

        DataBase_connector.my_db.commit()

        # ==============================================================================================================

        self.window = tkinter.Tk()
        self.window.title("Library Management System")
        self.window.geometry("300x100-530-250")
        self.window.config(bg="black")
        self.window['pady'] = 20

        label = tkinter.Label(self.window, text='Book return Successfully!', bg="black", fg='white')
        label.pack()

        ok = tkinter.Button(self.window, text="OK", activebackground='#FFA500',
                            command=self.refresh)
        ok.pack(side='bottom', anchor='n')
        ok['font'] = tkinter.font.Font(size=15)

        self.window.minsize(300, 100)
        self.window.maxsize(300, 100)

        # self.window.after(2500, self.window.destroy)

        self.window.mainloop()

    def update_info(self, info, staffID, fine):
        all_info = [i for i in info]
        date = datetime.today()
        return_date = datetime.strftime(date, '%d/%m/%y')
        all_info[7] = 'Yes'
        all_info[8] = return_date
        all_info[9] = staffID

        # ==============================================================================================================

        myc = DataBase_connector.my_db.cursor()

        sql = 'UPDATE LibraryManagementSystem.IssuedInfo SET isBookReturn = %s, return_date = %s, returnStaffID = %s, fine = %s WHERE bookID = %s AND studID = %s'
        val = [all_info[7], all_info[8], all_info[9], fine, all_info[1], all_info[3]]
        myc.execute(sql, val)

        sql = 'SELECT Available_copies FROM LibraryManagementSystem.BooksDetails WHERE BookID=%s'
        myc.execute(sql, [all_info[1]])
        x = myc.fetchall()

        Available_copies = x[0][0]

        if Available_copies == 0:
            sql = 'UPDATE LibraryManagementSystem.BooksDetails SET Availability = %s, Available_copies = %s WHERE BookID = %s'
            val = ['YES', 1, all_info[1]]
            myc.execute(sql, val)
        else:
            sql = 'UPDATE LibraryManagementSystem.BooksDetails SET Available_copies = %s WHERE BookID = %s'
            val = [Available_copies + 1, all_info[1]]
            myc.execute(sql, val)

        DataBase_connector.my_db.commit()

        # ==============================================================================================================

        self.window = tkinter.Tk()
        self.window.title("Library Management System")
        self.window.geometry("300x100-530-250")
        self.window.config(bg="black")
        self.window['pady'] = 20

        label = tkinter.Label(self.window, text='Book return Successfully!', bg="black", fg='white')
        label.pack()

        ok = tkinter.Button(self.window, text="OK", activebackground='#FFA500',
                            command=self.refresh)
        ok.pack(side='bottom', anchor='n')
        ok['font'] = tkinter.font.Font(size=15)

        self.window.minsize(300, 100)
        self.window.maxsize(300, 100)

        # self.window.after(2500, self.window.destroy)

        self.window.mainloop()

    def refresh(self):
        self.window.destroy()
        self.RFwindow.destroy()
        self.RB.destroy()


class get_diff:
    def __init__(self):
        self.monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def countLeapYears(m, y):
        years = y

        # Check if the current year needs to be considered
        # for the count of leap years or not
        if m <= 2:
            years -= 1

        # An year is a leap year if it is a multiple of 4,
        # multiple of 400 and not a multiple of 100.
        return int(years / 4) - int(years / 100) + int(years / 400)

    def getDifference(self, actual_return_date, today_date):
        # COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1'

        dt1_d = int(actual_return_date[0:2])
        dt1_m = int(actual_return_date[3:5])
        dt1_y = int(actual_return_date[6:])

        # initialize count using years and day
        n1 = dt1_y * 365 + dt1_d

        # Add days for months in given date
        for i in range(0, dt1_m - 1):
            n1 += self.monthDays[i]

        # Since every leap year is of 366 days,
        # Add a day for every leap year
        n1 += self.countLeapYears(dt1_m, dt1_y)

        # SIMILARLY, COUNT TOTAL NUMBER OF DAYS BEFORE 'dt2'

        dt2_d = int(today_date[0:2])
        dt2_m = int(today_date[3:5])
        dt2_y = int(today_date[6:])

        n2 = dt2_y * 365 + dt2_d
        for i in range(0, dt2_m - 1):
            n2 += self.monthDays[i]
        n2 += self.countLeapYears(dt2_m, dt2_y)

        # return difference between two counts
        return n2 - n1
