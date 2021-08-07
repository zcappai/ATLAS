# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solving_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sympy as sp
# from solving import GaussianElimination
# from solving_single_method import Ui_SolveSingleWindow
# from functools import partial
from validator import Validator
# from emptyimg import empty
from closeWindow import QMainWindow
from single_comparison import Ui_SingleCompWindow

class Ui_SolveInWindow(object):
    def __init__(self, equations, unknowns):
        self.equations = equations
        self.unknowns = unknowns

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.matrix = QtWidgets.QTableWidget(self.centralwidget)
        self.matrix.setMinimumSize(QtCore.QSize(500, 250))
        self.matrix.setInputMethodHints(QtCore.Qt.ImhNone)
        self.matrix.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.matrix.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.matrix.setRowCount(self.equations)
        self.matrix.setColumnCount(self.unknowns + 1)
        self.matrix.setObjectName("matrix")
        for i in range(self.matrix.columnCount()):
            for j in range(self.matrix.rowCount()):
                self.matrix.setItem(j, i, QtWidgets.QTableWidgetItem('0'))
        # self.matrix.itemChanged.connect(self.validation) #################################
        self.gridLayout.addWidget(self.matrix, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.matrix_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.matrix_info.setFont(font)
        self.matrix_info.setWordWrap(True)
        self.matrix_info.setObjectName("matrix_info")
        self.gridLayout.addWidget(self.matrix_info, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMinimumSize(QtCore.QSize(125, 50))
        self.submit.setMaximumSize(QtCore.QSize(125, 16777215))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.sendEquations)
        self.gridLayout.addWidget(self.submit, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("ATLAS")
        self.matrix_info.setText("Please enter the values for the linear equations into the table below."
        +"\nRemember, unique solutions can only be guaranteed when the number of equations equals the number of unknowns."
        +"\nUse the scrollbar for larger linear equations, if necessary.")
        self.submit.setText("Submit")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setFont(font)
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")

        self.validator = Validator(self.matrix, self.warning)
        self.matrix.itemChanged.connect(self.validator.validate) #################################

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "ATLAS"))
#         self.matrix_info.setText(_translate("MainWindow", "Please enter the values for the linear equations into the table below.\n"
# "Use the scrollbar for larger linear equations, if necessary."))
#         self.submit.setText(_translate("MainWindow", "Submit"))

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

    def sendEquations(self):
        final_matrix = []
        for i in range(self.matrix.rowCount()):
            curr_row = []
            for j in range(self.matrix.columnCount()):
                curr_row.append(self.matrix.item(i, j).text())
            final_matrix.append(curr_row)
        matrix = sp.Matrix(final_matrix)
        # empty()
        # arg = GaussianElimination(matrix)
        # found, solutions, reduced = solution.calc()
        # solution.latex2img()

        self.window = QMainWindow()
        self.ui = Ui_SingleCompWindow(matrix, "solve")
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

        # self.window = QMainWindow()
        # self.ui = Ui_SolveSingleWindow(solutions)
        # self.ui.setupUi(self.window)
        # self.MainWindow.hide()
        # self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_SolveInWindow(3,2)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
