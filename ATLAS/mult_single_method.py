# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mult_single_method.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from view_changer import Changer
from closeWindow import QMainWindow

class Ui_MultSingleWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        # self.images = listdir("images")
        # self.images = sorted(self.images, key=self.getint)
        # self.cursor = 0
        # self.scene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/"+self.images[self.cursor]))) ###################
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 2)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setObjectName("next")
        self.gridLayout.addWidget(self.next, 2, 1, 1, 1)
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setObjectName("prev")
        self.gridLayout.addWidget(self.prev, 2, 0, 1, 1)
        self.image = Changer(self.scene, self.graphicsView)
        self.next.clicked.connect(self.image.next_image) #######################
        self.prev.clicked.connect(self.image.prev_image) #######################        
        # self.next.clicked.connect(self.next_image) #######################
        # self.prev.clicked.connect(self.prev_image) #######################
        font = QtGui.QFont()
        font.setPointSize(30)
        self.showOriginalMatrices = QtWidgets.QPushButton(self.centralwidget)
        self.showOriginalMatrices.setObjectName("showOriginalMatrices")
        self.showOriginalMatrices.clicked.connect(self.image.show_matrix) ###############
        # self.showOriginalMatrices.clicked.connect(self.show_matrices) ###############
        self.gridLayout.addWidget(self.showOriginalMatrices, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("ATLAS")
        self.next.setText("Next Step")
        self.prev.setText("Previous Step")
        self.showOriginalMatrices.setText("Show Original Matrices")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "ATLAS"))
    #     self.next.setText(_translate("MainWindow", "Next Step"))
    #     self.prev.setText(_translate("MainWindow", "Previous Step"))
    #     self.showOriginalMatrices.setText(_translate("MainWindow", "Show Original Matrices"))

    # def next_image(self):
    #     if self.cursor < len(self.images) - 1:
    #         self.cursor += 1
    #         self.newscene = QtWidgets.QGraphicsScene()
    #         self.graphicsView.setScene(self.newscene)
    #         self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/"+self.images[self.cursor])))
    #     else:
    #         pass

    # def prev_image(self):
    #     if self.cursor > 0:
    #         self.cursor -= 1
    #         self.newscene = QtWidgets.QGraphicsScene()
    #         self.graphicsView.setScene(self.newscene)
    #         self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/"+self.images[self.cursor])))
    #     else:
    #         pass

    # def show_matrices(self):
    #     self.newscene = QtWidgets.QGraphicsScene()
    #     self.graphicsView.setScene(self.newscene)
    #     self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/0.png")))

    # def getint(self, name):
    #     num, _ = name.split('.')
    #     return int(num)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MultSingleWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
