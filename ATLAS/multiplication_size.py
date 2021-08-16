from PyQt5 import QtCore, QtGui, QtWidgets
from multiplication_input import Ui_MultInWindow
from closeWindow import QMainWindow

# Matrix Multiplication Matrix Size GUI
class Ui_MultSizeWindow(object):
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
        self.gridLayout.addWidget(self.mul_size_info, 0, 0, 1, 7)

        self.mult_size_info2 = QtWidgets.QLabel(self.centralwidget)
        self.mult_size_info2.setFont(font)
        self.mult_size_info2.setWordWrap(True)
        self.mult_size_info2.setObjectName("mult_size_info2")
        self.gridLayout.addWidget(self.mult_size_info2, 1, 0, 1, 7)

        self.mult_size_info3 = QtWidgets.QLabel(self.centralwidget)
        self.mult_size_info3.setFont(font)
        self.mult_size_info3.setWordWrap(True)
        self.mult_size_info3.setObjectName("mult_size_info3")
        self.gridLayout.addWidget(self.mult_size_info3, 2, 0, 1, 7)

        # Spinbox labels
        self.leftmatrixdim_label = QtWidgets.QLabel(self.centralwidget)
        self.leftmatrixdim_label.setFont(font)
        self.leftmatrixdim_label.setAlignment(QtCore.Qt.AlignCenter)
        self.leftmatrixdim_label.setObjectName("leftmatrixdim_label")
        self.gridLayout.addWidget(self.leftmatrixdim_label, 4, 1, 1, 1)

        self.shareddim_label = QtWidgets.QLabel(self.centralwidget)
        self.shareddim_label.setFont(font)
        self.shareddim_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shareddim_label.setObjectName("shareddim_label")
        self.gridLayout.addWidget(self.shareddim_label, 4, 3, 1, 1)

        self.rightmatrixdim_label = QtWidgets.QLabel(self.centralwidget)
        self.rightmatrixdim_label.setFont(font)
        self.rightmatrixdim_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rightmatrixdim_label.setObjectName("rightmatrixdim_label")
        self.gridLayout.addWidget(self.rightmatrixdim_label, 4, 5, 1, 1)

        # Matrix size spinbox
        self.leftmatrixdim = QtWidgets.QSpinBox(self.centralwidget)
        self.leftmatrixdim.setMinimumSize(QtCore.QSize(150, 75))
        self.leftmatrixdim.setFont(font)
        self.leftmatrixdim.setMaximum(10)
        self.leftmatrixdim.setAlignment(QtCore.Qt.AlignCenter)
        self.leftmatrixdim.setObjectName("leftmatrixdim")
        self.gridLayout.addWidget(self.leftmatrixdim, 5, 1, 1, 1)

        self.shareddim = QtWidgets.QSpinBox(self.centralwidget)
        self.shareddim.setMinimumSize(QtCore.QSize(150, 75))
        self.shareddim.setFont(font)
        self.shareddim.setMaximum(10)
        self.shareddim.setAlignment(QtCore.Qt.AlignCenter)
        self.shareddim.setObjectName("shareddim")
        self.gridLayout.addWidget(self.shareddim, 5, 3, 1, 1)

        self.rightmatrixdim = QtWidgets.QSpinBox(self.centralwidget)
        self.rightmatrixdim.setMinimumSize(QtCore.QSize(150, 75))
        self.rightmatrixdim.setFont(font)
        self.rightmatrixdim.setMaximum(10)
        self.rightmatrixdim.setAlignment(QtCore.Qt.AlignCenter)
        self.rightmatrixdim.setObjectName("rightmatrixdim")
        self.gridLayout.addWidget(self.rightmatrixdim, 5, 5, 1, 1)

        # Size submit button
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setMinimumSize(QtCore.QSize(150, 75))
        self.submit.setObjectName("submit")
        self.submit.setFont(font)
        self.submit.clicked.connect(self.sendSize)
        self.gridLayout.addWidget(self.submit, 7, 3, 1, 1)

        # Spacers provide structure
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 8, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.mul_size_info.setText("In order for 2 matrices to be successfully multiplied, 1 dimension from each matrix must be the same.")
        self.mult_size_info2.setText("Therefore, given 2 matrices with dimensions m x n and n x p. The dimension n must be the same for both matrices."
        +"\nRemember that the dimenions of a matrix are represented as \"number of rows\" x \"number of columns\".")
        self.mult_size_info3.setText("e.g. a matrix with 1 row and 3 columns (1 x 3 matrix) would be compatible with a matrix with 3 rows and 6 columns (3 x 6 matrix),"
        +"\nresulting in a matrix with 1 row and 6 columns.")
        self.leftmatrixdim_label.setText("m")
        self.shareddim_label.setText("n")
        self.rightmatrixdim_label.setText("p")
        self.submit.setText("Submit")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Sending sizes to create matrices
    def sendSize(self):
        self.window = QMainWindow()
        self.ui = Ui_MultInWindow(self.leftmatrixdim.value(), self.shareddim.value(), self.rightmatrixdim.value())
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.showMaximized()