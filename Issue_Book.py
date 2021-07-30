import tkinter
import tkinter.font
from PIL import Image, ImageTk


class IssueBook:

    def __init__(self):
        self.IB = tkinter.Frame()
        self.IB.place(x=0, y=0, width=1000, height=700)
        self.IB.config(bg='black')

        img = ImageTk.PhotoImage(Image.open("lib1.jpeg"))
        pan = tkinter.Label(self.IB, image=img, width=250, height=250)
        pan.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open("lib1.jpeg"))
        pan = tkinter.Label(self.IB, image=img2, width=250, height=250)
        pan.grid(row=0, column=2)

        label = tkinter.Label(self.IB, text='Issue Book', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        book_id = tkinter.Label(self.IB, text='Book ID', fg='white', bg='black')
        book_id.grid(row=1, column=1, sticky='W')
        book_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        book_id_entry = tkinter.Entry(self.IB)
        book_id_entry.grid(row=1, column=1, sticky='E')

        stud_id = tkinter.Label(self.IB, text='Student ID', fg='white', bg='black')
        stud_id.grid(row=2, column=1, sticky='W')
        stud_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        stud_id_entry = tkinter.Entry(self.IB)
        stud_id_entry.grid(row=2, column=1, sticky='E')

        issueDate = tkinter.Label(self.IB, text='Issue Date', fg='white', bg='black')
        issueDate.grid(row=3, column=1, sticky='W')
        issueDate['font'] = tkinter.font.Font(size=15, family='Helvetica')
        issueDate_entry = tkinter.Entry(self.IB)
        issueDate_entry.grid(row=3, column=1, sticky='E')

        quit_b = tkinter.Button(self.IB, text='Quit', command=self.IB.destroy)
        quit_b.grid(row=4, column=0, sticky='NE')
        quit_b['font'] = tkinter.font.Font(size=10)

        issue_b = tkinter.Button(self.IB, text='Issue')
        issue_b.grid(row=4, column=2, sticky='NW')
        issue_b['font'] = tkinter.font.Font(size=10)

        self.IB.rowconfigure(0, weight=1)
        self.IB.rowconfigure(1, weight=1)
        self.IB.rowconfigure(2, weight=1)
        self.IB.rowconfigure(3, weight=1)
        self.IB.rowconfigure(4, weight=1)

        self.IB.columnconfigure(0, weight=1)
        self.IB.columnconfigure(1, weight=1)
        self.IB.columnconfigure(2, weight=1)

        self.IB.mainloop()
