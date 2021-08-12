from PyQt5 import QtCore, QtWidgets
from view_changer import Changer

# GUI for viewing solution to multiple method
class Ui_NonNumSingleWindow(object):
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

        # GraphicsView for displaying contents of GraphicsScene
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 2)

        # GraphicsScene for viewing images of solution
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

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

        # For changing the image shown
        self.image = Changer(self.scene, self.graphicsView)
        self.next.clicked.connect(self.image.next_image)
        self.prev.clicked.connect(self.image.prev_image)
        self.showMatrix.clicked.connect(self.image.show_matrix)

        MainWindow.setCentralWidget(self.centralwidget)

        # Setting text for buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.next.setText("Next Step")
        self.prev.setText("Previous Step")
        self.showMatrix.setText("Show Original Matrices")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)