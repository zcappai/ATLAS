# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets, QtCore
import time
from closeWindow import QMainWindow
from os import listdir
import saver


class Ui_LoadingWindow(object):
    def __init__(self, method, view_screen):
        self.method = method
        self.view_screen = view_screen

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 126)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 1, 0, 1, 1)
        self.start_button.clicked.connect(self.solutionGen)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("ATLAS")
        self.start_button.setText("Generate Solution")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "ATLAS"))
    #     self.start_button.setText(_translate("MainWindow", "Generate Solution"))

    def solutionGen(self):
        self.thread1 = ImageGen(self.method)
        self.thread1.start()
        self.thread2 = ProgressUpdate()
        self.thread2.change_value.connect(self.setProgressVal)
        self.thread2.start()

    def setProgressVal(self, val):
        self.progressBar.setValue(val)
        if val == 100:
            self.window = QMainWindow()
            self.ui = self.view_screen
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()

class ImageGen(QtCore.QThread):
    def __init__(self, method):
        super().__init__()
        self.method = method
    # Create a counter thread
    change_value = QtCore.pyqtSignal(int)
    def run(self):
        self.method.latex2img()

class ProgressUpdate(QtCore.QThread):
    # Create a counter thread
    change_value = QtCore.pyqtSignal(int)
    def run(self):
        percent = 0
        while percent != 100.0:
            numSaved = len(saver.saved)
            images = listdir("images")
            numImages = len(images)
            new_percent = int((numImages/numSaved)*100)
            if new_percent > percent:
                time.sleep(0.3)
                percent = new_percent
                self.change_value.emit(percent)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoadingWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())