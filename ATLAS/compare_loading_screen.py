# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from eigenvector_compare_method import Ui_EigenvectorCompareWindow
from eigenvalue_compare_method import Ui_EigenvalueCompareWindow
from PyQt5 import QtCore, QtWidgets, QtCore
from time import sleep
from closeWindow import QMainWindow
from os import walk
from det_compare_method import Ui_DetCompareWindow
from mult_compare_method import Ui_MultCompareWindow
from inverse_compare_method import Ui_InverseCompareWindow
from solving_compare_method import Ui_SolveCompareWindow

class Ui_CompLoadingWindow(object):
    def __init__(self, function, allMethods):
        self.function = function
        self.allMethods = allMethods

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
        self.start_button.setText("Generate Solutions")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def solutionGen(self):
        self.thread1 = ImageGen(self.allMethods)
        self.thread1.start()
        self.thread2 = ProgressUpdate(self.allMethods)
        self.thread2.change_value.connect(self.setProgressVal)
        self.thread2.start()

    def setProgressVal(self, val):
        self.progressBar.setValue(val)
        if val == 100:
            if self.function == "det":
                self.window = QMainWindow()
                self.ui = Ui_DetCompareWindow()
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
            elif self.function == "mult":
                self.window = QMainWindow()
                self.ui = Ui_MultCompareWindow()
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
            elif self.function == "inv":
                self.window = QMainWindow()
                self.ui = Ui_InverseCompareWindow()
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
            elif self.function == "solve":
                self.window = QMainWindow()
                self.ui = Ui_SolveCompareWindow()
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
            elif self.function == "e_val":
                self.window = QMainWindow()
                self.ui = Ui_EigenvalueCompareWindow()
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
            elif self.function == "e_vec":
                self.window = QMainWindow()
                self.ui = Ui_EigenvectorCompareWindow()
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()

class ImageGen(QtCore.QThread):
    def __init__(self, allMethods):
        super().__init__()
        self.allMethods = allMethods
    # Create a counter thread
    change_value = QtCore.pyqtSignal(int)
    def run(self):
        for method in self.allMethods:
            method.compare_latex2img()

class ProgressUpdate(QtCore.QThread):
    def __init__(self, allMethods):
        super().__init__()
        self.allMethods = allMethods

    # Create a counter thread
    change_value = QtCore.pyqtSignal(int)
    def run(self):
        percent = 0
        totalImages = 0
        for i in self.allMethods:
            totalImages += len(i.saved)
        while percent != 100.0:
            numImages = self.numberCurrImgs()
            new_percent = int((numImages/totalImages)*100)
            if new_percent > percent:
                sleep(0.3)
                percent = new_percent
                self.change_value.emit(percent)

    def numberCurrImgs(self):
        numImages = 0
        for _, _, files in walk("images"):
            numImages += len(files)
        return numImages

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CompLoadingWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())