from PyQt5 import QtCore, QtGui, QtWidgets
from emptyimg import empty
from closeWindow import QMainWindow
from inverse_single_method import Ui_InverseSingleWindow
from det_single_method import Ui_DetSingleWindow
from eigenvalue_single_method import Ui_EigenvalueSingleWindow
from eigenvector_single_method import Ui_EigenvectorSingleWindow
from mult_single_method import Ui_MultSingleWindow
from solving_single_method import Ui_SolveSingleWindow
from loading_screen import Ui_LoadingWindow
from multiplication import Laderman, naiveMultiplication, Strassen
from determinant import naiveDeterminant, Sarrus, LU
from inverse import naiveInverse, CayleyHamilton
from solving import Cholesky, GaussianElimination, CramersRule
from eigenvalue import Eigenvalue
from eigenvector import Eigenvector

class Ui_SingleChoiceWindow(object):
    def __init__(self, arg, method):
        self.arg = arg
        self.method = method

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 3)
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setMinimumSize(QtCore.QSize(125, 50))
        self.submit_button.setMaximumSize(QtCore.QSize(125, 16777215))
        self.font = QtGui.QFont()
        self.font.setPointSize(20)
        self.submit_button.setFont(self.font)
        self.submit_button.setObjectName("submit_button")
        self.gridLayout.addWidget(self.submit_button, 7, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.methods_info = QtWidgets.QLabel(self.centralwidget)
        self.methods_info.setFont(self.font)
        self.methods_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.methods_info.setAlignment(QtCore.Qt.AlignCenter)
        self.methods_info.setWordWrap(True)
        self.methods_info.setObjectName("methods_info")
        self.gridLayout.addWidget(self.methods_info, 1, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        self.method_store = QtWidgets.QScrollArea(self.centralwidget)
        self.method_store.setWidgetResizable(True)
        self.method_store.setObjectName("method_store")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 358, 201))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.method_store.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.method_store, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.percent = 0

        if self.method == "mult":
            self.mult()
            self.submit_button.clicked.connect(self.multCall)
        elif self.method == "det":
            self.det()
            self.submit_button.clicked.connect(self.detCall)
        elif self.method == "inv":
            self.inv()
            self.submit_button.clicked.connect(self.invCall)
        elif self.method == "solve":
            self.solve()
            self.submit_button.clicked.connect(self.solveCall)
        elif self.method == "e_val":
            self.eigenvalue()
            self.submit_button.clicked.connect(self.eigenvalueCall)
        elif self.method == "e_vec":
            self.eigenvector()
            self.submit_button.clicked.connect(self.eigenvectorCall)

        # self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setObjectName("progressBar")
        # self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        # self.progressBar.setValue(0)
        # self.gridLayout.addWidget(self.progressBar, 10, 0, 1, 3)

        # self.loading_label = QtWidgets.QLabel(self.centralwidget)
        # self.loading_label.setObjectName("loading_label")
        # self.loading_label.setFont(self.font)
        # self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        # self.gridLayout.addWidget(self.loading_label, 9, 0, 1, 3)

        MainWindow.setWindowTitle("ATLAS")
        self.submit_button.setText("Submit")
        self.methods_info.setText("Select one of the methods below and click the \"Submit\" button:")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "ATLAS"))
    #     self.submit_button.setText(_translate("MainWindow", "Submit"))
    #     self.methods_info.setText(_translate("MainWindow", "Select one of the methods below and click the submit button:"))

    # def updateProgress(self):
    #     self.submit_button.hide()
    #     self.loading_label.setText("Please do NOT click the screen. The solution is loading...")
    #     time.sleep(1)
    #     while self.percent != 100.0:
    #         numSaved = len(saver.saved)
    #         images = listdir("images")
    #         numImages = len(images)
    #         self.percent = int((numImages/numSaved)*100)
    #         current_percent = int(self.progressBar.text()[:-1])
    #         if self.percent > current_percent:
    #             self.progressBar.reset()
    #             self.progressBar.setValue(self.percent)

    def mult(self):
        self.standard = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.standard.setObjectName("standard")
        self.verticalLayout.addWidget(self.standard)
        self.standard.setText("Standard Method")
        self.standard.setFont(self.font)

        self.strassen = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.strassen.setObjectName("strassen")
        self.verticalLayout.addWidget(self.strassen)
        self.strassen.setText("Strassen's Method")
        self.strassen.setFont(self.font)

        left = self.arg[0]
        right = self.arg[1]
        if left.rows == 3 and left.cols == 3 and right.rows == 3 and right.cols == 3:
            self.laderman = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
            self.laderman.setObjectName("laderman")
            self.verticalLayout.addWidget(self.laderman)
            self.laderman.setText("Laderman Method")
            self.laderman.setFont(self.font)

    def multCall(self):
        if self.standard.isChecked() == True:
            mult = naiveMultiplication(*self.arg)
            empty()
            mult.calc()
            mult.addSaved(True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadingWindow(mult, Ui_MultSingleWindow())
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
            # y = threading.Thread(target=self.updateProgress)
            # y.start()
            # mult.latex2img()
        elif self.strassen.isChecked() == True:
            mult = Strassen(*self.arg)
            empty()
            mult.calc()
            mult.addSaved(True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadingWindow(mult, Ui_MultSingleWindow())
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
            # y = threading.Thread(target=self.updateProgress)
            # y.start()
            # mult.latex2img()
        try:
            if self.laderman.isChecked() == True:
                empty()
                mult = Laderman(*self.arg)
                mult.calc()
                mult.addSaved(True)
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_LoadingWindow(mult, Ui_MultSingleWindow())
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
                # y = threading.Thread(target=self.updateProgress)
                # y.start()
                # mult.latex2img()
        except:
            pass

    def det(self):
        self.laplace = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.laplace.setObjectName("laplace")
        self.verticalLayout.addWidget(self.laplace)
        self.laplace.setText("Laplace Expansion")
        self.laplace.setFont(self.font)

        if self.arg.rows == 3:
            self.sarrus = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
            self.sarrus.setObjectName("sarrus")
            self.verticalLayout.addWidget(self.sarrus)
            self.sarrus.setText("Sarrus' Method")
            self.sarrus.setFont(self.font)

        self.lu = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.lu.setObjectName("lu")
        self.verticalLayout.addWidget(self.lu)
        self.lu.setText("LU Decomposition")
        self.lu.setFont(self.font)

    def detCall(self):
        if self.laplace.isChecked() == True:
            determinant = naiveDeterminant(self.arg)
            empty()
            ans = determinant.calc()
            determinant.addSaved(True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadingWindow(determinant, Ui_DetSingleWindow(ans))
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
            # determinant.latex2img()
        elif self.lu.isChecked() == True:
            empty()
            determinant = LU(self.arg)
            ans = determinant.calc()
            determinant.addSaved(True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadingWindow(determinant, Ui_DetSingleWindow(ans))
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
            # determinant.latex2img()
        try:
            if self.sarrus.isChecked() == True:
                empty()
                determinant = Sarrus(self.arg)
                ans = determinant.calc()
                determinant.addSaved(True)
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_LoadingWindow(determinant, Ui_DetSingleWindow(ans))
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
                # determinant.latex2img()
        except:
            pass

        # try:
        #     self.window = QtWidgets.QMainWindow()
        #     self.ui = Ui_DetSingleWindow(ans)
        #     self.ui.setupUi(self.window)
        #     self.MainWindow.hide()
        #     self.window.show()
        # except:
        #     pass

    def inv(self):
        self.standard = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.standard.setObjectName("standard")
        self.verticalLayout.addWidget(self.standard)
        self.standard.setText("Standard Method")
        self.standard.setFont(self.font)

        self.cayley = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.cayley.setObjectName("cayley")
        self.verticalLayout.addWidget(self.cayley)
        self.cayley.setText("Cayley-Hamilton Theorem")
        self.cayley.setFont(self.font)

    def invCall(self):
        if self.standard.isChecked() == True:
            empty()
            inverse = naiveInverse(self.arg)
            check, message = inverse.check()
            if check == True:
                inverse.calc()
                inverse.addSaved(True)
                ans = message
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_LoadingWindow(inverse, Ui_InverseSingleWindow(ans))
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
                # inverse.latex2img()
            elif check == False:
                # inverse.latex2img()
                inverse.addSaved(True)
                ans = message
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_LoadingWindow(inverse, Ui_InverseSingleWindow(ans))
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
        elif self.cayley.isChecked() == True:
            empty()
            inverse = CayleyHamilton(self.arg)
            check, message = inverse.check()
            if check == True:
                inverse.calc()
                inverse.addSaved(True)
                ans = message
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_LoadingWindow(inverse, Ui_InverseSingleWindow(ans))
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
                # inverse.latex2img()
                # ans = message
            elif check == False:
                inverse.addSaved(True)
                ans = message
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_LoadingWindow(inverse, Ui_InverseSingleWindow(ans))
                self.ui.setupUi(self.window)
                self.MainWindow.hide()
                self.window.show()
                # inverse.latex2img()
                # ans = message

        # try:
        #     self.window = QtWidgets.QMainWindow()
        #     self.ui = Ui_InverseSingleWindow(ans)
        #     self.ui.setupUi(self.window)
        #     self.MainWindow.hide()
        #     self.window.show()
        # except:
        #     pass

    def solve(self):
        self.gaussian = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.gaussian.setObjectName("gaussian")
        self.verticalLayout.addWidget(self.gaussian)
        self.gaussian.setText("Gaussian Elimination")
        self.gaussian.setFont(self.font)

        self.cramers = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.cramers.setObjectName("cramers")
        self.verticalLayout.addWidget(self.cramers)
        self.cramers.setText("Cramer's Rule")
        self.cramers.setFont(self.font)

        if Cholesky(self.arg).check() == True:
            self.cholesky = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
            self.cholesky.setObjectName("cholesky")
            self.verticalLayout.addWidget(self.cholesky)
            self.cholesky.setText("Cholesky Decomposition")
            self.cholesky.setFont(self.font)

    def solveCall(self):
        if self.gaussian.isChecked() == True:
            solve = GaussianElimination(self.arg)
            empty()
            ans = solve.calc()[1]
            solve.addSaved(True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadingWindow(solve, Ui_SolveSingleWindow(ans))
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
            # solve.latex2img()
        elif self.cramers.isChecked() == True:
            empty()
            solve = CramersRule(self.arg)
            ans = solve.calc()
            solve.addSaved(True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadingWindow(solve, Ui_SolveSingleWindow(ans))
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
            # solve.latex2img()
        elif self.cholesky.isChecked() == True:
            empty()
            solve = Cholesky(self.arg)
            ans = solve.calc()
            solve.addSaved(True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadingWindow(solve, Ui_SolveSingleWindow(ans))
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
            # solve.latex2img()

        # try:
        #     self.window = QtWidgets.QMainWindow()
        #     self.ui = Ui_SolveSingleWindow(ans)
        #     self.ui.setupUi(self.window)
        #     self.MainWindow.hide()
        #     self.window.show()
        # except:
        #     pass

    def eigenvalue(self):
        self.characteristic = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.characteristic.setObjectName("characteristic")
        self.verticalLayout.addWidget(self.characteristic)
        self.characteristic.setText("Characteristic Equation")
        self.characteristic.setFont(self.font)

    def eigenvalueCall(self):
        if self.characteristic.isChecked() == True:
            e_value = Eigenvalue(self.arg)
            empty()
            ans = e_value.calc()
            e_value.addSaved(True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadingWindow(e_value, Ui_EigenvalueSingleWindow(ans))
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()

    def eigenvector(self):
        self.gaussian = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.gaussian.setObjectName("gaussian")
        self.verticalLayout.addWidget(self.gaussian)
        self.gaussian.setText("Gaussian Elimination")
        self.gaussian.setFont(self.font)

    def eigenvectorCall(self):
        if self.gaussian.isChecked() == True:
            e_vector = Eigenvector(self.arg)
            empty()
            ans = e_vector.calc()
            e_vector.addSaved(True)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadingWindow(e_vector, Ui_EigenvectorSingleWindow(ans))
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
            # solve.latex2img()

        # try:
        #     self.window = QtWidgets.QMainWindow()
        #     self.ui = Ui_EigenvalueSingleWindow(ans)
        #     self.ui.setupUi(self.window)
        #     self.MainWindow.hide()
        #     self.window.show()
        # except:
        #     pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_SingleChoiceWindow(None, None)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
