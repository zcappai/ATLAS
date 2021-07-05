# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eigenvector_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import sympy as sp
from eigenvector import Eigenvector
from eigenvector_single_method import Ui_EigenvectorSingleWindow
from validator import Validator
from emptyimg import empty
from closeWindow import QMainWindow


class Ui_EigenvectorInWindow(object):
    def __init__(self, size):
        self.size = size

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 871)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.matrix = QtWidgets.QTableWidget(self.centralwidget)
        self.matrix.setInputMethodHints(QtCore.Qt.ImhNone)
        self.matrix.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.matrix.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.matrix.setRowCount(self.size)
        self.matrix.setColumnCount(self.size)
        self.matrix.setObjectName("matrix")
        for i in range(self.matrix.columnCount()):
            for j in range(self.matrix.rowCount()):
                self.matrix.setItem(j, i, QtWidgets.QTableWidgetItem('0'))
        validator = Validator(self.matrix)
        self.matrix.itemChanged.connect(partial(validator.validate)) ######################
        # self.matrix.itemChanged.connect(self.validation) ######################
        self.gridLayout.addWidget(self.matrix, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.matrix_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.matrix_info.setFont(font)
        self.matrix_info.setWordWrap(True)
        self.matrix_info.setObjectName("matrix_info")
        self.gridLayout.addWidget(self.matrix_info, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMinimumSize(QtCore.QSize(125, 50))
        self.submit.setMaximumSize(QtCore.QSize(125, 16777215))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.sendMatrix)
        self.gridLayout.addWidget(self.submit, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
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
        self.matrix_info.setText(_translate("MainWindow", "Please enter the values into the square matrix below.\n"
"Use the scrollbar for larger matrices, if necessary."))
        self.submit.setText(_translate("MainWindow", "Submit"))

    # def validation(self):
    #     input_text = self.matrix.currentItem().text()
    #     validation_rule = QtGui.QDoubleValidator(-100, 100, 10)
    #     if validation_rule.validate(input_text, 0)[0] == QtGui.QValidator.Acceptable:
    #         pass
    #     else:
    #         cell = self.matrix.currentIndex()
    #         self.matrix.setCurrentCell(cell.row(), cell.column())
    #         self.matrix.setItem(cell.row(), cell.column(), QtWidgets.QTableWidgetItem('0'))
    #         print("INVALID!") ################### INSERT A POPUP MESSAGE HERE = "Invalid input. Default value set to 0."

    def sendMatrix(self):
        final_matrix = []
        for i in range(self.matrix.rowCount()):
            curr_row = []
            for j in range(self.matrix.columnCount()):
                curr_row.append(self.matrix.item(i, j).text())
            final_matrix.append(curr_row)
        matrix = sp.Matrix(final_matrix)
        empty()
        e_vec = Eigenvector(matrix)
        solutions = e_vec.calc()
        e_vec.latex2img()

        self.window = QMainWindow()
        self.ui = Ui_EigenvectorSingleWindow(solutions)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_EigenvectorInWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
