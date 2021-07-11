# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solving_size.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from solving_input import Ui_SolveInWindow
from closeWindow import QMainWindow

class Ui_SolveSizeWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 871)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 4, 1, 1)
        self.mul_size_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mul_size_info.setFont(font)
        self.mul_size_info.setWordWrap(True)
        self.mul_size_info.setObjectName("mul_size_info")
        self.gridLayout.addWidget(self.mul_size_info, 0, 0, 1, 5)
        self.equations = QtWidgets.QSpinBox(self.centralwidget)
        self.equations.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.equations.setFont(font)
        self.equations.setAlignment(QtCore.Qt.AlignCenter)
        self.equations.setObjectName("equations")
        self.gridLayout.addWidget(self.equations, 4, 1, 1, 1)
        self.unknowns = QtWidgets.QSpinBox(self.centralwidget)
        self.unknowns.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.unknowns.setFont(font)
        self.unknowns.setAlignment(QtCore.Qt.AlignCenter)
        self.unknowns.setObjectName("unknowns")
        self.gridLayout.addWidget(self.unknowns, 4, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 5)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMinimumSize(QtCore.QSize(125, 50))
        self.submit.setMaximumSize(QtCore.QSize(125, 16777215))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.sendSizes)
        self.gridLayout.addWidget(self.submit, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATLAS"))
        self.mul_size_info.setText(_translate("MainWindow", "In the 2 boxes below, choose the number of equations you wish to enter and the number of unknowns in those equations."))
        self.label.setText(_translate("MainWindow", "Equations"))
        self.label_2.setText(_translate("MainWindow", "Unknowns"))
        self.submit.setText(_translate("MainWindow", "Submit"))

    def sendSizes(self):
        self.window = QMainWindow()
        self.ui = Ui_SolveInWindow(self.equations.value(), self.unknowns.value())
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_SolveSizeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
