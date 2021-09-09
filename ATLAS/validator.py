from PyQt5 import QtGui, QtWidgets, QtCore

# Validating inputs into QTableWidget
class Validator:
    # Constructor takes table and warning label as arguments
    def __init__(self, matrix, warning):
        self.matrix = matrix
        self.warning = warning

    # Validates an input
    def validation(self):
        # Gets current table input
        input_text = self.matrix.currentItem().text()
        # Rule for validating table input
        validation_rule = QtGui.QDoubleValidator(-1000000, 1000000, 10)
        # If input is valid, do nothing
        if validation_rule.validate(input_text, 0)[0] == QtGui.QValidator.Acceptable:
            pass
        # If input is invalid, reset and show warning
        else:
            # Invalid input is replaced with 0
            cell = self.matrix.currentIndex()
            self.matrix.setItem(cell.row(), cell.column(), QtWidgets.QTableWidgetItem('0'))

            sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            screen_height = sizeObject.height()
            screen_width = sizeObject.width()
            # Warning message is shown
            self.warning.setText("Invalid input! Only integers and decimals are accepted.")
            self.warning.setGeometry(QtCore.QRect(screen_width/2 - 500, screen_height/2 - 50, 1000, 100))
            self.warning.setAlignment(QtCore.Qt.AlignHCenter)

            # Warning message is faded
            self.fade(self.warning)

    # Fades any widget passed as argument
    def fade(self, widget):
        # Opacity effect
        self.effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)
        # Animating opacity effect
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(2500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()