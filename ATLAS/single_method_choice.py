from PyQt5 import QtCore, QtGui, QtWidgets
from emptyimg import empty
from num_single_method import Ui_NumSingleWindow
from non_num_single_method import Ui_NonNumSingleWindow
from loading_screen import Ui_LoadingWindow
from multiplication import Laderman, naiveMultiplication, Strassen
from determinant import naiveDeterminant, Sarrus, LU
from inverse import naiveInverse, CayleyHamilton
from solving import Cholesky, GaussianElimination, CramersRule
from eigenvalue import Characteristic
from eigenvector import Eigenvector
from closeWindow import QMainWindow

# GUI for Choosing Single Method
class Ui_SingleChoiceWindow(object):
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

        self.font = QtGui.QFont()
        self.font.setPointSize(30)
        # Method submit button
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setMinimumSize(QtCore.QSize(150, 75))
        self.submit_button.setFont(self.font)
        self.submit_button.setObjectName("submit_button")
        self.gridLayout.addWidget(self.submit_button, 7, 0, 1, 3, QtCore.Qt.AlignHCenter)

        # Method choice info
        self.methods_info = QtWidgets.QLabel(self.centralwidget)
        self.methods_info.setFont(self.font)
        self.methods_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.methods_info.setAlignment(QtCore.Qt.AlignCenter)
        self.methods_info.setWordWrap(True)
        self.methods_info.setObjectName("methods_info")
        self.gridLayout.addWidget(self.methods_info, 1, 0, 1, 3)

        # Shows list of available methods
        self.method_store = QtWidgets.QScrollArea(self.centralwidget)
        self.method_store.setWidgetResizable(True)
        self.method_store.setObjectName("method_store")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 358, 201))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.method_store.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.method_store, 5, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        # Spacers provide structure
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.submit_button.setText("Submit")
        self.methods_info.setText("Select one of the methods below and click the \"Submit\" button:")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Function ID determines which method options are shown
        # And which methods are connected to submit button
        if self.func == "mult":
            self.mult()
            self.submit_button.clicked.connect(self.multCall)
        elif self.func == "det":
            self.det()
            self.submit_button.clicked.connect(self.detCall)
        elif self.func == "inv":
            self.inv()
            self.submit_button.clicked.connect(self.invCall)
        elif self.func == "solve":
            self.solve()
            self.submit_button.clicked.connect(self.solveCall)
        elif self.func == "e_val":
            self.eigenvalue()
            self.submit_button.clicked.connect(self.eigenvalueCall)
        elif self.func == "e_vec":
            self.eigenvector()
            self.submit_button.clicked.connect(self.eigenvectorCall)

    # Displaying all matrix multiplication method options
    def mult(self):
        self.standard = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.standard.setObjectName("standard")
        self.verticalLayout.addWidget(self.standard)
        self.standard.setText("Standard Method")
        self.standard.setFont(self.font)
        self.standard.setChecked(True)

        self.strassen = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.strassen.setObjectName("strassen")
        self.verticalLayout.addWidget(self.strassen)
        self.strassen.setText("Strassen's Method")
        self.strassen.setFont(self.font)

        self.laderman = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.laderman.setObjectName("laderman")
        self.verticalLayout.addWidget(self.laderman)
        self.laderman.setText("Laderman Method")
        self.laderman.setFont(self.font)

    # Calculates solution for chosen matrix multiplication method
    def multCall(self):
        empty()
        if self.standard.isChecked() == True:
            mult = naiveMultiplication(*self.arg)
        elif self.strassen.isChecked() == True:
            mult = Strassen(*self.arg)
        elif self.laderman.isChecked() == True:
            mult = Laderman(*self.arg)
        mult.calc()
        mult.addSaved(True)
        # Passes method object to loading screen
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_LoadingWindow(mult, Ui_NonNumSingleWindow())
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Displaying all determinant method options
    def det(self):
        self.laplace = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.laplace.setObjectName("laplace")
        self.verticalLayout.addWidget(self.laplace)
        self.laplace.setText("Laplace Expansion")
        self.laplace.setFont(self.font)
        self.laplace.setChecked(True)

        self.sarrus = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.sarrus.setObjectName("sarrus")
        self.verticalLayout.addWidget(self.sarrus)
        self.sarrus.setText("Sarrus' Method")
        self.sarrus.setFont(self.font)

        self.lu = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.lu.setObjectName("lu")
        self.verticalLayout.addWidget(self.lu)
        self.lu.setText("LU Decomposition")
        self.lu.setFont(self.font)

    # Calculates solution for chosen determinant method
    def detCall(self):
        empty()
        if self.laplace.isChecked() == True:
            determinant = naiveDeterminant(self.arg)
        elif self.lu.isChecked() == True:
            determinant = LU(self.arg)
        elif self.sarrus.isChecked() == True:
            determinant = Sarrus(self.arg)
        ans = determinant.calc()
        determinant.addSaved(True)
        # Passes method object to loading screen
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_LoadingWindow(determinant, Ui_NumSingleWindow(ans, self.func))
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Displaying all inverse method options
    def inv(self):
        self.cramer = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.cramer.setObjectName("cramer")
        self.verticalLayout.addWidget(self.cramer)
        self.cramer.setText("Cramer's Rule")
        self.cramer.setFont(self.font)
        self.cramer.setChecked(True)

        self.cayley = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.cayley.setObjectName("cayley")
        self.verticalLayout.addWidget(self.cayley)
        self.cayley.setText("Cayley-Hamilton Theorem")
        self.cayley.setFont(self.font)

    # Calculates solution for chosen inverse method
    def invCall(self):
        empty()
        if self.cramer.isChecked() == True:
            inverse = naiveInverse(self.arg)
        elif self.cayley.isChecked() == True:
            inverse = CayleyHamilton(self.arg)
        check = inverse.check()
        if check == True:
            inverse.calc()
            inverse.addSaved(True)
        elif check == False:
            inverse.addSaved(True)
        # Passes method object to loading screen
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_LoadingWindow(inverse, Ui_NonNumSingleWindow())
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Displaying all solving systems of linear equations method options
    def solve(self):
        self.gaussian = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.gaussian.setObjectName("gaussian")
        self.verticalLayout.addWidget(self.gaussian)
        self.gaussian.setText("Gaussian Elimination")
        self.gaussian.setFont(self.font)
        self.gaussian.setChecked(True)

        self.cramers = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.cramers.setObjectName("cramers")
        self.verticalLayout.addWidget(self.cramers)
        self.cramers.setText("Cramer's Rule")
        self.cramers.setFont(self.font)

        self.cholesky = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.cholesky.setObjectName("cholesky")
        self.verticalLayout.addWidget(self.cholesky)
        self.cholesky.setText("Cholesky Decomposition")
        self.cholesky.setFont(self.font)

    # Calculates solution for chosen solving systems of linear equations method
    def solveCall(self):
        empty()
        if self.gaussian.isChecked() == True:
            solve = GaussianElimination(self.arg)
            ans = solve.calc()[1]
        elif self.cramers.isChecked() == True:
            solve = CramersRule(self.arg)
            ans = solve.calc()
        elif self.cholesky.isChecked() == True:
            solve = Cholesky(self.arg)
            ans = solve.calc()
        solve.addSaved(True)
        # Passes method object to loading screen
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_LoadingWindow(solve, Ui_NumSingleWindow(ans, self.func))
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Displaying all eigenvalue method options
    def eigenvalue(self):
        self.characteristic = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.characteristic.setObjectName("characteristic")
        self.verticalLayout.addWidget(self.characteristic)
        self.characteristic.setText("Characteristic Equation")
        self.characteristic.setFont(self.font)
        self.characteristic.setChecked(True)

    # Calculates solution for chosen eigenvalue method
    def eigenvalueCall(self):
        empty()
        if self.characteristic.isChecked() == True:
            e_value = Characteristic(self.arg)
        ans = e_value.calc()
        e_value.addSaved(True)
        # Passes method object to loading screen
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_LoadingWindow(e_value, Ui_NumSingleWindow(ans, self.func))
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    # Displaying all eigenvector method options
    def eigenvector(self):
        self.gaussian = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.gaussian.setObjectName("gaussian")
        self.verticalLayout.addWidget(self.gaussian)
        self.gaussian.setText("Gaussian Elimination")
        self.gaussian.setFont(self.font)
        self.gaussian.setChecked(True)

    # Calculates solution for chosen eigenvector method
    def eigenvectorCall(self):
        empty()
        if self.gaussian.isChecked() == True:
            e_vector = Eigenvector(self.arg)
        e_vector.calc()
        e_vector.addSaved(True)
        # Passes method object to loading screen
        self.window = QMainWindow()
        self.window.setFixedSize(400, 150)
        self.ui = Ui_LoadingWindow(e_vector, Ui_NonNumSingleWindow())
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()