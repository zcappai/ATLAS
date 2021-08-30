from PyQt5 import QtCore, QtGui, QtWidgets
from single_method_choice import Ui_SingleChoiceWindow
from compare_loading_screen import Ui_CompLoadingWindow
from os import mkdir
import multiplication
import determinant
import inverse
import solving
import eigenvalue
import eigenvector
from emptyimg import empty
from closeWindow import QMainWindow
import saver
from closeWindow import QMainWindow

# GUI for Choosing Single Method or Method Comparison
class Ui_SingleCompWindow(object):
    # Initialises matrix arguments and function ID
    def __init__(self, arg, func):
        self.arg = arg
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
        # Compare methods button
        self.comparison_button = QtWidgets.QPushButton(self.centralwidget)
        self.comparison_button.setFont(font)
        self.comparison_button.setMinimumSize(QtCore.QSize(150, 75))
        self.comparison_button.setObjectName("comparison_button")
        self.comparison_button.clicked.connect(self.toCompare)
        self.gridLayout.addWidget(self.comparison_button, 4, 3, 1, 1)

        # Single method button
        self.single_button = QtWidgets.QPushButton(self.centralwidget)
        self.single_button.setFont(font)
        self.single_button.setMinimumSize(QtCore.QSize(150, 75))
        self.single_button.setObjectName("single_button")
        self.single_button.clicked.connect(self.toSingle)
        self.gridLayout.addWidget(self.single_button, 4, 1, 1, 1)

        # Info label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)

        # Spacers provide structure
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 3, 1, 1, 1)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.comparison_button.setText("Comparison")
        self.label.setText("Click one of the options below:\n\"One Method\" allows you to choose a single method to use.\n\"Comparison\" allows you to compare all valid methods.")
        self.single_button.setText("One Method")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Displays GUI for choosing single method
    def toSingle(self):
        self.window = QMainWindow()
        self.ui = Ui_SingleChoiceWindow(self.arg, self.func)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()

    # For method comparison
    def toCompare(self):
        empty()
        self.window = QMainWindow()
        if self.func == "mult":
            self.compareMult()
        elif self.func == "det":
            self.compareDet()
        elif self.func == "inv":
            self.compareInv()
        elif self.func == "solve":
            self.compareSolve()
        elif self.func == "e_val":
            self.compareEigenvalue()
        elif self.func == "e_vec":
            self.compareEigenvector()

    # Comparing matrix multiplication methods
    def compareMult(self):
        methods = multiplication.getMethods()
        methodsToSend = []
        # Generating solution for each method
        for (i, j) in methods:
            mkdir("images/{}/".format(i))
            current_method = j(*self.arg)
            current_method.calc()
            methodsToSend.append(current_method)
        # Loading screen generates step-by-step solutions
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_CompLoadingWindow("mult", methodsToSend)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Comparing determinant methods
    def compareDet(self):
        methods = determinant.getMethods()
        methodsToSend = []
        # Generating solution for each method
        for (i, j) in methods:
            mkdir("images/{}/".format(i))
            current_method = j(self.arg)
            current_method.calc()
            methodsToSend.append(current_method)
        # Loading screen generates step-by-step solutions
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_CompLoadingWindow("det", methodsToSend)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Comparing inverse methods
    def compareInv(self):
        methods = inverse.getMethods()
        methodsToSend = []
        # Generating solution for each method
        for (i, j) in methods:
            mkdir("images/{}/".format(i))
            current_method = j(self.arg)
            check_bool = current_method.check()
            if check_bool == True:
                current_method.calc()
            else:
                pass
            methodsToSend.append(current_method)
        # Loading screen generates step-by-step solutions
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_CompLoadingWindow("inv", methodsToSend)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Comparing solving systems of linear equations methods
    def compareSolve(self):
        methods = solving.getMethods()
        methodsToSend = []
        # Generating solution for each method
        for (i, j) in methods:
            mkdir("images/{}/".format(i))
            matrix = self.arg[:, :]
            current_method = j(matrix)
            current_method.calc()
            methodsToSend.append(current_method)
        # Loading screen generates step-by-step solutions
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_CompLoadingWindow("solve", methodsToSend)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Comparing eigenvalue methods
    def compareEigenvalue(self):
        methods = eigenvalue.getMethods()
        methodsToSend = []
        # Generating solution for each method
        for (i, j) in methods:
            mkdir("images/{}/".format(i))
            matrix = self.arg[:, :]
            current_method = j(matrix)
            current_method.calc()
            methodsToSend.append(current_method)
        # Loading screen generates step-by-step solutions
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_CompLoadingWindow("e_val", methodsToSend)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Comparing eigenvector methods
    def compareEigenvector(self):
        methods = eigenvector.getMethods()
        methodsToSend = []
        # Generating solution for each method
        for (i, j) in methods:
            mkdir("images/{}/".format(i))
            matrix = self.arg[:, :]
            current_method = j(matrix)
            current_method.calc()
            methodsToSend.append(current_method)
        # Loading screen generates step-by-step solutions
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_CompLoadingWindow("e_vec", methodsToSend)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()