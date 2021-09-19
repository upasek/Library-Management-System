import tkinter
import smtplib
from random import randint
from tkinter import font
from PIL import Image, ImageTk
import DataBase_connector


class change_password:
    def __init__(self, staffID):
        self.new_pass_entry = None
        self.otp_entry = None
        self.random_val = None
        self.mail = None

        self.SI = staffID
        self.P_window = tkinter.Frame()
        self.P_window.place(x=0, y=0, width=1000, height=700)
        self.P_window.config(bg='black')

        label = tkinter.Label(self.P_window, text='We will send OTP on\nyour registered Gmail ID !', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=20, family='Helvetica', weight='bold')

        img = ImageTk.PhotoImage(Image.open("Images/lib1.jpeg"))
        pan = tkinter.Label(self.P_window, image=img, width=250, height=400)
        pan.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open("Images/lib1.jpeg"))
        pan = tkinter.Label(self.P_window, image=img2, width=250, height=400)
        pan.grid(row=0, column=2)

        # self.staff_Id = tkinter.Label(self.P_window, text='STAFF ID', bg='black', fg='white')
        # self.staff_Id.grid(row=1, column=1, sticky='NW')
        # self.staff_Id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        # self.staff_Id_entry = tkinter.Entry(self.P_window)
        # self.staff_Id_entry.grid(row=1, column=1, sticky='NE')

        Quit = tkinter.Button(self.P_window, text='QUIT', pady=10, width=10, activebackground='red',
                              activeforeground='yellow', command=self.P_window.destroy)
        Quit.grid(row=2, column=1, sticky='NW')

        send_otp = tkinter.Button(self.P_window, text='Send OTP', pady=10, width=10, activebackground='red',
                                  activeforeground='yellow', command=self.send_otp)
        send_otp.grid(row=2, column=1, sticky='NE')

        self.P_window.rowconfigure(0, weight=1)
        self.P_window.rowconfigure(1, weight=1)
        self.P_window.rowconfigure(2, weight=1)

        self.P_window.columnconfigure(0, weight=1)
        self.P_window.columnconfigure(1, weight=2)
        self.P_window.columnconfigure(2, weight=1)

        self.P_window.mainloop()

    def send_otp(self):
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT email_ID FROM LibraryManagementSystem.StaffLoginInfo WHERE staff_ID=%s"
        val = [self.SI]

        myc.execute(sql, val)

        result = myc.fetchall()

        self.mail = result[0][0]

        DataBase_connector.my_db.commit()

        # ============================ Send OTP to staff mail ID =======================

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
            sql = "UPDATE LibraryManagementSystem.StaffLoginInfo SET s_password = %s WHERE (staff_ID = %s AND sr_no <> %s)"
            val_x = [str(self.new_pass_entry.get()), str(self.SI), 0]

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
