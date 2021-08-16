from PyQt5 import QtCore, QtGui, QtWidgets
from compare_view_changer import CompareChanger
import inverse

# GUI for viewing all inverse methods
class Ui_InverseCompareWindow(object):
    # Setting up GUI
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")

        # Parent widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Scrollable area for QGraphicsViews and buttons for multiple methods
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1063, 1618))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        font = QtGui.QFont()
        font.setPointSize(30)

        # For getting image subfolder names
        methods = inverse.getMethods()

        # Provides structure to widget layout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)

        # Cramer's Rule #
        # Label
        self.label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 0, 0, 1, 1)

        # Next step button
        self.next_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.next_1.setObjectName("next_1")
        self.next_1.setFont(font)
        self.gridLayout_2.addWidget(self.next_1, 2, 1, 1, 1)

        # Previous step button
        self.prev_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.prev_1.setObjectName("prev_1")
        self.prev_1.setFont(font)
        self.gridLayout_2.addWidget(self.prev_1, 2, 0, 1, 1)

        # Show original matrix button
        self.original_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.original_1.setObjectName("original_1")
        self.original_1.setFont(font)
        self.gridLayout_2.addWidget(self.original_1, 3, 0, 1, 1)

        # Viewing all steps button
        self.viewAll_1 = QtWidgets.QPushButton(self.centralwidget)
        self.viewAll_1.setObjectName("viewAll_1")
        self.viewAll_1.setFont(font)
        self.gridLayout_2.addWidget(self.viewAll_1, 3, 1, 1, 1)

        # GraphicsView for displaying contents of GraphicsScene
        self.cramer = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.cramer.setMinimumSize(QtCore.QSize(0, 700))
        self.cramer.setObjectName("cramer")
        self.gridLayout_2.addWidget(self.cramer, 1, 0, 1, 2)

        # GraphicsScene for viewing images of solution
        self.scene_1 = QtWidgets.QGraphicsScene()
        self.cramer.setScene(self.scene_1)

        # For changing the image shown
        self.image_1 = CompareChanger(self.scene_1, self.cramer, methods[0][0])
        self.prev_1.clicked.connect(self.image_1.prev_image)
        self.next_1.clicked.connect(self.image_1.next_image)
        self.original_1.clicked.connect(self.image_1.show_matrix)
        self.viewAll_1.clicked.connect(self.image_1.show_single)

        # Cayley-Hamilton Theorem #
        # Label
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        # Previous step button
        self.prev_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.prev_2.setObjectName("prev_2")
        self.prev_2.setFont(font)
        self.gridLayout_2.addWidget(self.prev_2, 9, 0, 1, 1)

        # Next step button
        self.next_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.next_2.setObjectName("next_2")
        self.next_2.setFont(font)
        self.gridLayout_2.addWidget(self.next_2, 9, 1, 1, 1)

        # Show original matrix button
        self.original_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.original_2.setObjectName("original_2")
        self.original_2.setFont(font)
        self.gridLayout_2.addWidget(self.original_2, 10, 0, 1, 1)

        # Viewing all steps button
        self.viewAll_2 = QtWidgets.QPushButton(self.centralwidget)
        self.viewAll_2.setObjectName("viewAll_2")
        self.viewAll_2.setFont(font)
        self.gridLayout_2.addWidget(self.viewAll_2, 10, 1, 1, 1)

        # GraphicsView for displaying contents of GraphicsScene
        self.cayley = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.cayley.setMinimumSize(QtCore.QSize(0, 700))
        self.cayley.setObjectName("cayley")
        self.gridLayout_2.addWidget(self.cayley, 7, 0, 1, 2)

        # GraphicsScene for viewing images of solution
        self.scene_2 = QtWidgets.QGraphicsScene()
        self.cayley.setScene(self.scene_2)

        # For changing the image shown
        self.image_2 = CompareChanger(self.scene_2, self.cayley, methods[1][0])
        self.prev_2.clicked.connect(self.image_2.prev_image)
        self.next_2.clicked.connect(self.image_2.next_image)
        self.original_2.clicked.connect(self.image_2.show_matrix)
        self.viewAll_2.clicked.connect(self.image_2.show_single)

        MainWindow.setCentralWidget(self.centralwidget)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.label_1.setText("Cramer's Rule")
        self.next_1.setText("Next Step")
        self.prev_1.setText("Previous Step")
        self.original_1.setText("Show Original Matrices")
        self.viewAll_1.setText("View All Steps")

        self.label_2.setText("Cayley-Hamilton Theorem")
        self.next_2.setText("Next Step")
        self.prev_2.setText("Previous Step")
        self.original_2.setText("Show Original Matrices")
        self.viewAll_2.setText("View All Steps")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)