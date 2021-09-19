import tkinter
from tkinter import font
from PIL import Image, ImageTk

import Staff_activity.Add_Book_Details
import Staff_activity.Delete_Book
import Staff_activity.Update_Book_Details
import Staff_activity.View_Books_List
import Staff_activity.Issue_Book
import Staff_activity.Return_Book
import Staff_activity.Update_Profile
import Staff_activity.Change_Password
import Staff_activity.Students_Records


class staff_loginFrame:
    def __init__(self, staffID):
        self.root = tkinter.Frame()
        self.root.place(x=0, y=0, width=1000, height=700)
        self.root.config(bg='black')

        log_out = tkinter.Button(self.root, text='Log Out', pady=10, width=10, activebackground='red', activeforeground='yellow', command=self.root.destroy)
        log_out.grid(row=0, column=2, sticky='NE')

        img = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img, width=250, height=350)
        panel.grid(row=0, column=0, sticky='S')

        img2 = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img2, width=250, height=350)
        panel.grid(row=0, column=2, sticky='S')

        label = tkinter.Label(self.root, text='Library Management System', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=25, family='Helvetica')

        add_book = tkinter.Button(self.root, text='Add book Details', pady=10, width=30, activebackground='red',
                                  activeforeground='yellow', command=Staff_activity.Add_Book_Details.add_book)
        add_book.grid(row=1, column=0, sticky='E')

        update_book = tkinter.Button(self.root, text='Update Book Details', pady=10, width=30, activebackground='red',
                                     activeforeground='yellow', command=Staff_activity.Update_Book_Details.UpdateDetails)
        update_book.grid(row=1, column=1)

        delete_book = tkinter.Button(self.root, text='Delete Book', pady=10, width=30, activebackground='red',
                                     activeforeground='yellow', command=Staff_activity.Delete_Book.Delete_Book)
        delete_book.grid(row=1, column=2, sticky='W')

        view_book_list = tkinter.Button(self.root, text='View Book List', pady=10, width=30, activebackground='red',
                                        activeforeground='yellow', command=Staff_activity.View_Books_List.viewList)
        view_book_list.grid(row=2, column=0, sticky='E')

        issue_book = tkinter.Button(self.root, text='Issue Book', pady=10, width=30, activebackground='red',
                                    activeforeground='yellow', command=lambda: Staff_activity.Issue_Book.IssueBook(staffID))
        issue_book.grid(row=2, column=1)

        return_book = tkinter.Button(self.root, text='Return Book', pady=10, width=30, activebackground='red',
                                     activeforeground='yellow', command=lambda: Staff_activity.Return_Book.ReturnBook(staffID))
        return_book.grid(row=2, column=2, sticky='W')

        student_records = tkinter.Button(self.root, text='Student Record', pady=10, width=30, activebackground='red',
                                         activeforeground='yellow', command=lambda: Staff_activity.Students_Records.studentsRecords(staffID))
        student_records.grid(row=3, column=0, sticky='E')

        update_details = tkinter.Button(self.root, text='Update Profile', pady=10, width=30, activebackground='red',
                                        activeforeground='yellow', command=lambda: Staff_activity.Update_Profile.update_profile(staffID))
        update_details.grid(row=3, column=1)

        change_password = tkinter.Button(self.root, text='Change Password', pady=10, width=30, activebackground='red',
                                         activeforeground='yellow', command=lambda: Staff_activity.Change_Password.change_password(staffID))
        change_password.grid(row=3, column=2, sticky='W')

        self.root.columnconfigure(0, weight=2)
        self.root.columnconfigure(1, weight=4)
        self.root.columnconfigure(2, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)

        self.root.mainloop()
