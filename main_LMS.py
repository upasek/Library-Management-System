import tkinter
from tkinter import font
from PIL import Image, ImageTk

import LoginFrame.staff_login_frame
import LoginFrame.student_login_frame


class mainWindow(object):

    def __init__(self):

        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("Library Management System")
        self.mainWindow.geometry('1000x700')
        self.mainWindow.config(bg='Black')

        img = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.mainWindow, image=img, width=250, height=500)
        panel.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.mainWindow, image=img2, width=250, height=500)
        panel.grid(row=0, column=2)

        label = tkinter.Label(self.mainWindow, text='Library Management System', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=25, family='Helvetica')

        admin_login = tkinter.Button(self.mainWindow, text='STAFF LOGIN', pady=10, width=20, activebackground='red', activeforeground='yellow', command=LoginFrame.staff_login_frame.staff_login)
        admin_login.grid(row=0, column=1, sticky='WS')

        stud_login = tkinter.Button(self.mainWindow, text='STUDENT LOGIN', pady=10, width=20, activebackground='red', activeforeground='yellow', command=LoginFrame.student_login_frame.student_login)
        stud_login.grid(row=0, column=1, sticky='ES')

        self.mainWindow.columnconfigure(0, weight=1)
        self.mainWindow.columnconfigure(1, weight=2)
        self.mainWindow.columnconfigure(2, weight=1)

        self.mainWindow.rowconfigure(0, weight=1)
        self.mainWindow.rowconfigure(1, weight=1)
        self.mainWindow.rowconfigure(2, weight=1)

        self.mainWindow.minsize(1000, 700)
        self.mainWindow.maxsize(1000, 700)

        self.mainWindow.mainloop()


if __name__ == '__main__':
    mainWindow()
