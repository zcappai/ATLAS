from PyQt5 import QtGui, QtWidgets
from os import listdir

# Changes image shown by QGraphisView
class CompareChanger:
    # Sets initial image
    def __init__(self, initialScene, graphicsView, subfolder):
        self.cursor = 0 # Initial location in list of images
        self.graphicsView = graphicsView
        self.subfolder = subfolder # Initialising subfolder
        images = self.imageList() # Gets list of images in subfolder
        # Adding initial image to QGraphicsScene in QGraphicsView
        initialScene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}/{}".format(self.subfolder, images[self.cursor]))))

    # Changes to next image
    def next_image(self):
        # Gets list of images
        images = self.imageList()
        if self.cursor < len(images) - 1:
            self.cursor += 1
            self.newscene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.newscene)
            # Adding next image to QGraphicsScene in QGraphicsView
            self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}/{}".format(self.subfolder, images[self.cursor]))))
        else:
            pass

    # Changes to previous image
    def prev_image(self):
        # Gets list of images
        images = self.imageList()
        if self.cursor > 0:
            self.cursor -= 1
            self.newscene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.newscene)
            # Adding previous image to QGraphicsScene in QGraphicsView
            self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}/{}".format(self.subfolder, images[self.cursor]))))
        else:
            pass

    # Changes to original input matrix image
    def show_matrix(self):
        # Gets list of images
        images = self.imageList()
        self.newscene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.newscene)
        # Adding first image on list to QGraphicsScene in QGraphicsView
        self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}/{}".format(self.subfolder, images[0]))))

    # Changes to single image with all steps
    def show_single(self):
        self.newscene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.newscene)
        # Adding single view image to QGraphicsScene in QGraphicsView
        self.newscene.addPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("images/{}/{}".format(self.subfolder, "single.png"))))

    # Returns list of image names sorted in ascending order
    def imageList(self):
        images = listdir("images/{}".format(self.subfolder))
        images.remove("single.png")
        images = sorted(images, key=self.getint)
        return images

    # Gets 1st part of string split by .
    # e.g. "1.png" returns 1
    def getint(self, name):
        num, _ = name.split('.')
        return int(num)