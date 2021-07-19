from emptyimg import empty
import sympy as sp
import text2image
import compare_text2image
from string import ascii_lowercase
from determinant import naiveDeterminant
import saver

class GaussianElimination:
    def __init__(self, matrix):
        self.matrix = matrix
        self.equations = matrix.rows
        self.unknowns = matrix.cols - 1
        # self.atoms = list(ascii_lowercase)
        # for x in range(self.unknowns//26):
        #     self.atoms += ["".join([i, str(x)]) for i in list(ascii_lowercase)]
        # saver.saved = []
        # saver.text = []

    def calc(self):
        saver.names = 0
        if self.equations < self.unknowns:
            message = "There are infinitely many solutions (or there are no solutions)"
            saver.text.append((saver.names, message))
            return False, [], None
        elif self.equations > self.unknowns:
            message = "There are no solutions (this is an overdetermined system)"
            saver.text.append((saver.names, message))
            return False, [], None
        else:
            # Applying Rouché–Capelli theorem
            aug = self.matrix[:, :]
            coef = self.matrix[:, :]
            saver.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1
            saver.text.append((saver.names, "Rouch\'e–Capelli theorem is used to identify inconsistent systems"))
            saver.names += 1
            saver.text.append((saver.names, "This is done by comparing the ranks of the augmented and coefficient matrices"))
            saver.names += 1
            coef.col_del(self.unknowns)
            saver.text.append((saver.names, "The augmented matrix rank is {}".format(aug.rank())))
            saver.names += 1
            saver.text.append((saver.names, "The coefficient matrix rank is {}".format(coef.rank())))
            saver.names += 1
            if aug.rank() > coef.rank():
                saver.text.append((saver.names, "Therefore, the system of linear equations is inconsistent and no solutions exist"))
                saver.names += 1
                return False, [], None
            saver.text.append((saver.names, "Therefore, the system of linear equations is consistent"))
            saver.names += 1
            saver.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1

            ## REFACTOR!!!!!!!
            n = self.equations
            for i in range(0, n):
                saver.text.append((saver.names, "For column..."))
                saver.names += 1
                saver.saved.append((saver.names, sp.latex(self.matrix.col(i))))
                saver.names += 1
                # Search for maximum in this column
                maxEl = abs(self.matrix.row(i).col(i)[0])
                maxRow = i
                for k in range(i + 1, n):
                    if abs(self.matrix.row(k).col(i)[0]) > maxEl:
                        maxEl = abs(self.matrix.row(k).col(i)[0])
                        maxRow = k
                saver.text.append((saver.names, "...find the maximum in the column, which is {} on row {}".format(maxEl, maxRow+1)))
                saver.names += 1

                # Swap maximum row with current row
                saver.text.append((saver.names, "Swap the current row..."))
                saver.names += 1
                saver.saved.append((saver.names, sp.latex(self.matrix.row(i))))
                saver.names += 1
                saver.text.append((saver.names, "...and the row with the maximum value"))
                saver.names += 1
                saver.saved.append((saver.names, sp.latex(self.matrix.row(maxRow))))
                saver.names += 1
                self.matrix.row_swap(maxRow, i)
                saver.text.append((saver.names, "To give the matrix"))
                saver.names += 1
                saver.saved.append((saver.names, sp.latex(self.matrix)))
                saver.names += 1

                # Make all rows below this one 0 in current column
                saver.text.append((saver.names, "Now all elements below the current row in the current column must be 0"))
                saver.names += 1
                for k in range(i + 1, n):
                    c = self.matrix.row(k).col(i)[0] / self.matrix.row(i).col(i)[0]
                    if c == sp.nan:
                        pass
                    else:
                        saver.text.append((saver.names, "Taking the ratio between {} and {} in...". format(self.matrix.row(k).col(i)[0], self.matrix.row(i).col(i)[0])))
                        saver.names += 1
                        saver.saved.append((saver.names, sp.latex(self.matrix.col(i))))
                        saver.names += 1
                        saver.text.append((saver.names, "...gives the ratio {}".format(c)))
                        saver.names += 1
                        saver.text.append((saver.names, "This ratio is substracted from row {} by multiplying the ratio by values from row {}".format(k+1, i+1)))
                        saver.names += 1
                        self.matrix.row_op(k, lambda a, j: a - c*self.matrix[i, j])
                        saver.text.append((saver.names, "To give the following matrix"))
                        saver.names += 1
                        saver.saved.append((saver.names, sp.latex(self.matrix)))
                        saver.names += 1
                saver.text.append((saver.names, "This results in the following matrix"))
                saver.names += 1
                saver.saved.append((saver.names, sp.latex(self.matrix)))
                saver.names += 1

            saver.text.append((saver.names, "This matrix is now in row echelon form"))
            saver.names += 1
            saver.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1
            row_ech = self.matrix[:, :]

            # Solve equation Ax=b for an upper triangular matrix A
            x = [0 for i in range(n)]
            saver.text.append((saver.names, "Now use back substitution to find the solutions"))
            saver.names += 1
            for i in range(n - 1, -1, -1):
                x[i] = self.matrix.row(i).col(n)[0] / self.matrix.row(i).col(i)[0]
                if x[i] == sp.nan: #####################################################
                    x[i] = 1
                saver.text.append((saver.names, "On row..."))
                saver.names += 1
                saver.saved.append((saver.names, sp.latex(self.matrix.row(i))))
                saver.names += 1
                saver.text.append((saver.names, "...dividing {} by {} gives the solution {}".format(self.matrix.row(i).col(n)[0], self.matrix.row(i).col(i)[0], x[i])))
                self.matrix[i, i] = 1
                self.matrix[i, n] = x[i]
                saver.names += 1
                for k in range(i - 1, -1, -1):
                    saver.text.append((saver.names, "For row..."))
                    saver.names += 1
                    saver.saved.append((saver.names, sp.latex(self.matrix.row(k))))
                    saver.names += 1
                    saver.text.append((saver.names, "Remove the value {} and multiply by the solution {} to subtract from the constant".format(self.matrix.row(k).col(i)[0], x[i])))
                    saver.names += 1
                    self.matrix[k, n] -= self.matrix.row(k).col(i)[0] * x[i]
                    self.matrix[k, i] = 0
                    saver.text.append((saver.names, "To give the matrix"))
                    saver.names += 1
                    saver.saved.append((saver.names, sp.latex(self.matrix)))
                    saver.names += 1
            saver.text.append((saver.names, "Now the matrix is in the form..."))
            saver.names += 1
            saver.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1
            saver.text.append((saver.names, "...where the constants are the solutions"))
            saver.names += 1
            saver.saved.append((saver.names, sp.latex(x)))
            saver.names += 1
            return True, x, row_ech

    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0]) ######################
        for i in saver.text:
            text2image.toImage(i[1], i[0]) ######################

    def compare_latex2img(self, subfolder):
        for i in saver.saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder) ######################
        for i in saver.text:
            compare_text2image.toImage(i[1], i[0], subfolder) ######################

