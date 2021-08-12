from PyQt5 import QtWidgets
import emptyimg
import main_screen
import saver

# Modifying QMainWindow to add exit dialog
class QMainWindow(QtWidgets.QMainWindow):
    # Constructor sets window to be maximised
    def __init__(self):
        super().__init__()
        self.showMaximized()
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.resize(sizeObject.width(), sizeObject.height())

    # Empties "images" folder when close or reset
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        close.setWindowTitle("ATLAS")
        close.setText("Are you sure you want to quit?\n(Press Reset to go to the main menu)")
        close.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Reset)
        close.setIcon(QtWidgets.QMessageBox.Question)
        close = close.exec()

        # Closes and empties "images" folder
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
            emptyimg.empty()
        # No action taken
        elif close == QtWidgets.QMessageBox.No:
            event.ignore()
        # Resets to main menu and empties "images" folder
        elif close == QtWidgets.QMessageBox.Reset:
            main_screen.MainWindow.show()
            emptyimg.empty()
            saver.saved = []