# -*- coding: utf-8 -*-

# import tkinter as tk
#
# # 主窗体
# mainForm = tk.Tk()
# # 设置窗体title
# mainForm.wm_title("this is my first python gui programme")
#
#
# mainForm.mainloop()

# from tkinter import *
# import tkMessageBox
#
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         tkMessageBox.showinfo('Message', 'Hello, %s' % name)
#
#
# app = Application()
# app.master.title("title")
# app.mainloop()

import sys
from PyQt4 import QtGui
from PyQt4 import QtOpenGL

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(800, 600)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())