class CramersRule:
    def __init__(self, matrix):
        self.matrix = matrix
        self.equations = matrix.rows
        self.unknowns = matrix.cols - 1
        # self.atoms = list(ascii_lowercase)
        # for x in range(self.unknowns//26):
        #     self.atoms += ["".join([i, str(x)]) for i in list(ascii_lowercase)]
        # saver.saved = []
        # saver.text = []

    def calc(self):
        if self.equations < self.unknowns:
            message = "There are infinitely many solutions (or there are no solutions)"
            saver.text.append((saver.names, message))
            return ["No unique solutions"]
        elif self.equations > self.unknowns:
            message = "There are no solutions (this is an overdetermined system)"
            saver.text.append((saver.names, message))
            return ["No unique solutions"]
        else:
            saver.saved.append((saver.names, sp.latex(self.matrix[:, :])))
            saver.names += 1
            if self.unknowns == -1 and self.equations == 0:
                return []
            solutions = []
            saver.text.append((saver.names, "The matrix of coefficients is..."))
            saver.names += 1
            mat_coeff = self.matrix[:, :]
            mat_coeff.col_del(-1)
            saver.saved.append((saver.names, sp.latex(mat_coeff)))
            saver.names += 1
            det_mat_coeff = naiveDeterminant(mat_coeff).calc()
            saver.text.append((saver.names, "...with a determinant of {}".format(det_mat_coeff)))
            saver.names += 1
            if det_mat_coeff == 0:
                saver.text.append((saver.names, "Since the determinant is {}, no solutions exist".format(det_mat_coeff)))
                saver.names += 1
                return []
            for i in range(self.unknowns):
                saver.text.append((saver.names, "In the matrix...".format(i+1)))
                saver.names += 1
                saver.saved.append((saver.names, sp.latex(self.matrix[:, :])))
                saver.names += 1
                mat = self.matrix[:, :]
                mat.col_swap(i, -1)
                saver.text.append((saver.names, "Column {} is swapped with the column of constants to give".format(i+1)))
                saver.names += 1
                saver.saved.append((saver.names, sp.latex(mat[:, :])))
                saver.names += 1
                mat.col_del(-1)
                saver.text.append((saver.names, "Then, the last column is removed from the matrix to give"))
                saver.names += 1
                saver.saved.append((saver.names, sp.latex(mat[:, :])))
                saver.names += 1
                det_new_matrix = naiveDeterminant(mat).calc()
                solution = det_new_matrix/det_mat_coeff
                saver.text.append((saver.names, "The determinant of this matrix is {}".format(det_new_matrix)))
                saver.names += 1
                saver.text.append((saver.names, "Dividing the determinants of this matrix {} by that of the matrix of coefficients {}...".format(det_new_matrix, det_mat_coeff)))
                saver.names += 1
                saver.text.append((saver.names, "...gives the solution of {}".format(solution)))
                saver.names += 1
                solutions.append(solution)
            saver.text.append((saver.names, "Therefore, the solutions are..."))
            saver.names += 1
            saver.saved.append((saver.names, str(solutions)))
            saver.names += 1
            return solutions

    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0]) ######################
        for i in saver.text:
            text2image.toImage(i[1], i[0]) ######################

    def compare_latex2img(self, subfolder):
        for i in saver.saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder) ######################
        for i in saver.text:
            compare_text2image.toImage(i[1], i[0], subfolder) ######################

