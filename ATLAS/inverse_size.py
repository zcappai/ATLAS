# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inverse_size.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from inverse_input import Ui_InverseInWindow
from closeWindow import QMainWindow

class Ui_InverseSizeWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 871)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mult_size_info2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mult_size_info2.setFont(font)
        self.mult_size_info2.setWordWrap(True)
        self.mult_size_info2.setObjectName("mult_size_info2")
        self.gridLayout.addWidget(self.mult_size_info2, 1, 0, 1, 5)
        self.mult_size_info3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mult_size_info3.setFont(font)
        self.mult_size_info3.setWordWrap(True)
        self.mult_size_info3.setObjectName("mult_size_info3")
        self.gridLayout.addWidget(self.mult_size_info3, 2, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.mul_size_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mul_size_info.setFont(font)
        self.mul_size_info.setWordWrap(True)
        self.mul_size_info.setObjectName("mul_size_info")
        self.gridLayout.addWidget(self.mul_size_info, 0, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        self.size = QtWidgets.QSpinBox(self.centralwidget)
        self.size.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.size.setFont(font)
        self.size.setAlignment(QtCore.Qt.AlignCenter)
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 5, 2, 1, 1)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMinimumSize(QtCore.QSize(125, 50))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.sendSize) ################
        self.gridLayout.addWidget(self.submit, 6, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 7, 2, 1, 1)
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
        self.mult_size_info2.setText(_translate("MainWindow", "Remember, the inverse of a matrix can only be calculated for a square matrix, which is a matrix that has the same number of elements along its width and height."))
        self.mult_size_info3.setText(_translate("MainWindow", "e.g. if you enter the number 4, the matrix must be of size 4x4."))
        self.mul_size_info.setText(_translate("MainWindow", "Use the box below to choose what size matrix you wish to enter."))
        self.submit.setText(_translate("MainWindow", "Submit"))

    def sendSize(self):
        self.window = QMainWindow()
        self.ui = Ui_InverseInWindow(self.size.value())
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_InverseSizeWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
