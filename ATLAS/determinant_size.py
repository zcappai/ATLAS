# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'determinant_size.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from determinant_input import Ui_DetInWindow

class Ui_DetSizeWindow(object):
    def setupUi(self, DetSizeWindow):
        self.DetSizeWindow = DetSizeWindow
        DetSizeWindow.setObjectName("DetSizeWindow")
        self.centralwidget = QtWidgets.QWidget(DetSizeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.det_size_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.det_size_info.setFont(font)
        self.det_size_info.setWordWrap(True)
        self.det_size_info.setObjectName("det_size_info")
        self.gridLayout.addWidget(self.det_size_info, 0, 0, 1, 1)
        self.det_size = QtWidgets.QSpinBox(self.centralwidget)
        self.det_size.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.det_size.setFont(font)
        self.det_size.setAlignment(QtCore.Qt.AlignCenter)
        self.det_size.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.det_size.setMaximum(1000)
        self.det_size.setObjectName("det_size")
        self.gridLayout.addWidget(self.det_size, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.det_size_info2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.det_size_info2.setFont(font)
        self.det_size_info2.setWordWrap(True)
        self.det_size_info2.setObjectName("det_size_info2")
        self.gridLayout.addWidget(self.det_size_info2, 2, 0, 1, 1)
        self.det_size_info1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.det_size_info1.setFont(font)
        self.det_size_info1.setWordWrap(True)
        self.det_size_info1.setObjectName("det_size_info1")
        self.gridLayout.addWidget(self.det_size_info1, 1, 0, 1, 1)
        self.det_size_submit = QtWidgets.QPushButton(self.centralwidget)
        self.det_size_submit.setMinimumSize(QtCore.QSize(125, 50))
        self.det_size_submit.setMaximumSize(QtCore.QSize(125, 16777215))
        self.det_size_submit.setObjectName("det_size_submit")
        self.det_size_submit.clicked.connect(self.sendSize) #######################################
        self.gridLayout.addWidget(self.det_size_submit, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        DetSizeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DetSizeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        DetSizeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DetSizeWindow)
        self.statusbar.setObjectName("statusbar")
        DetSizeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DetSizeWindow)
        QtCore.QMetaObject.connectSlotsByName(DetSizeWindow)

    def retranslateUi(self, DetSizeWindow):
        _translate = QtCore.QCoreApplication.translate
        DetSizeWindow.setWindowTitle(_translate("DetSizeWindow", "MainWindow"))
        self.det_size_info.setText(_translate("DetSizeWindow", "Use the box below to choose what size matrix you wish to enter."))
        self.det_size_info2.setText(_translate("DetSizeWindow", "e.g. if you enter the number 4, the matrix must be of size 4x4."))
        self.det_size_info1.setText(_translate("DetSizeWindow", "Remember, the determinant can only be calculated for a square matrix, which is a matrix that has the same number of elements along its width and height."))
        self.det_size_submit.setText(_translate("DetSizeWindow", "Submit"))
    
    def sendSize(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DetInWindow(self.det_size.value())
        print(self.det_size.value())
        self.ui.setupUi(self.window)
        self.DetSizeWindow.hide()
        self.window.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DetSizeWindow = QtWidgets.QMainWindow()
    ui = Ui_DetSizeWindow()
    ui.setupUi(DetSizeWindow)
    DetSizeWindow.showMaximized()
    sys.exit(app.exec_())
    