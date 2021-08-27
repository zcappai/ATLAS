import sys
from closeWindow import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from multiplication_size import Ui_MultSizeWindow
from square_size import Ui_SquareSizeWindow
from solving_size import Ui_SolveSizeWindow
from eigen_choice_screen import Ui_EigenChoiceWindow

# Main Menu GUI Class
class Ui_MainWindow(object):
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
        font.setPointSize(45)
        # Welcome message
        self.welcome_message = QtWidgets.QLabel(self.centralwidget)
        self.welcome_message.setFont(font)
        self.welcome_message.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_message.setObjectName("welcome_message")
        self.gridLayout.addWidget(self.welcome_message, 0, 0, 1, 2)

        font1 = QtGui.QFont()
        font1.setPointSize(30)
        # Determinant button
        self.determinant_button = QtWidgets.QPushButton(self.centralwidget)
        self.determinant_button.setFont(font1)
        self.determinant_button.setMinimumHeight(75)
        self.determinant_button.setObjectName("determinant_button")
        self.determinant_button.clicked.connect(self.toDeterminant)
        self.gridLayout.addWidget(self.determinant_button, 4, 0, 1, 1)

        # Multiplication button
        self.multiplication_button = QtWidgets.QPushButton(self.centralwidget)
        self.multiplication_button.setFont(font1)
        self.multiplication_button.setMinimumHeight(75)
        self.multiplication_button.setObjectName("multiplication_button")
        self.multiplication_button.clicked.connect(self.toMultiplication)
        self.gridLayout.addWidget(self.multiplication_button, 4, 1, 1, 1)

        # Inverse button
        self.inverse_button = QtWidgets.QPushButton(self.centralwidget)
        self.inverse_button.setFont(font1)
        self.inverse_button.setMinimumHeight(75)
        self.inverse_button.setObjectName("inverse_button")
        self.inverse_button.clicked.connect(self.toInverse)
        self.gridLayout.addWidget(self.inverse_button, 5, 0, 1, 1)

        # Eigenvalues/eigenvectors button
        self.eigen_button = QtWidgets.QPushButton(self.centralwidget)
        self.eigen_button.setFont(font1)
        self.eigen_button.setMinimumHeight(75)
        self.eigen_button.setObjectName("eigen_button")
        self.eigen_button.clicked.connect(self.toEigenChoice)
        self.gridLayout.addWidget(self.eigen_button, 5, 1, 1, 1)

        # Solving systems of linear equations button
        self.solving_systems = QtWidgets.QPushButton(self.centralwidget)
        self.solving_systems.setFont(font1)
        self.solving_systems.setMinimumHeight(75)
        self.solving_systems.setObjectName("solving_systems")
        self.solving_systems.clicked.connect(self.toSolve)
        self.gridLayout.addWidget(self.solving_systems, 6, 0, 1, 2)

        # Information about main menu
        self.main_info = QtWidgets.QLabel(self.centralwidget)
        self.main_info.setFont(font1)
        self.main_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_info.setAlignment(QtCore.Qt.AlignCenter)
        self.main_info.setObjectName("main_info")
        self.gridLayout.addWidget(self.main_info, 1, 0, 1, 2)

        # Spacers provide structure
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.welcome_message.setText("Welcome to ATLAS!")
        self.multiplication_button.setText("Matrix Multiplication")
        self.inverse_button.setText("Inverse")
        self.eigen_button.setText("Eigenvalues/Eigenvectors")
        self.main_info.setText("Choose a linear algebra function from the selection below!\n\nPress the \"Reset\" button after pressing\nthe \u2613 button to reset to the main menu")
        self.solving_systems.setText("Solving Systems of Linear Equations")
        self.determinant_button.setText("Determinants")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def toDeterminant(self):
        self.window = QMainWindow()
        self.ui = Ui_SquareSizeWindow("det")
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()

    def toMultiplication(self):
        self.window = QMainWindow()
        self.ui = Ui_MultSizeWindow()
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()
    
    def toInverse(self):
        self.window = QMainWindow()
        self.ui = Ui_SquareSizeWindow("inv")
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()

    def toSolve(self):
        self.window = QMainWindow()
        self.ui = Ui_SolveSizeWindow()
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()

    def toEigenChoice(self):
        self.window = QMainWindow()
        self.ui = Ui_EigenChoiceWindow()
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()

# Defined outside of main() to load main menu from other parts of ATLAS
app = QtWidgets.QApplication(sys.argv)
MainWindow = QMainWindow()
# Loads main menu of ATLAS
def main():
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())