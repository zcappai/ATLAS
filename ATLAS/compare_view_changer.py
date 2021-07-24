from PyQt5 import QtGui, QtWidgets
from os import listdir

class CompareChanger:
    def __init__(self, initialScene, graphicsView, subfolder):
        self.cursor = 0
        self.images = listdir("images/{}".format(subfolder))
        self.images = sorted(self.images, key=self.getint)
        self.graphicsView = graphicsView
        self.subfolder = subfolder
        initialScene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}/{}".format(self.subfolder, self.images[self.cursor])))) ###################

    def next_image(self):
        if self.cursor < len(self.images) - 1:
            self.cursor += 1
            self.newscene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.newscene)
            self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}/{}".format(self.subfolder, self.images[self.cursor]))))
        else:
            pass

    def prev_image(self):
        if self.cursor > 0:
            self.cursor -= 1
            self.newscene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.newscene)
            self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}/{}".format(self.subfolder, self.images[self.cursor]))))
        else:
            pass

    def show_matrix(self):
        self.newscene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.newscene)
        self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}/{}".format(self.subfolder, self.images[0]))))

    def getint(self, name):
        num, _ = name.split('.')
        return int(num)