from PyQt5 import QtCore, QtGui, QtWidgets
from square_input import Ui_SquareInWindow
from closeWindow import QMainWindow

# Square Matrix Size GUI
class Ui_SquareSizeWindow(object):
    # Constructor initialises function ID
    def __init__(self, func):
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
        # Size information
        self.size_info = QtWidgets.QLabel(self.centralwidget)
        self.size_info.setFont(font)
        self.size_info.setWordWrap(True)
        self.size_info.setObjectName("size_info")
        self.gridLayout.addWidget(self.size_info, 0, 0, 1, 1)

        self.size_info1 = QtWidgets.QLabel(self.centralwidget)
        self.size_info1.setFont(font)
        self.size_info1.setWordWrap(True)
        self.size_info1.setObjectName("size_info1")
        self.gridLayout.addWidget(self.size_info1, 1, 0, 1, 1)

        self.size_info2 = QtWidgets.QLabel(self.centralwidget)
        self.size_info2.setFont(font)
        self.size_info2.setWordWrap(True)
        self.size_info2.setObjectName("size_info2")
        self.gridLayout.addWidget(self.size_info2, 2, 0, 1, 1)

        # Matrix size spinbox
        self.size = QtWidgets.QSpinBox(self.centralwidget)
        self.size.setMinimumSize(QtCore.QSize(150, 75))
        self.size.setFont(font)
        self.size.setAlignment(QtCore.Qt.AlignCenter)
        self.size.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.size.setMaximum(10)
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)

        # Size submit button
        self.size_submit = QtWidgets.QPushButton(self.centralwidget)
        self.size_submit.setMinimumSize(QtCore.QSize(150, 75))
        self.size_submit.setFont(font)
        self.size_submit.setMaximumSize(QtCore.QSize(125, 16777215))
        self.size_submit.setObjectName("size_submit")
        self.size_submit.clicked.connect(self.sendSize)
        self.gridLayout.addWidget(self.size_submit, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)

        # Spacers provide structure
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.size_submit.setText("Submit")
        if self.func == "det":
            self.size_info.setText("Use the box below to choose what size matrix you wish to enter and press the \"Submit\" button.")
            self.size_info1.setText("Remember, the determinant can only be calculated for a square matrix, which is a matrix that has the same number of rows and columns.")
            self.size_info2.setText("e.g. if you enter the number 4, the input will be a 4 x 4 matrix.")
        elif self.func == "inv":
            self.size_info.setText("Use the box below to choose what size matrix you wish to enter and press the \"Submit\" button.")
            self.size_info1.setText("Remember, the inverse of a matrix can only be calculated for a square matrix with a non-zero determinant,"
            +"\nwhich is a matrix that has the same number of rows and columns.")
            self.size_info2.setText("e.g. if you enter the number 4, the input will be a 4 x 4 matrix.")
        elif self.func == "e_val":
            self.size_info.setText("Use the box below to choose what size matrix you wish to enter and press the \"Submit\" button.")
            self.size_info1.setText("Remember, the eigenvalue can only be calculated for a square matrix, which is a matrix that has the same number of rows and columns.")
            self.size_info2.setText("e.g. if you enter the number 4, the input will be a 4 x 4 matrix.")
        elif self.func == "e_vec":
            self.size_info.setText("Use the box below to choose what size matrix you wish to enter and press the \"Submit\" button.")
            self.size_info1.setText("Remember, the eigenvector can only be calculated for a square matrix, which is a matrix that has the same number of rows and columns.")
            self.size_info2.setText("e.g. if you enter the number 4, the input will be a 4 x 4 matrix.")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Sending size to create matrix
    def sendSize(self):
        self.window = QMainWindow()
        self.ui = Ui_SquareInWindow(self.size.value(), self.func)
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()