from PyQt5 import QtCore, QtGui, QtWidgets
from compare_view_changer import CompareChanger
import eigenvalue

# GUI for viewing all eigenvalue methods
class Ui_EigenvalueCompareWindow(object):
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
        methods = eigenvalue.getMethods()

        # Provides structure to widget layout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)

        # Characteristic Equation #
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
        self.graphicsView_1 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_1.setMinimumSize(QtCore.QSize(0, 700))
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.gridLayout_2.addWidget(self.graphicsView_1, 1, 0, 1, 2)

        # GraphicsScene for viewing images of solution
        self.scene_1 = QtWidgets.QGraphicsScene()
        self.graphicsView_1.setScene(self.scene_1)

        # For changing the image shown
        self.image_1 = CompareChanger(self.scene_1, self.graphicsView_1, methods[0][0])
        self.prev_1.clicked.connect(self.image_1.prev_image)
        self.next_1.clicked.connect(self.image_1.next_image)
        self.original_1.clicked.connect(self.image_1.show_matrix)
        self.viewAll_1.clicked.connect(self.image_1.show_single)

        MainWindow.setCentralWidget(self.centralwidget)

        # Setting text for labels, buttons and window
        MainWindow.setWindowTitle("ATLAS")
        self.label_1.setText("Characteristic Equation")
        self.next_1.setText("Next Step")
        self.prev_1.setText("Previous Step")
        self.original_1.setText("Show Original Matrix")
        self.viewAll_1.setText("View All Steps")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)