from PyQt5 import QtCore, QtGui, QtWidgets
import sympy as sp
from validator import Validator
from closeWindow import QMainWindow
from single_comparison import Ui_SingleCompWindow

# Matrix Multiplication Input GUI
class Ui_MultInWindow(object):
    # Initialises matrix sizes
    def __init__(self, leftdim, shareddim, rightdim):
        self.leftdim = leftdim
        self.shareddim = shareddim
        self.rightdim = rightdim

    # Setting up GUI
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")

        # Parent widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Provides structure to widget layout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Table for inputting left matrix
        self.matrixleft = QtWidgets.QTableWidget(self.centralwidget)
        self.matrixleft.setRowCount(self.leftdim)
        self.matrixleft.setColumnCount(self.shareddim)
        self.matrixleft.setObjectName("matrixleft")
        self.gridLayout.addWidget(self.matrixleft, 3, 1, 2, 1)
        # Setting all left table values to 0
        for i in range(self.matrixleft.columnCount()):
            for j in range(self.matrixleft.rowCount()):
                self.matrixleft.setItem(j, i, QtWidgets.QTableWidgetItem('0'))

        # Table for inputting right matrix
        self.matrixright = QtWidgets.QTableWidget(self.centralwidget)
        self.matrixright.setRowCount(self.shareddim)
        self.matrixright.setColumnCount(self.rightdim)
        self.matrixright.setObjectName("matrixright")
        self.gridLayout.addWidget(self.matrixright, 3, 2, 1, 1)
        # Setting all right table values to 0
        for i in range(self.matrixright.columnCount()):
            for j in range(self.matrixright.rowCount()):
                self.matrixright.setItem(j, i, QtWidgets.QTableWidgetItem('0'))

        font = QtGui.QFont()
        font.setPointSize(30)
        # Matrix labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)

        # Input information
        self.matrix_info = QtWidgets.QLabel(self.centralwidget)
        self.matrix_info.setFont(font)
        self.matrix_info.setWordWrap(True)
        self.matrix_info.setObjectName("matrix_info")
        self.gridLayout.addWidget(self.matrix_info, 0, 0, 1, 4)

        # Matrix input submit button
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMinimumSize(QtCore.QSize(150, 75))
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.gridLayout.addWidget(self.submit, 7, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.submit.clicked.connect(self.sendMatrix)

        MainWindow.setCentralWidget(self.centralwidget)

        # Spacers provide structure
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 2)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.label.setText("Left Matrix")
        self.matrix_info.setText("Please enter the matrix values for both matrices into the tables below and press the \"Submit\" button.\nFor larger matrices, a scrollbar will appear.")
        self.submit.setText("Submit")
        self.label_2.setText("Right Matrix")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Warning label for invalid inputs
        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setFont(font)
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")

        # Validates inputs into tables
        self.validator_left = Validator(self.matrixleft, self.warning)
        self.validator_right = Validator(self.matrixright, self.warning)
        self.matrixleft.itemChanged.connect(self.validator_left.validation)
        self.matrixright.itemChanged.connect(self.validator_right.validation)

    # Sends matrices to choose single method or compare methods
    def sendMatrix(self):
        # Transfers left table values into SymPy matrix
        final_matrix_left = []
        for i in range(self.matrixleft.rowCount()):
            curr_row = []
            for j in range(self.matrixleft.columnCount()):
                curr_row.append(self.matrixleft.item(i, j).text())
            final_matrix_left.append(curr_row)

        # Transfers right table values into SymPy matrix
        final_matrix_right = []
        for i in range(self.matrixright.rowCount()):
            curr_row = []
            for j in range(self.matrixright.columnCount()):
                curr_row.append(self.matrixright.item(i, j).text())
            final_matrix_right.append(curr_row)
        final_matrix_left = sp.Matrix(final_matrix_left)
        final_matrix_right = sp.Matrix(final_matrix_right)
        arg = (final_matrix_left, final_matrix_right)

        # Sends matrices and function ID to choose single method or compare methods
        self.window = QMainWindow()
        self.ui = Ui_SingleCompWindow(arg, "mult")
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()