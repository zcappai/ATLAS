# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function_screen - Copy.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from single_method_choice import Ui_SingleChoiceWindow
from mult_compare_method import Ui_MultCompareWindow
from os import mkdir
from multiplication import getMethods
from compare_emptyimg import empty
from closeWindow import QMainWindow

class Ui_SingleCompWindow(object):
    def __init__(self, arg, method):
        self.arg = arg
        self.method = method

    def setupUi(self, SingleCompWindow):
        self.SingleCompWindow = SingleCompWindow
        SingleCompWindow.setObjectName("SingleCompWindow")
        SingleCompWindow.resize(1110, 831)
        self.centralwidget = QtWidgets.QWidget(SingleCompWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 1, 1, 1)
        self.comparison_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.comparison_button.setFont(font)
        self.comparison_button.setObjectName("comparison_button")
        self.comparison_button.clicked.connect(self.toCompare)
        self.gridLayout.addWidget(self.comparison_button, 4, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 3, 1, 1, 1)
        self.one_option_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.one_option_button.setFont(font)
        self.one_option_button.setObjectName("one_option_button")
        self.one_option_button.clicked.connect(self.toSingle)
        self.gridLayout.addWidget(self.one_option_button, 4, 1, 1, 1)
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setMinimumSize(QtCore.QSize(0, 50))
        self.back_button.setMaximumSize(QtCore.QSize(50, 16777215))
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 0, 0, 2, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        SingleCompWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SingleCompWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        SingleCompWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SingleCompWindow)
        self.statusbar.setObjectName("statusbar")
        SingleCompWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SingleCompWindow)
        QtCore.QMetaObject.connectSlotsByName(SingleCompWindow)

    def retranslateUi(self, SingleCompWindow):
        _translate = QtCore.QCoreApplication.translate
        SingleCompWindow.setWindowTitle(_translate("SingleCompWindow", "SingleCompWindow"))
        self.comparison_button.setText(_translate("SingleCompWindow", "Comparison"))
        self.label.setText(_translate("SingleCompWindow", "Select one of the options:\n"
"\"One Method\" allows you to choose a single method to use\n"
"\"Comparison\" allows you to compare all the methods available."))
        self.one_option_button.setText(_translate("SingleCompWindow", "One Method"))
        self.back_button.setText(_translate("SingleCompWindow", "Go Back"))

    def toSingle(self):
        self.window = QMainWindow()
        self.ui = Ui_SingleChoiceWindow(self.arg, self.method)
        self.ui.setupUi(self.window)
        self.SingleCompWindow.hide()
        self.window.showMaximized()

    def toCompare(self):
        empty()
        self.window = QMainWindow()
        if self.method == "mult":
            self.compareMult()
            self.ui = Ui_MultCompareWindow()
        self.ui.setupUi(self.window)
        self.SingleCompWindow.hide()
        self.window.showMaximized()

    def compareMult(self):
        methods = getMethods()
        for (i, j) in methods:
            mkdir("multiple-images/{}/".format(i))
            current_method = j(*self.arg)
            current_method.calc()
            current_method.compare_latex2img(i)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SingleCompWindow = QMainWindow()
    ui = Ui_SingleCompWindow(None, "mult")
    ui.setupUi(SingleCompWindow)
    SingleCompWindow.show()
    sys.exit(app.exec_())
