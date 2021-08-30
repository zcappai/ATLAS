from PyQt5 import QtCore, QtGui, QtWidgets
from solving_input import Ui_SolveInWindow
from closeWindow import QMainWindow

# Solving System of Linear Equations Matrix Size GUI
class Ui_SolveSizeWindow(object):
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
        # Size information
        self.mul_size_info = QtWidgets.QLabel(self.centralwidget)
        self.mul_size_info.setFont(font)
        self.mul_size_info.setWordWrap(True)
        self.mul_size_info.setObjectName("mul_size_info")
        self.gridLayout.addWidget(self.mul_size_info, 0, 0, 1, 5)

        # Matrix size spinbox
        self.equations = QtWidgets.QSpinBox(self.centralwidget)
        self.equations.setMinimumSize(QtCore.QSize(150, 75))
        self.equations.setFont(font)
        self.equations.setAlignment(QtCore.Qt.AlignCenter)
        self.equations.setMaximum(10)
        self.equations.setObjectName("equations")
        self.gridLayout.addWidget(self.equations, 4, 1, 1, 1)

        self.unknowns = QtWidgets.QSpinBox(self.centralwidget)
        self.unknowns.setMinimumSize(QtCore.QSize(150, 75))
        self.unknowns.setFont(font)
        self.unknowns.setAlignment(QtCore.Qt.AlignCenter)
        self.unknowns.setMaximum(10)
        self.unknowns.setObjectName("unknowns")
        self.gridLayout.addWidget(self.unknowns, 4, 3, 1, 1)

        # Spinbox labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 1)

        # Size submit button
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMinimumSize(QtCore.QSize(150, 75))
        self.submit.setObjectName("submit")
        self.submit.setFont(font)
        self.submit.clicked.connect(self.sendSize)
        self.gridLayout.addWidget(self.submit, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        # Spacers provide structure
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 2, 1, 1)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.mul_size_info.setText("In the 2 boxes below, choose the number of equations you wish to enter and the number of unknowns in those equations.")
        self.label.setText("Equations")
        self.label_2.setText("Unknowns")
        self.submit.setText("Submit")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Sending sizes to create matrices
    def sendSize(self):
        self.window = QMainWindow()
        self.ui = Ui_SolveInWindow(self.equations.value(), self.unknowns.value())
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()