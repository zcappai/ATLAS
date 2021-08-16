from PyQt5 import QtGui, QtWidgets
from os import listdir
from PyQt5 import QtCore

from PyQt5.QtCore import QRectF

# Changes image shown by QGraphisView
class Changer:
    # Sets initial image
    def __init__(self, initialScene, graphicsView):
        self.cursor = 0 # Initial location in list of images
        images = self.imageList() # Gets list of images
        self.graphicsView = graphicsView
        # Adding initial image to QGraphicsScene in QGraphicsView
        initialScene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/"+images[self.cursor])))

    # Changes to next image
    def next_image(self):
        # Gets list of images
        images = self.imageList()
        # Cursor will not be larger than number of images
        if self.cursor < len(images) - 1:
            self.cursor += 1
            self.newscene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.newscene)
            # Adding next image to QGraphicsScene in QGraphicsView
            self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/"+images[self.cursor])))
        else:
            pass

    # Changes to previous image
    def prev_image(self):
        # Gets list of images
        images = self.imageList()
        # Cursor will not go below 0
        if self.cursor > 0:
            self.cursor -= 1
            self.newscene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.newscene)
            # Adding previous image to QGraphicsScene in QGraphicsView
            self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/"+images[self.cursor])))
        else:
            pass

    # Changes to original input matrix image
    def show_matrix(self):
        # Gets list of images
        images = self.imageList()
        self.newscene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.newscene)
        # Adding first image on list to QGraphicsScene in QGraphicsView
        self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}".format(images[0]))))

    # Changes to single image with all steps
    def show_single(self):
        self.newscene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.newscene)
        # Adding single view image to QGraphicsScene in QGraphicsView
        self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}".format("single.png"))))

    # Returns list of image names sorted in ascending order
    def imageList(self):
        images = listdir("images")
        images.remove("single.png")
        images = sorted(images, key=self.getint)
        return images

    # Gets 1st part of string split by .
    # e.g. "1.png" returns 1
    def getint(self, name):
        num, _ = name.split('.')
        return int(num)