class Cholesky:
    def __init__(self, matrix):
        self.matrix = matrix
        self.equations = matrix.rows
        self.unknowns = matrix.cols - 1
        # self.atoms = list(ascii_lowercase)
        # for x in range(self.unknowns//26):
        #     self.atoms += ["".join([i, str(x)]) for i in list(ascii_lowercase)]
        # saver.saved = []
        # saver.text = []

    def check(self):
        if self.equations < self.unknowns:
            message = "There are infinitely many solutions (or there are no solutions)"
            saver.text.append((saver.names, message))
            saver.names += 1
            return False
        elif self.equations > self.unknowns:
            message = "There are no solutions (this is an overdetermined system)"
            saver.text.append((saver.names, message))
            saver.names += 1
            return False
        else:
            # https://www.gaussianwaves.com/2013/04/tests-for-positive-definiteness-of-a-matrix/
            square = self.matrix[:, :]
            square.col_del(-1)
            transposed = square.T
            if square == transposed:
                pass
            else:
                return False
            determinants = []
            det = naiveDeterminant(square).calc()
            determinants.append(det)
            while square.cols > 1:
                square.col_del(-1)
                square.row_del(-1)
                det = naiveDeterminant(square).calc()
                determinants.append(det)
            for i in determinants:
                if i < 0:
                    return False
            return True

    def calc(self):
        saver.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        if self.unknowns == -1 and self.equations == 0:
            return [], True
        check_compatible = self.check()
        if check_compatible == True:
            A = self.matrix[:, :]
            n = self.equations

            # Create zero matrix for L
            L = sp.Matrix(n, n, [0]*n*n)

            # Perform the Cholesky decomposition
            for i in range(n):
                for k in range(i+1):
                    tmp_sum = sum(L.row(i).col(j)[0] * L.row(k).col(j)[0] for j in range(k))
                    if (i == k): # Diagonal elements
                        L[i, k] = sp.sqrt(A.row(i).col(i)[0] - tmp_sum)
                    else:
                        L[i, k] = (1.0 / L.row(k).col(k)[0] * (A.row(i).col(k)[0] - tmp_sum))

            # Forward substitution
            L = L.col_insert(n+1, A.col(-1))
            x = [0 for i in range(n)]
            for i in range(0, n):
                x[i] = L.row(i).col(n)[0] / L.row(i).col(i)[0]
                if x[i] == sp.nan: #####################################################
                    x[i] = 1
                for k in range(i + 1, n):
                    L[k, n] -= L.row(k).col(i)[0] * x[i]
                L[i, n] = x[i]

            # Transposed matrix
            L.col_del(-1)
            L = L.T
            L = L.col_insert(n+1,sp.Matrix(n, 1, x))

            # Back substitution
            x = [0 for i in range(n)]
            for i in range(n - 1, -1, -1):
                x[i] = sp.N(L.row(i).col(n)[0] / L.row(i).col(i)[0], 10)
                if x[i] == sp.nan: #####################################################
                    x[i] = 1
                L[i, i] = 1
                L[i, n] = x[i]
                for k in range(i - 1, -1, -1):
                    L[k, n] -= L.row(k).col(i)[0] * x[i]
                    L[k, i] = 0
            return x, check_compatible
        else:
            return [], check_compatible

    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0]) ######################
        for i in saver.text:
            text2image.toImage(i[1], i[0]) ######################

    def compare_latex2img(self, subfolder):
        for i in saver.saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder) ######################
        for i in saver.text:
            compare_text2image.toImage(i[1], i[0], subfolder) ######################

def getMethods():
    methods = []
    methods.append(("Gaussian", GaussianElimination))
    methods.append(("Cramers", CramersRule))
    methods.append(("Cholesky", Cholesky))
    return methods

# empty()
# x = sp.Matrix([[1,1,1,9],[2,-3,4,13],[3,4,5,40]])
# x = sp.Matrix([[0, 0, 0, 0],[1, 0, 1, 0],[-1, 0, -1, 0]])
# x = sp.Matrix([[6,15,55,76],[15,55,225,295],[55,225,979,1259]])
# x = sp.Matrix([[2,-1,0,3],[-1,2,-1,4],[0,-1,2,5]])
# sp.pprint(x)
# new = Cholesky(x)
# print(new.check())
# sp.pprint(new.calc())
# new.latex2img()