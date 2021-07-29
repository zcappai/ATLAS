from PyQt5 import QtWidgets
import emptyimg
import main_screen
import saver

class QMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.resize(sizeObject.width(), sizeObject.height())

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        close.setWindowTitle("ATLAS")
        close.setText("Are you sure you want to quit?\n(Press Reset to go to the main menu)")
        close.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Reset)
        close.setIcon(QtWidgets.QMessageBox.Question)
        close = close.exec()

        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
            emptyimg.empty()
        elif close == QtWidgets.QMessageBox.No:
            event.ignore()
        elif close == QtWidgets.QMessageBox.Reset:
            main_screen.MainWindow.show()
            emptyimg.empty()
            saver.saved = []