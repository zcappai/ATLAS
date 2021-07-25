from PyQt5 import QtGui, QtWidgets, QtCore

class Validator:
    def __init__(self, matrix, warning):
        self.matrix = matrix
        self.warning = warning

    def validate(self):
        input_text = self.matrix.currentItem().text()
        validation_rule = QtGui.QDoubleValidator(-100, 100, 10)
        if validation_rule.validate(input_text, 0)[0] == QtGui.QValidator.Acceptable:
            pass
        else:
            cell = self.matrix.currentIndex()
            self.matrix.setCurrentCell(cell.row(), cell.column())
            self.matrix.setItem(cell.row(), cell.column(), QtWidgets.QTableWidgetItem('0'))

            sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            screen_height = sizeObject.height()
            screen_width = sizeObject.width()
            self.warning.setText("Invalid input! Only integers and decimals are accepted.")
            self.warning.setGeometry(QtCore.QRect(screen_width/2 - 500, screen_height/2 - 50, 1000, 100))
            self.warning.setAlignment(QtCore.Qt.AlignHCenter)

            self.fade(self.warning)

    def fade(self, widget):
        self.effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(2500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    # def unfade(self, widget):
    #     self.effect = QtWidgets.QGraphicsOpacityEffect()
    #     widget.setGraphicsEffect(self.effect)

    #     self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
    #     self.animation.setDuration(2500)
    #     self.animation.setStartValue(0)
    #     self.animation.setEndValue(1)
    #     self.animation.start()