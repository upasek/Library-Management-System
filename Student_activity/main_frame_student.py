import tkinter
from tkinter import font
from PIL import Image, ImageTk

import Student_activity.Update_Profile
import Student_activity.Change_Password
import Student_activity.Book_record
import Student_activity.Pay_fine


class student_loginFrame:
    def __init__(self, studID):
        self.root = tkinter.Frame()
        self.root.place(x=0, y=0, width=1000, height=700)
        self.root.config(bg='black')

        log_out = tkinter.Button(self.root, text='Log Out', pady=10, width=10, activebackground='red',
                                 activeforeground='yellow', command=self.root.destroy)
        log_out.grid(row=0, column=2, sticky='NE')

        img = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img, width=200, height=390)
        panel.grid(row=0, column=0, sticky='S')

        img2 = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img2, width=200, height=390)
        panel.grid(row=0, column=2, sticky='S')

        label = tkinter.Label(self.root, text='Library Management System', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=25, family='Helvetica')

        book_record = tkinter.Button(self.root, text='Books Records', pady=10, width=25, activebackground='red',
                                     activeforeground='yellow',
                                     command=lambda: Student_activity.Book_record.bookRecord(studID))
        book_record.grid(row=2, column=1, sticky='W')

        pay_fine = tkinter.Button(self.root, text='Pay Fine', pady=10, width=25, activebackground='red',
                                  activeforeground='yellow',
                                  command=lambda: Student_activity.Pay_fine.PayFine(studID))
        pay_fine.grid(row=2, column=1, sticky='E')

        update_Profile = tkinter.Button(self.root, text='Update Profile', pady=10, width=25, activebackground='red',
                                        activeforeground='yellow',
                                        command=lambda: Student_activity.Update_Profile.update_profile(studID))
        update_Profile.grid(row=3, column=1, sticky='W')

        change_password = tkinter.Button(self.root, text='Change Password', pady=10, width=25, activebackground='red',
                                         activeforeground='yellow',
                                         command=lambda: Student_activity.Change_Password.change_password(studID))
        change_password.grid(row=3, column=1, sticky='E')

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(2, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)

        self.root.mainloop()
