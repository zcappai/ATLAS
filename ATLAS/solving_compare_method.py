# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mult_compare_method.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from compare_view_changer import CompareChanger
import solving
from closeWindow import QMainWindow

class Ui_SolveCompareWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1063, 1618))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        font = QtGui.QFont()
        font.setPointSize(20)
        methods = solving.getMethods()

        # Gaussian Elimination
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.next_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.next_1.setObjectName("next_1")
        self.gridLayout_2.addWidget(self.next_1, 2, 1, 1, 1)

        self.prev_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.prev_1.setObjectName("prev_1")
        self.gridLayout_2.addWidget(self.prev_1, 2, 0, 1, 1)

        self.original_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.original_1.setObjectName("original_1")
        self.gridLayout_2.addWidget(self.original_1, 3, 0, 1, 2)

        self.gaussian = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.gaussian.setMinimumSize(QtCore.QSize(0, 700))
        self.gaussian.setObjectName("gaussian")
        self.gridLayout_2.addWidget(self.gaussian, 1, 0, 1, 2)
        self.scene_1 = QtWidgets.QGraphicsScene()
        self.gaussian.setScene(self.scene_1)

        self.image_1 = CompareChanger(self.scene_1, self.gaussian, methods[0][0])
        self.prev_1.clicked.connect(self.image_1.prev_image)
        self.next_1.clicked.connect(self.image_1.next_image)
        self.original_1.clicked.connect(self.image_1.show_matrix)

        # Cramer's Rule
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.prev_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.prev_2.setObjectName("prev_2")
        self.gridLayout_2.addWidget(self.prev_2, 9, 0, 1, 1)

        self.next_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.next_2.setObjectName("next_2")
        self.gridLayout_2.addWidget(self.next_2, 9, 1, 1, 1)

        self.original_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.original_2.setObjectName("original_2")
        self.gridLayout_2.addWidget(self.original_2, 10, 0, 1, 2)

        self.cramers = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.cramers.setMinimumSize(QtCore.QSize(0, 700))
        self.cramers.setObjectName("cramers")
        self.gridLayout_2.addWidget(self.cramers, 7, 0, 1, 2)
        self.scene_2 = QtWidgets.QGraphicsScene()
        self.cramers.setScene(self.scene_2)

        self.image_2 = CompareChanger(self.scene_2, self.cramers, methods[1][0])
        self.prev_2.clicked.connect(self.image_2.prev_image)
        self.next_2.clicked.connect(self.image_2.next_image)
        self.original_2.clicked.connect(self.image_2.show_matrix)

        # Cholesky Decomposition
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 11, 0, 1, 1)

        self.prev_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.prev_3.setObjectName("prev_3")
        self.gridLayout_2.addWidget(self.prev_3, 16, 0, 1, 1)

        self.next_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.next_3.setObjectName("next_3")
        self.gridLayout_2.addWidget(self.next_3, 16, 1, 1, 1)

        self.original_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.original_3.setObjectName("original_3")
        self.gridLayout_2.addWidget(self.original_3, 17, 0, 1, 2)

        self.cholesky = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.cholesky.setMinimumSize(QtCore.QSize(0, 700))
        self.cholesky.setObjectName("cholesky")
        self.gridLayout_2.addWidget(self.cholesky, 13, 0, 1, 2)
        self.scene_3 = QtWidgets.QGraphicsScene()
        self.cholesky.setScene(self.scene_3)

        self.image_3 = CompareChanger(self.scene_3, self.cholesky, methods[2][0])
        self.prev_3.clicked.connect(self.image_3.prev_image)
        self.next_3.clicked.connect(self.image_3.next_image)
        self.original_3.clicked.connect(self.image_3.show_matrix)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("ATLAS")
        self.next_1.setText("Next Step")
        self.prev_1.setText("Previous Step")
        self.original_1.setText("Show Original Matrices")
        self.next_2.setText("Next Step")
        self.prev_2.setText("Previous Step")
        self.original_2.setText("Show Original Matrices")
        self.next_3.setText("Next Step")
        self.prev_3.setText("Previous Step")
        self.original_3.setText("Show Original Matrices")
        self.label.setText("Gaussian Elimination")
        self.label_2.setText("Cramer's Rule")
        self.label_3.setText("Cholesky Decomposition")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "ATLAS"))
    #     self.next_1.setText(_translate("MainWindow", "Next Step"))
    #     self.prev_1.setText(_translate("MainWindow", "Previous Step"))
    #     self.original_1.setText(_translate("MainWindow", "Show Original Matrices"))
    #     self.next_2.setText(_translate("MainWindow", "Next Step"))
    #     self.prev_2.setText(_translate("MainWindow", "Previous Step"))
    #     self.original_2.setText(_translate("MainWindow", "Show Original Matrices"))
    #     self.next_3.setText(_translate("MainWindow", "Next Step"))
    #     self.prev_3.setText(_translate("MainWindow", "Previous Step"))
    #     self.original_3.setText(_translate("MainWindow", "Show Original Matrices"))
    #     self.label.setText(_translate("MainWindow", "Gaussian Elimination"))
    #     self.label_2.setText(_translate("MainWindow", "Cramer's Rule"))
    #     self.label_3.setText(_translate("MainWindow", "Cholesky Decomposition"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_SolveCompareWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
