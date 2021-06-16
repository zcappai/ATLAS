# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiplication_size.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from multiplication_input import Ui_MultInWindow


class Ui_MultSizeWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 871)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mult_size_info3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mult_size_info3.setFont(font)
        self.mult_size_info3.setWordWrap(True)
        self.mult_size_info3.setObjectName("mult_size_info3")
        self.gridLayout.addWidget(self.mult_size_info3, 2, 0, 1, 7)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMinimumSize(QtCore.QSize(125, 50))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.sendSizes)
        self.gridLayout.addWidget(self.submit, 7, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 6, 1, 1)
        self.shareddim_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.shareddim_label.setFont(font)
        self.shareddim_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shareddim_label.setObjectName("shareddim_label")
        self.gridLayout.addWidget(self.shareddim_label, 4, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.mult_size_info2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mult_size_info2.setFont(font)
        self.mult_size_info2.setWordWrap(True)
        self.mult_size_info2.setObjectName("mult_size_info2")
        self.gridLayout.addWidget(self.mult_size_info2, 1, 0, 1, 7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        self.leftmatrixdim = QtWidgets.QSpinBox(self.centralwidget)
        self.leftmatrixdim.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.leftmatrixdim.setFont(font)
        self.leftmatrixdim.setAlignment(QtCore.Qt.AlignCenter)
        self.leftmatrixdim.setObjectName("leftmatrixdim")
        self.gridLayout.addWidget(self.leftmatrixdim, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 4, 1, 1)
        self.rightmatrixdim_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.rightmatrixdim_label.setFont(font)
        self.rightmatrixdim_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rightmatrixdim_label.setObjectName("rightmatrixdim_label")
        self.gridLayout.addWidget(self.rightmatrixdim_label, 4, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 8, 3, 1, 1)
        self.mul_size_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mul_size_info.setFont(font)
        self.mul_size_info.setWordWrap(True)
        self.mul_size_info.setObjectName("mul_size_info")
        self.gridLayout.addWidget(self.mul_size_info, 0, 0, 1, 7)
        self.rightmatrixdim = QtWidgets.QSpinBox(self.centralwidget)
        self.rightmatrixdim.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.rightmatrixdim.setFont(font)
        self.rightmatrixdim.setAlignment(QtCore.Qt.AlignCenter)
        self.rightmatrixdim.setObjectName("rightmatrixdim")
        self.gridLayout.addWidget(self.rightmatrixdim, 5, 5, 1, 1)
        self.leftmatrixdim_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.leftmatrixdim_label.setFont(font)
        self.leftmatrixdim_label.setAlignment(QtCore.Qt.AlignCenter)
        self.leftmatrixdim_label.setObjectName("leftmatrixdim_label")
        self.gridLayout.addWidget(self.leftmatrixdim_label, 4, 1, 1, 1)
        self.shareddim = QtWidgets.QSpinBox(self.centralwidget)
        self.shareddim.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.shareddim.setFont(font)
        self.shareddim.setAlignment(QtCore.Qt.AlignCenter)
        self.shareddim.setObjectName("shareddim")
        self.gridLayout.addWidget(self.shareddim, 5, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 3, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mult_size_info3.setText(_translate("MainWindow", "e.g. a matrix with 1 row and 3 columns (1*3) would be compatible with a matrix with 3 rows and 6 columns (3*6), resulting in a matrix with 1 row and 6 columns."))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.shareddim_label.setText(_translate("MainWindow", "n"))
        self.mult_size_info2.setText(_translate("MainWindow", "Therefore, given 2 matrices with dimensions m*n and n*p. The dimension n must be the same for both matrices. Remember that the dimenions of a matrix are represented as \"number of rows\"*\"number of columns\"."))
        self.rightmatrixdim_label.setText(_translate("MainWindow", "p"))
        self.mul_size_info.setText(_translate("MainWindow", "In order for 2 matrices to be successfully multiplied, 1 dimension from each matrix must be the same."))
        self.leftmatrixdim_label.setText(_translate("MainWindow", "m"))

    def sendSizes(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MultInWindow(self.leftmatrixdim.value(), self.shareddim.value(), self.rightmatrixdim.value())
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MultSizeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
