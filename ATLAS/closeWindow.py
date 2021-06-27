from PyQt5 import QtWidgets
import compare_emptyimg
import emptyimg

class QMainWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        close.setWindowTitle("ATLAS")
        close.setText("Are you sure you want to quit?")
        close.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        close = close.exec()

        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
            compare_emptyimg.empty()
            emptyimg.empty()
        else:
            event.ignore()