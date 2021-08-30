from eigenvector_compare_method import Ui_EigenvectorCompareWindow
from eigenvalue_compare_method import Ui_EigenvalueCompareWindow
from PyQt5 import QtCore, QtWidgets, QtCore, QtGui
import time
from closeWindow import QMainWindow
from os import walk
from det_compare_method import Ui_DetCompareWindow
from mult_compare_method import Ui_MultCompareWindow
from inverse_compare_method import Ui_InverseCompareWindow
from solving_compare_method import Ui_SolveCompareWindow

# GUI for progress bar while images generate
class Ui_CompLoadingWindow(object):
    # Initialises list of method objects and single method viewing GUI
    def __init__(self, func, allMethods):
        self.func = func
        self.allMethods = allMethods

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
        # Progress bar
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setFont(font)
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)

        # Generate solutions button
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 1, 0, 1, 1)
        self.start_button.clicked.connect(self.solutionGen)

        MainWindow.setCentralWidget(self.centralwidget)

        # Setting text for button and window
        MainWindow.setWindowTitle("ATLAS")
        self.start_button.setText("Generate Solutions")
        self.start_button.setFont(font)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Starts 2 threads: image generation and progress bar update
    def solutionGen(self):
        # Thread 1 generates images for step-by-step solutions
        self.thread1 = ImageGen(self.allMethods)
        self.thread1.start()
        # Thread 2 updates progress bar as images are generated
        self.thread2 = ProgressUpdate(self.allMethods)
        self.thread2.new_value.connect(self.setPercentage)
        self.thread2.start()

    # Sets new progress bar value
    def setPercentage(self, val):
        self.progressBar.setValue(val)
        # Terminates threads and loads solution viewing GUI
        if val == 100:
            self.thread1.terminate()
            self.thread2.terminate()
            if self.func == "det":
                self.ui = Ui_DetCompareWindow()
            elif self.func == "mult":
                self.ui = Ui_MultCompareWindow()
            elif self.func == "inv":
                self.ui = Ui_InverseCompareWindow()
            elif self.func == "solve":
                self.ui = Ui_SolveCompareWindow()
            elif self.func == "e_val":
                self.ui = Ui_EigenvalueCompareWindow()
            elif self.func == "e_vec":
                self.ui = Ui_EigenvectorCompareWindow()
            self.window = QMainWindow()
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.showMaximized()

# Thread for generating images
class ImageGen(QtCore.QThread):
    # Initialises list of method objects
    def __init__(self, allMethods):
        super().__init__()
        self.allMethods = allMethods

    # Runs thread for generating images
    def run(self):
        for method in self.allMethods:
            method.compare_latex2img()

# Thread for calculating percentage completion
class ProgressUpdate(QtCore.QThread):
    # Initialises list of method objects
    def __init__(self, allMethods):
        super().__init__()
        self.allMethods = allMethods

    new_value = QtCore.pyqtSignal(int)
    # Runs thread for calculating progress
    def run(self):
        percent = 0
        # Total number of images expected
        totalExpected = 0
        for i in self.allMethods:
            totalExpected += len(i.saved)
        # Will run until progress bar is full
        while percent != 100.0:
            # Total number of images saved
            numImages = self.numberCurrImgs()
            new_percent = int((numImages/totalExpected)*100)
            # If new percentage is higher, value is emitted
            if new_percent > percent:
                time.sleep(0.3)
                percent = new_percent
                self.new_value.emit(percent)

    # Calculates total number of images saved in "images" directory
    def numberCurrImgs(self):
        numImages = 0
        for _, _, files in walk("images"):
            numImages += len(files)
        return numImages