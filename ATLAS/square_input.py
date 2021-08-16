from PyQt5 import QtCore, QtGui, QtWidgets
import sympy as sp
from validator import Validator
from closeWindow import QMainWindow
from single_comparison import Ui_SingleCompWindow

# Square Matrix Input GUI
class Ui_SquareInWindow(object):
    # Initialises matrix size and function ID
    def __init__(self, size, func):
        self.size = size
        self.func = func

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

        font = QtGui.QFont()
        font.setPointSize(30)
        # Input information
        self.matrix_info = QtWidgets.QLabel(self.centralwidget)
        self.matrix_info.setFont(font)
        self.matrix_info.setWordWrap(True)
        self.matrix_info.setObjectName("matrix_info")
        self.gridLayout.addWidget(self.matrix_info, 0, 0, 1, 3)

        # Table for inputting matrix
        self.matrix = QtWidgets.QTableWidget(self.centralwidget)
        self.matrix.setRowCount(self.size)
        self.matrix.setColumnCount(self.size)
        self.matrix.setObjectName("matrix")
        self.gridLayout.addWidget(self.matrix, 2, 1, 1, 1)
        # Setting all table values to 0
        for i in range(self.matrix.columnCount()):
            for j in range(self.matrix.rowCount()):
                self.matrix.setItem(j, i, QtWidgets.QTableWidgetItem('0'))

        # Matrix input submit button
        self.input_submit = QtWidgets.QPushButton(self.centralwidget)
        self.input_submit.setFont(font)
        self.input_submit.setMinimumSize(QtCore.QSize(150, 75))
        self.input_submit.setObjectName("input_submit")
        self.input_submit.clicked.connect(self.sendMatrix)
        self.gridLayout.addWidget(self.input_submit, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        # Spacers provide structure
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.matrix_info.setText("Please enter the matrix values into the table below and press the \"Submit\" button.\nFor larger matrices, a scrollbar will appear.")
        self.input_submit.setText("Submit")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Warning label for invalid inputs
        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setFont(font)
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")

        # Validates inputs into table
        self.validator = Validator(self.matrix, self.warning)
        self.matrix.itemChanged.connect(self.validator.validation)

    # Sends matrix to choose single method or compare methods
    def sendMatrix(self):
        # Transfers table values into SymPy matrix
        final_matrix = []
        for i in range(self.matrix.rowCount()):
            curr_row = []
            for j in range(self.matrix.columnCount()):
                curr_row.append(self.matrix.item(i, j).text())
            final_matrix.append(curr_row)
        arg = sp.Matrix(final_matrix)

        # Sends matrix and function ID to choose single method or compare methods
        self.window = QMainWindow()
        self.ui = Ui_SingleCompWindow(arg, self.func)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()