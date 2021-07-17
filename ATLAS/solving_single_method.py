# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solving_single_method.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from os import listdir
from functools import partial
from view_changer import Changer
from closeWindow import QMainWindow

class Ui_SolveSingleWindow(object):
    def __init__(self, solutions):
        self.solutions = solutions

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 871)
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
        # self.next.clicked.connect(self.next_image) #######################
        # self.prev.clicked.connect(self.prev_image) #######################
        self.gridLayout.addWidget(self.prev, 2, 0, 1, 1)
        self.answer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.answer.setFont(font)
        self.answer.setObjectName("answer")
        self.gridLayout.addWidget(self.answer, 0, 0, 1, 2)
        self.showOriginalMatrix = QtWidgets.QPushButton(self.centralwidget)
        self.showOriginalMatrix.setObjectName("showOriginalMatrix")
        # self.showOriginalMatrix.clicked.connect(self.show_matrix) ###############
        self.image = Changer(self.scene, self.graphicsView)
        self.next.clicked.connect(self.image.next_image) #######################
        self.prev.clicked.connect(self.image.prev_image) #######################
        self.showOriginalMatrix.clicked.connect(self.image.show_matrix) ###############
        self.gridLayout.addWidget(self.showOriginalMatrix, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATLAS"))
        self.next.setText(_translate("MainWindow", "Next Step"))
        self.prev.setText(_translate("MainWindow", "Previous Step"))
        message = ""
        for i in self.solutions:
            message += str(i)
            message += ", "
        self.answer.setText(_translate("MainWindow", "Solution: "+str(message[:-2])))
        self.showOriginalMatrix.setText(_translate("MainWindow", "Show Original Matrix"))

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

    # def show_matrix(self):
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
    ui = Ui_SolveSingleWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
