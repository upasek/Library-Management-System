# # import webbrowser
# from threading import Thread
# import tkinter
# from selenium import webdriver
#
#
# class a:
#     @staticmethod
#     def open_page():
#         driver = webdriver.Chrome()
#         # webbrowser.open_new(r"https://www.paypal.com/paypalme/kiranupase123")
#         # print(webbrowser.)
#         url = "https://www.paypal.com/paypalme/kiranupase123"
#         driver.get(url)
#
#         driver.close()
#
#     def successful_window(self):
#         self.window = tkinter.Tk()
#         self.window.title("Library Management System")
#         self.window.geometry("300x100-530-250")
#         self.window.config(bg="black")
#         self.window['pady'] = 5
#
#         label = tkinter.Label(self.window, text="WARNING!", bg='black', fg='white')
#         label.pack(side='top')
#
#         label2 = tkinter.Label(self.window, text='pay.', bg='black', fg='white')
#         label2.pack(side='top')
#
#         # ok button for destroy frame
#         ok = tkinter.Button(self.window, text="OK", activebackground='#FFA500',
#                             command=self.window.destroy)
#         ok.pack(side='bottom', anchor='n')
#
#         self.window.minsize(300, 100)
#         self.window.maxsize(300, 100)
#         self.window.mainloop()
#
#     def open_both(self):
#         t = Thread(target=self.open_page)
#         t.start()
#
#         print(t.is_alive())
#
#
# ob = a()
# ob.open_both()


from selenium import webdriver

# Here Chrome  will be used
driver = webdriver.Chrome()

# URL of website
url = "https://www.geeksforgeeks.org/"

# Opening the website
driver.get(url)

# Closes the current window
driver.close()