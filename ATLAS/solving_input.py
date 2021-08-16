from PyQt5 import QtCore, QtGui, QtWidgets
import sympy as sp
from validator import Validator
from closeWindow import QMainWindow
from single_comparison import Ui_SingleCompWindow

# System of Linear Equations Input GUI
class Ui_SolveInWindow(object):
    # Initialises matrix size
    def __init__(self, equations, unknowns):
        self.equations = equations
        self.unknowns = unknowns

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

        # Table for inputting system of linear equations
        self.matrix = QtWidgets.QTableWidget(self.centralwidget)
        self.matrix.setRowCount(self.equations)
        self.matrix.setColumnCount(self.unknowns + 1)
        self.matrix.setObjectName("matrix")
        self.gridLayout.addWidget(self.matrix, 2, 1, 1, 1)
        # Setting all table values to 0
        for i in range(self.matrix.columnCount()):
            for j in range(self.matrix.rowCount()):
                self.matrix.setItem(j, i, QtWidgets.QTableWidgetItem('0'))

        font = QtGui.QFont()
        font.setPointSize(30)
        # Input information
        self.matrix_info = QtWidgets.QLabel(self.centralwidget)
        self.matrix_info.setFont(font)
        self.matrix_info.setWordWrap(True)
        self.matrix_info.setObjectName("matrix_info")
        self.gridLayout.addWidget(self.matrix_info, 0, 0, 1, 3)

        # Matrix input submit button
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMinimumSize(QtCore.QSize(150, 75))
        self.submit.setObjectName("submit")
        self.submit.setFont(font)
        self.submit.clicked.connect(self.sendMatrix)
        self.gridLayout.addWidget(self.submit, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        # Spacers provide structure
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.matrix_info.setText("Please enter the values for the linear equations into the table below."
        +"\nRemember, unique solutions can only be guaranteed when the number of equations equals the number of unknowns."
        +"\nUse the scrollbar for larger linear equations, if necessary.")
        self.submit.setText("Submit")

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
        self.ui = Ui_SingleCompWindow(arg, "solve")
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()
