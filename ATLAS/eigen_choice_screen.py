# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eigen_choice_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from eigenvalue_size import Ui_EigenvalueSizeWindow
from eigenvector_size import Ui_EigenvectorSizeWindow
from closeWindow import QMainWindow


class Ui_EigenChoiceWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.eigenvector_size_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.eigenvector_size_button.setFont(font)
        self.eigenvector_size_button.setObjectName("eigenvector_size_button")
        self.eigenvector_size_button.clicked.connect(self.toEigenvectorSize)
        self.gridLayout.addWidget(self.eigenvector_size_button, 4, 3, 1, 1)
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
        self.eigenvalue_size_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.eigenvalue_size_button.setFont(font)
        self.eigenvalue_size_button.setObjectName("eigenvalue_size_button")
        self.eigenvalue_size_button.clicked.connect(self.toEigenvalueSize)
        self.gridLayout.addWidget(self.eigenvalue_size_button, 4, 1, 1, 1)
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setMinimumSize(QtCore.QSize(0, 50))
        self.back_button.setMaximumSize(QtCore.QSize(50, 16777215))
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 0, 0, 2, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
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
        self.eigenvector_size_button.setText(_translate("MainWindow", "Eigenvector"))
        self.label.setText(_translate("MainWindow", "Select one of the options:\n"
"\"Eigenvalue\" allows you to calculate the eigenvalue of a matrix\n"
"\"Eigenvector\" allows you to calculate the eigenvector of a matrix"))
        self.eigenvalue_size_button.setText(_translate("MainWindow", "Eigenvalue"))
        self.back_button.setText(_translate("MainWindow", "Go Back"))

    def toEigenvalueSize(self):
        self.window = QMainWindow()
        self.ui = Ui_EigenvalueSizeWindow()
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()

    def toEigenvectorSize(self):
        self.window = QMainWindow()
        self.ui = Ui_EigenvectorSizeWindow()
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_EigenChoiceWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
