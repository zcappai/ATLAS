from PyQt5 import QtCore, QtWidgets, QtCore
import time
from closeWindow import QMainWindow
from os import listdir
import saver

# GUI for progress bar while images generate
class Ui_LoadingWindow(object):
    # Initialises method object and single method viewing GUI
    def __init__(self, method, view_screen):
        self.method = method
        self.view_screen = view_screen

    # Setting up GUI
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 126)

        # Parent widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Provides structure to widget layout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Progress bar
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)

        # Generate solution button
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 1, 0, 1, 1)
        self.start_button.clicked.connect(self.solutionGen)

        MainWindow.setCentralWidget(self.centralwidget)

        # Setting text for button and window
        MainWindow.setWindowTitle("ATLAS")
        self.start_button.setText("Generate Solution")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Starts 2 threads: image generation and progress bar update
    def solutionGen(self):
        # Thread 1 generates images for step-by-step solutions
        self.thread1 = ImageGen(self.method)
        self.thread1.start()
        # Thread 2 updates progress bar as images are generated
        self.thread2 = ProgressUpdate()
        self.thread2.change_value.connect(self.setProgressVal)
        self.thread2.start()

    # Sets new progress bar value
    def setProgressVal(self, val):
        self.progressBar.setValue(val)
        # Terminates threads and loads solution viewing GUI
        if val == 100:
            self.thread1.terminate()
            self.thread2.terminate()
            self.window = QMainWindow()
            self.ui = self.view_screen
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()

# Thread for generating images
class ImageGen(QtCore.QThread):
    # Initialises method object
    def __init__(self, method):
        super().__init__()
        self.method = method

    # Runs thread for generating images
    def run(self):
        self.method.latex2img()

# Thread for calculating percentage completion
class ProgressUpdate(QtCore.QThread):
    change_value = QtCore.pyqtSignal(int)
    # Runs thread for calculating progress
    def run(self):
        percent = 0
        # Will run until progress bar is full
        while percent != 100.0:
            # Total number of images expected
            numExpected = len(saver.saved)
            images = listdir("images")
            # Total number of images saved
            numImages = len(images)
            new_percent = int((numImages/numExpected)*100)
            # If new percentage is higher, value is emitted
            if new_percent > percent:
                time.sleep(0.3)
                percent = new_percent
                self.change_value.emit(percent)