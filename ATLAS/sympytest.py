# # print(10.0**20)
# # print(1+10.0**20)
# # print((1+10.0**20)-10.0**20)
# # print(1+(10.0**20-10.0**20))

# import logging
# from operator import mul
# import threading
# import time


# from PyQt5 import QtGui
# from PyQt5.QtWidgets import QApplication, QDialog, QProgressBar, QPushButton, QVBoxLayout
# import sys
# from PyQt5.QtCore import Qt, QThread, pyqtSignal
# import time
# from multiplication import naiveMultiplication
# import sympy as sp
# from emptyimg import empty
# from os import listdir
# import saver

# class MyThread(QThread):
#     def __init__(self, mult, parent: None):
#         super().__init__(parent=parent)
#         self.mult = mult
#     # Create a counter thread
#     change_value = pyqtSignal(int)
#     def run(self):
#         self.mult.latex2img()

# class MyString(QThread):
#     # Create a counter thread
#     change_value = pyqtSignal(int)
#     def run(self):
#         percent = 0
#         while percent != 100.0:
#             numSaved = len(saver.saved)
#             images = listdir("images")
#             numImages = len(images)
#             new_percent = int((numImages/numSaved)*100)
#             if new_percent > percent:
#                 time.sleep(0.3)
#                 percent = new_percent
#                 self.change_value.emit(percent)
# class Window(QDialog):
#     def __init__(self, mult):
#         super().__init__()
#         self.mult = mult
#         self.title = "PyQt5 ProgressBar"
#         self.top = 200
#         self.left = 500
#         self.width = 300
#         self.height = 100
#         self.setWindowIcon(QtGui.QIcon("icon.png"))
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         vbox = QVBoxLayout()
#         self.progressbar = QProgressBar()
#         #self.progressbar.setOrientation(Qt.Vertical)
#         self.progressbar.setMaximum(100)
#         self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}"
#                                        "QProgressBar::chunk {background:yellow}")
#         #qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
#         #self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white); }")
#         #self.progressbar.setTextVisible(False)
#         vbox.addWidget(self.progressbar)
#         self.button = QPushButton("Start Progressbar")
#         self.button.setStyleSheet('background-color:yellow')
#         self.button.clicked.connect(self.startProgressBar)
#         vbox.addWidget(self.button)
#         self.setLayout(vbox)
#         self.show()

#     def startProgressBar(self):
#         self.thread = MyThread(self.mult, parent=None)
#         self.thread.start()
#         self.thread_new = MyString()
#         self.thread_new.change_value.connect(self.setProgressVal)
#         self.thread_new.start()

#     def setProgressVal(self, val):
#         self.progressbar.setValue(val)


# a = sp.Matrix([[1,3],[4,5]])
# b = sp.Matrix([[1,3],[6,9]])
# mult = naiveMultiplication(a, b)
# empty()
# mult.calc()
# mult.addSaved(True)
# App = QApplication(sys.argv)
# window = Window(mult)
# sys.exit(App.exec())