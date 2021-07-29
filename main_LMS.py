import tkinter
from tkinter import font

from PIL import Image, ImageTk

import Add_Book_Details
import Delete_Book
import Update_Book_Details
import View_Books_List
import Issue_Book
import Return_Book


class mainWindow(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Library Management System")
        self.root.geometry('1000x700')
        self.root.config(bg='Black')

        img = ImageTk.PhotoImage(Image.open('lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img, width=250, height=500)
        panel.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open('lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img2, width=250, height=500)
        panel.grid(row=0, column=2)

        label = tkinter.Label(self.root, text='Library Management System', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=25, family='Helvetica')

        add_book = tkinter.Button(self.root, text='Add book Details', pady=10, width=30, activebackground='red',
                                  activeforeground='yellow', command=Add_Book_Details.add_book)
        add_book.grid(row=1, column=0, sticky='E')

        update_book = tkinter.Button(self.root, text='Update Book Details', pady=10, width=30, activebackground='red',
                                     activeforeground='yellow', command=Update_Book_Details.UpdateDetails)
        update_book.grid(row=1, column=1)

        delete_book = tkinter.Button(self.root, text='Delete Book', pady=10, width=30, activebackground='red',
                                     activeforeground='yellow', command=Delete_Book.Delete_Book)
        delete_book.grid(row=1, column=2, sticky='W')

        view_book_list = tkinter.Button(self.root, text='View Book List', pady=10, width=30, activebackground='red',
                                        activeforeground='yellow', command=View_Books_List.viewList)
        view_book_list.grid(row=2, column=0, sticky='E')

        issue_book = tkinter.Button(self.root, text='Issue Book', pady=10, width=30, activebackground='red',
                                    activeforeground='yellow', command=Issue_Book.IssueBook)
        issue_book.grid(row=2, column=1)

        return_book = tkinter.Button(self.root, text='Return Book', pady=10, width=30, activebackground='red',
                                     activeforeground='yellow', command=Return_Book.ReturnBook)
        return_book.grid(row=2, column=2, sticky='W')

        self.root.columnconfigure(0, weight=2)
        self.root.columnconfigure(1, weight=4)
        self.root.columnconfigure(2, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        self.root.minsize(1000, 700)
        self.root.maxsize(1000, 700)
        self.root.mainloop()


if __name__ == '__main__':
    mainWindow()
