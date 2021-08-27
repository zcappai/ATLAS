from PyQt5 import QtCore, QtGui, QtWidgets
from square_size import Ui_SquareSizeWindow
from closeWindow import QMainWindow

# GUI for Choosing Eigenvalue or Eigenvector
class Ui_EigenChoiceWindow(object):
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
        # Eigenvector button
        self.eigenvector_button = QtWidgets.QPushButton(self.centralwidget)
        self.eigenvector_button.setFont(font)
        self.eigenvector_button.setMinimumSize(QtCore.QSize(150, 75))
        self.eigenvector_button.setObjectName("eigenvector_button")
        self.eigenvector_button.clicked.connect(self.toEigenvectorSize)
        self.gridLayout.addWidget(self.eigenvector_button, 4, 3, 1, 1)

        # Eigenvalue button
        self.eigenvalue_button = QtWidgets.QPushButton(self.centralwidget)
        self.eigenvalue_button.setFont(font)
        self.eigenvalue_button.setMinimumSize(QtCore.QSize(150, 75))
        self.eigenvalue_button.setObjectName("eigenvalue_button")
        self.eigenvalue_button.clicked.connect(self.toEigenvalueSize)
        self.gridLayout.addWidget(self.eigenvalue_button, 4, 1, 1, 1)

        # Options info
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
        self.eigenvector_button.setText("Eigenvector")
        self.label.setText("Select one of the options:\n\"Eigenvalue\" allows you to calculate the eigenvalue of a matrix\n\"Eigenvector\" allows you to calculate the eigenvector of a matrix")
        self.eigenvalue_button.setText("Eigenvalue")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Loads GUI for choosing eigenvalue size
    def toEigenvalueSize(self):
        self.window = QMainWindow()
        self.ui = Ui_SquareSizeWindow("e_val")
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()

    # Loads GUI for choosing eigenvector size
    def toEigenvectorSize(self):
        self.window = QMainWindow()
        self.ui = Ui_SquareSizeWindow("e_vec")
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()