# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'size.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from eigenvalue_input import Ui_EigenvalueInWindow


class Ui_EigenvalueSizeWindow(object):
    def setupUi(self, EigenvalueSizeWindow):
        self.EigenvalueSizeWindow = EigenvalueSizeWindow
        EigenvalueSizeWindow.setObjectName("EigenvalueSizeWindow")
        EigenvalueSizeWindow.resize(1100, 871)
        self.centralwidget = QtWidgets.QWidget(EigenvalueSizeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.size_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.size_info.setFont(font)
        self.size_info.setWordWrap(True)
        self.size_info.setObjectName("size_info")
        self.gridLayout.addWidget(self.size_info, 0, 0, 1, 1)
        self.size = QtWidgets.QSpinBox(self.centralwidget)
        self.size.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.size.setFont(font)
        self.size.setAlignment(QtCore.Qt.AlignCenter)
        self.size.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.size.setMaximum(1000)
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.size_info2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.size_info2.setFont(font)
        self.size_info2.setWordWrap(True)
        self.size_info2.setObjectName("size_info2")
        self.gridLayout.addWidget(self.size_info2, 2, 0, 1, 1)
        self.size_info1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.size_info1.setFont(font)
        self.size_info1.setWordWrap(True)
        self.size_info1.setObjectName("size_info1")
        self.gridLayout.addWidget(self.size_info1, 1, 0, 1, 1)
        self.size_submit = QtWidgets.QPushButton(self.centralwidget)
        self.size_submit.setMinimumSize(QtCore.QSize(125, 50))
        self.size_submit.setMaximumSize(QtCore.QSize(125, 16777215))
        self.size_submit.setObjectName("size_submit")
        self.size_submit.clicked.connect(self.sendSize) #########################
        self.gridLayout.addWidget(self.size_submit, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        EigenvalueSizeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EigenvalueSizeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        EigenvalueSizeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EigenvalueSizeWindow)
        self.statusbar.setObjectName("statusbar")
        EigenvalueSizeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EigenvalueSizeWindow)
        QtCore.QMetaObject.connectSlotsByName(EigenvalueSizeWindow)

    def retranslateUi(self, EigenvalueSizeWindow):
        _translate = QtCore.QCoreApplication.translate
        EigenvalueSizeWindow.setWindowTitle(_translate("EigenvalueSizeWindow", "MainWindow"))
        self.size_info.setText(_translate("EigenvalueSizeWindow", "Use the box below to choose what size matrix you wish to enter."))
        self.size_info2.setText(_translate("EigenvalueSizeWindow", "e.g. if you enter the number 4, the matrix must be of size 4x4."))
        self.size_info1.setText(_translate("EigenvalueSizeWindow", "Remember, the eigenvalue can only be calculated for a square matrix, which is a matrix that has the same number of elements along its width and height."))
        self.size_submit.setText(_translate("EigenvalueSizeWindow", "Submit"))

    def sendSize(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EigenvalueInWindow(self.size.value())
        self.ui.setupUi(self.window)
        self.EigenvalueSizeWindow.hide()
        self.window.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EigenvalueSizeWindow = QtWidgets.QMainWindow()
    ui = Ui_EigenvalueSizeWindow()
    ui.setupUi(EigenvalueSizeWindow)
    EigenvalueSizeWindow.show()
    sys.exit(app.exec_())
