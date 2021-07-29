from PyQt5 import QtGui, QtWidgets
from os import listdir

class Changer:
    def __init__(self, initialScene, graphicsView):
        self.cursor = 0
        images = self.imageList()
        self.graphicsView = graphicsView
        initialScene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/"+images[self.cursor]))) ###################

    def next_image(self):
        images = self.imageList()
        if self.cursor < len(images) - 1:
            self.cursor += 1
            self.newscene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.newscene)
            self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/"+images[self.cursor])))
        else:
            pass

    def prev_image(self):
        images = self.imageList()
        if self.cursor > 0:
            self.cursor -= 1
            self.newscene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.newscene)
            self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/"+images[self.cursor])))
        else:
            pass

    def show_matrix(self):
        self.newscene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.newscene)
        self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/0.png")))

    def getint(self, name):
        num, _ = name.split('.')
        return int(num)

    def imageList(self):
        images = listdir("images")
        images = sorted(images, key=self.getint)
        return images