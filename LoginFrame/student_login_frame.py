import smtplib
import tkinter
from random import randint
from tkinter import font

from PIL import Image, ImageTk

import Registration.student_registration
import Student_activity.main_frame_student
import DataBase_connector


class student_login:
    def __init__(self):
        self.S_frame = tkinter.Frame()
        self.S_frame.place(x=0, y=0, width=1000, height=700)
        self.S_frame.config(bg='black')

        img = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.S_frame, image=img, width=250, height=300)
        panel.grid(row=0, column=0)

        label = tkinter.Label(self.S_frame, text='STUDENT LOGIN', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=25, family='Helvetica')

        register_B = tkinter.Button(self.S_frame, text='Register Now', command=Registration.student_registration.Registration_S)
        register_B.grid(row=0, column=2)

        self.student_id = tkinter.Label(self.S_frame, text='STUDENT ID', bg='black', fg='white')
        self.student_id.grid(row=1, column=1, sticky='NW')
        self.student_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.student_id_entry = tkinter.Entry(self.S_frame)
        self.student_id_entry.grid(row=1, column=1, sticky='NE')

        self.__password = tkinter.Label(self.S_frame, text='PASSWORD', bg='black', fg='white')
        self.__password.grid(row=2, column=1, sticky='W')
        self.__password['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.__password_entry = tkinter.Entry(self.S_frame)
        self.__password_entry.grid(row=2, column=1, sticky='E')

        login_B = tkinter.Button(self.S_frame, text='LOGIN', pady=10, width=20, activebackground='red',
                                 activeforeground='yellow', command=self.checkInfo)
        login_B.grid(row=3, column=2, sticky='W')

        Quit = tkinter.Button(self.S_frame, text='QUIT', pady=10, width=20, activebackground='red',
                              activeforeground='yellow', command=self.S_frame.destroy)
        Quit.grid(row=3, column=1)

        forgot_P = tkinter.Button(self.S_frame, text='Forgot password', pady=10, width=20, activebackground='red',
                                  activeforeground='yellow', command=forgot_password)
        forgot_P.grid(row=3, column=0, sticky='E')

        self.S_frame.columnconfigure(0, weight=1)
        self.S_frame.columnconfigure(1, weight=1)
        self.S_frame.columnconfigure(2, weight=1)

        self.S_frame.rowconfigure(0, weight=1)
        self.S_frame.rowconfigure(1, weight=1)
        self.S_frame.rowconfigure(2, weight=1)
        self.S_frame.rowconfigure(3, weight=1)
        self.S_frame.rowconfigure(4, weight=1)

        self.S_frame.mainloop()

    def checkInfo(self):
        if self.student_id_entry.get() and self.__password_entry.get():
            self.checkInfoInDB()
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

    def checkInfoInDB(self):
        myc = DataBase_connector.my_db.cursor()

        sql = 'SELECT student_ID FROM LibraryManagementSystem.StudentLoginInfo'

        myc.execute(sql)

        result = myc.fetchall()

        sql = 'SELECT s_password FROM LibraryManagementSystem.StudentLoginInfo WHERE student_ID = %s'

        x = [self.student_id_entry.get()]

        myc.execute(sql, x)

        val = myc.fetchall()

        DataBase_connector.my_db.commit()

        list_SID = [i[0] for i in result]

        list_pass = [i[0] for i in val]

        if self.student_id_entry.get() in list_SID and self.__password_entry.get() in list_pass:
            Id = self.student_id_entry.get()
            self.student_id_entry.delete(0, 'end')
            self.__password_entry.delete(0, 'end')
            Student_activity.main_frame_student.student_loginFrame(Id)
        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-250")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please Enter valid staff ID and password.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()


class forgot_password:
    def __init__(self):
        self.mail = None
        self.random_val = None
        self.otp_entry = None
        self.new_pass_entry = None

        self.P_window = tkinter.Tk()
        self.P_window.title('Library Management System')
        self.P_window.geometry('500x400')
        self.P_window.config(bg='Black')

        label = tkinter.Label(self.P_window, text='We will send OTP on\nyour registered Gmail ID !', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=20, family='Helvetica', weight='bold')

        self.student_Id = tkinter.Label(self.P_window, text='STUDENT ID', bg='black', fg='white')
        self.student_Id.grid(row=1, column=1, sticky='NW')
        self.student_Id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.student_Id_entry = tkinter.Entry(self.P_window)
        self.student_Id_entry.grid(row=1, column=1, sticky='NE')

        Quit = tkinter.Button(self.P_window, text='QUIT', pady=10, width=10, activebackground='red',
                              activeforeground='yellow', command=self.P_window.destroy)
        Quit.grid(row=2, column=0, sticky='EN')

        send_otp = tkinter.Button(self.P_window, text='Send OTP', pady=10, width=10, activebackground='red',
                                  activeforeground='yellow', command=self.checkInfo)
        send_otp.grid(row=2, column=2, sticky='NW')

        self.P_window.rowconfigure(0, weight=1)
        self.P_window.rowconfigure(1, weight=1)
        self.P_window.rowconfigure(2, weight=1)

        self.P_window.columnconfigure(0, weight=1)
        self.P_window.columnconfigure(1, weight=2)
        self.P_window.columnconfigure(2, weight=1)

        self.P_window.mainloop()

    def checkInfo(self):
        if self.student_Id_entry.get():
            self.checkStaffID_DB()
        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-380")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please Enter student ID .', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def checkStaffID_DB(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT student_ID FROM LibraryManagementSystem.StudentLoginInfo"
        myc.execute(sql)
        result = myc.fetchall()
        li = [i[0] for i in result]
        DataBase_connector.my_db.commit()

        if self.student_Id_entry.get() in li:
            self.send_otp()
        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-380")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please Enter valid Student ID.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def send_otp(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT email_ID FROM LibraryManagementSystem.StudentLoginInfo WHERE student_ID=%s"
        val = [self.student_Id_entry.get()]

        myc.execute(sql, val)

        result = myc.fetchall()

        self.mail = result[0][0]

        DataBase_connector.my_db.commit()

        # ============================ Send OTP to student mail ID =======================

        ob = smtplib.SMTP('imap.gmail.com', 587)
        ob.starttls()
        ob.login("mailID@gmail.com", "password")
        subject = "Library Management System"
        self.random_val = randint(100000, 999999)
        message = 'Subject : {}\n\n{}'.format(subject, self.random_val)
        ob.sendmail("mailID@gmail.com", self.mail, message)
        # print("send successful..")
        ob.quit()

        self.otp_frame()

    def otp_frame(self):
        self.window = tkinter.Tk()
        self.window.title('Library Management System')
        self.window.geometry('400x200')
        self.window.config(bg='Black')

        label = tkinter.Label(self.window, text='Enter OTP !', bg="black", fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

        self.otp_entry = tkinter.Entry(self.window)
        self.otp_entry.grid(row=1, column=1,)

        ok_B = tkinter.Button(self.window, text="OK", pady=10, width=10, activebackground='red',
                              activeforeground='yellow', command=self.check_otp)
        ok_B.grid(row=2, column=1)

        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=2)
        self.window.columnconfigure(2, weight=1)

        # self.window.after(25000, self.window.destroy)

        self.window.mainloop()

    def check_otp(self):
        if int(self.random_val) == int(self.otp_entry.get()):
            self.window.destroy()
            self.otp_frame = tkinter.Tk()
            self.otp_frame.title('Library Management System')
            self.otp_frame.geometry('500x400')
            self.otp_frame.config(bg='Black')

            label = tkinter.Label(self.otp_frame, text='Enter New Password !', bg='black', fg='white')
            label.grid(row=0, column=1)
            label['font'] = tkinter.font.Font(size=30, family='Helvetica', weight='bold')

            new_pass = tkinter.Label(self.otp_frame, text='New Password', bg='black', fg='white')
            new_pass.grid(row=1, column=1, sticky='WN')
            new_pass['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            self.new_pass_entry = tkinter.Entry(self.otp_frame)
            self.new_pass_entry.grid(row=1, column=1, sticky='EN')

            cancel = tkinter.Button(self.otp_frame, text='Cancel', pady=10, width=5, activebackground='red',
                                    activeforeground='yellow', command=self.otp_frame.destroy)
            cancel.grid(row=2, column=0, sticky='EN')

            update = tkinter.Button(self.otp_frame, text='Update', pady=10, width=5, activebackground='red',
                                    activeforeground='yellow', command=self.check_new_password)
            update.grid(row=2, column=2, sticky='NW')

            self.otp_frame.rowconfigure(0, weight=1)
            self.otp_frame.rowconfigure(1, weight=1)
            self.otp_frame.rowconfigure(2, weight=1)

            self.otp_frame.columnconfigure(0, weight=1)
            self.otp_frame.columnconfigure(1, weight=3)
            self.otp_frame.columnconfigure(2, weight=1)

            self.otp_frame.mainloop()

        else:
            self.window.destroy()
            new_password = tkinter.Tk()
            new_password.title('Library Management System')
            new_password.geometry('300x100')
            new_password.config(bg='Black')

            label = tkinter.Label(new_password, text='invalid otp !', bg='black', fg='white')
            label.grid(row=1, column=1)
            label['font'] = tkinter.font.Font(size=60, family='Helvetica', weight='bold')

            ok = tkinter.Button(new_password, text='OK', pady=5, width=2, activebackground='red',
                                activeforeground='yellow', command=new_password.destroy)
            ok.grid(row=2, column=1)

            new_password.rowconfigure(0, weight=1)
            new_password.rowconfigure(1, weight=1)
            new_password.rowconfigure(2, weight=1)

            new_password.columnconfigure(0, weight=1)
            new_password.columnconfigure(1, weight=3)
            new_password.columnconfigure(2, weight=1)

            new_password.mainloop()

    def check_new_password(self):
        if self.new_pass_entry.get():
            # print([self.new_pass_entry.get(), self.staff_Id_entry.get()])
            myc = DataBase_connector.my_db.cursor()
            sql = "UPDATE LibraryManagementSystem.StudentLoginInfo SET s_password = %s WHERE (student_ID = %s AND sr_no <> %s)"
            val_x = [str(self.new_pass_entry.get()), str(self.student_Id_entry.get()), 0]

            myc.execute(sql, val_x)

            DataBase_connector.my_db.commit()

            self.ok_frame = tkinter.Tk()
            self.ok_frame.title('Library Management System')
            self.ok_frame.geometry('300x100')
            self.ok_frame.config(bg='Black')

            label = tkinter.Label(self.ok_frame, text='Password Updated !', bg='black', fg='white')
            label.grid(row=1, column=1)
            label['font'] = tkinter.font.Font(size=60, family='Helvetica', weight='bold')

            ok = tkinter.Button(self.ok_frame, text='OK', pady=5, width=2, activebackground='red',
                                activeforeground='yellow', command=self.delete_frames)
            ok.grid(row=2, column=1)

            self.ok_frame.rowconfigure(0, weight=1)
            self.ok_frame.rowconfigure(1, weight=1)
            self.ok_frame.rowconfigure(2, weight=1)

            self.ok_frame.columnconfigure(0, weight=1)
            self.ok_frame.columnconfigure(1, weight=3)
            self.ok_frame.columnconfigure(2, weight=1)

            self.ok_frame.mainloop()

        else:
            new_password = tkinter.Tk()
            new_password.title('Library Management System')
            new_password.geometry('300x100')
            new_password.config(bg='Black')

            label = tkinter.Label(new_password, text='Please Enter New Password!', bg='black', fg='white')
            label.grid(row=1, column=1)
            label['font'] = tkinter.font.Font(size=60, family='Helvetica', weight='bold')

            ok = tkinter.Button(new_password, text='OK', pady=5, width=2, activebackground='red',
                                activeforeground='yellow', command=new_password.destroy)
            ok.grid(row=2, column=1)

            new_password.rowconfigure(0, weight=1)
            new_password.rowconfigure(1, weight=1)
            new_password.rowconfigure(2, weight=1)

            new_password.columnconfigure(0, weight=1)
            new_password.columnconfigure(1, weight=3)
            new_password.columnconfigure(2, weight=1)

            new_password.mainloop()

    def delete_frames(self):
        self.ok_frame.destroy()
        self.otp_frame.destroy()
        self.P_window.destroy()
