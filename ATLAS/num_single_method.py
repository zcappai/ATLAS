from PyQt5 import QtCore, QtGui, QtWidgets
from view_changer import Changer

# GUI for viewing solution to single method
# Solution is numerical value(s)
class Ui_NumSingleWindow(object):
    # Initialising numerical answer(s) and function ID
    def __init__(self, solution, func):
        self.solution = solution
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
        # Label for displaying numerical answer(s)
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setObjectName("answer")
        self.answer.setFont(font)
        self.gridLayout.addWidget(self.answer, 0, 0, 1, 2)

        # Next step button
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setObjectName("next")
        self.gridLayout.addWidget(self.next, 2, 1, 1, 1)

        # Previous step button
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setObjectName("prev")
        self.gridLayout.addWidget(self.prev, 2, 0, 1, 1)

        # Show original matrix button
        self.showMatrix = QtWidgets.QPushButton(self.centralwidget)
        self.showMatrix.setObjectName("showMatrix")
        self.gridLayout.addWidget(self.showMatrix, 3, 0, 1, 2)

        # GraphicsView for displaying contents of GraphicsScene
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 2)

        # GraphicsScene for viewing images of solution
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        # For changing the image shown
        self.image = Changer(self.scene, self.graphicsView)
        self.next.clicked.connect(self.image.next_image)
        self.prev.clicked.connect(self.image.prev_image)
        self.showMatrix.clicked.connect(self.image.show_matrix)

        MainWindow.setCentralWidget(self.centralwidget)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.next.setText("Next Step")
        self.prev.setText("Previous Step")
        # Displaying solutions on QLabel depending on function
        if self.func == "det":
            self.answer.setText("Determinant: "+str(self.solution))
        else:
            message = ""
            for i in self.solution:
                message += str(i)
                message += ", "
            if self.func == "solve":
                self.answer.setText("Solution: "+str(message[:-2]))
            elif self.func == "e_val":
                self.answer.setText("Eigenvalues: \u03BB = "+str(message[:-2]))
        self.showMatrix.setText("Show Original Matrix")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)