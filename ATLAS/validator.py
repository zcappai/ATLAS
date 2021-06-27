from PyQt5 import QtGui, QtWidgets

class Validator:
    def __init__(self, matrix):
        self.matrix = matrix

    def validate(self):
        input_text = self.matrix.currentItem().text()
        validation_rule = QtGui.QDoubleValidator(-100, 100, 10)
        if validation_rule.validate(input_text, 0)[0] == QtGui.QValidator.Acceptable:
            pass
        else:
            cell = self.matrix.currentIndex()
            self.matrix.setCurrentCell(cell.row(), cell.column())
            self.matrix.setItem(cell.row(), cell.column(), QtWidgets.QTableWidgetItem('0'))
            print("INVALID!") ################### INSERT A POPUP MESSAGE HERE = "Invalid input. Default value set to 0."