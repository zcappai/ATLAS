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
        self.saved = []
        # self.text = []

    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        if self.equations < self.unknowns:
            message = "\\text{There are infinitely many}$$$$\\text{solutions (or there are no solutions)}"
            self.saved.append((saver.names, message))
            return False, [], None
        elif self.equations > self.unknowns:
            message = "\\text{There are no solutions }$$$$\\text{(this is an overdetermined system)}"
            self.saved.append((saver.names, message))
            return False, [], None
        else:
            # Applying Rouché–Capelli theorem
            aug = self.matrix[:, :]
            coef = self.matrix[:, :]
            self.saved.append((saver.names, """\\text{Rouch\\'e–Capelli theorem is used to identify}
            $$$$\\text{inconsistent systems. This is done by comparing}$$$$\\text{the ranks of the augmented and coefficient matrices.}"""))
            saver.names += 1
            coef.col_del(self.unknowns)
            self.saved.append((saver.names, "\\text{The rank of the augmented matrix}$$$$"+sp.latex(aug)+"$$$$\\text{is }"+sp.latex(aug.rank())))
            saver.names += 1
            self.saved.append((saver.names, "\\text{The rank of the coefficient matrix}$$$$"+sp.latex(coef)+"$$$$\\text{is }"+sp.latex(coef.rank())))
            saver.names += 1
            if aug.rank() > coef.rank():
                self.saved.append((saver.names, "\\text{Since the rank of the augmented matrix is}$$$$\\text{larger than the rank of the coefficient matrix,}"
                "$$$$\\text{the system of linear equations is}$$$$\\text{inconsistent and no solutions exist.}"))
                saver.names += 1
                return False, [], None
            self.saved.append((saver.names, "\\text{Since the rank of the augmented matrix is}$$$$\\text{NOT larger than the rank of the coefficient matrix,}"
            +"$$$$\\text{the system of linear equations is consistent}"))
            saver.names += 1

            ## REFACTOR!!!!!!!
            n = self.equations
            self.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{Now, partial pivoting is used, which}$$$$\\text{is the process of swapping rows based on the}"
            +"$$$$\\text{maximum absolute value in the current column}$$$$\\text{below the current element. This is}$$$$\\text{used to improve numerical stability,}"
            +"$$$$\\text{as it helps to reduce rounding errors.}"))
            saver.names += 1
            for i in range(0, n):
                # Search for maximum in this column
                maxEl = abs(self.matrix.row(i).col(i)[0])
                maxRow = i
                for k in range(i + 1, n):
                    if abs(self.matrix.row(k).col(i)[0]) > maxEl:
                        maxEl = abs(self.matrix.row(k).col(i)[0])
                        maxRow = k
                self.saved.append((saver.names, "\\text{For column }"+sp.latex(self.matrix.col(i))
                +"\\text{the maximum absolute in the column}$$$$\\text{ below the current element }"+sp.latex(self.matrix.row(i).col(i)[0])+"\\text{ is }"+sp.latex(maxEl)+"\\text{ on row }"+sp.latex(maxRow+1)))
                saver.names += 1

                # Swap maximum row with current row
                self.saved.append((saver.names, "\\text{Swap the current row}$$$$"+sp.latex(self.matrix.row(i))+"$$$$\\text{and the row with the maximum value}$$$$"+sp.latex(self.matrix.row(maxRow))))
                saver.names += 1
                self.matrix.row_swap(maxRow, i)
                self.saved.append((saver.names, "\\text{This gives the matrix}$$$$"+sp.latex(self.matrix)))
                saver.names += 1

                # Make all rows below this one 0 in current column
                self.saved.append((saver.names, "\\text{Now all elements below the current}$$$$\\text{row in the current column must be 0}"))
                saver.names += 1
                for k in range(i + 1, n):
                    c = self.matrix.row(k).col(i)[0] / self.matrix.row(i).col(i)[0]
                    if c == sp.nan:
                        pass
                    else:
                        self.saved.append((saver.names, "\\text{Taking the ratio between }"+sp.latex(self.matrix.row(k).col(i)[0])+"\\text{ and }"+sp.latex(self.matrix.row(i).col(i)[0])
                        +"\\text{ in }"+sp.latex(self.matrix.col(i))+"\\text{gives the ratio }"+sp.latex(c)))
                        saver.names += 1
                        self.saved.append((saver.names, "\\text{This ratio is substracted from row }"+sp.latex(k+1)+"$$$$\\text{ by multiplying the ratio by values from row }"+sp.latex(i+1)))
                        saver.names += 1
                        self.matrix.row_op(k, lambda a, j: a - c*self.matrix[i, j])
                        self.saved.append((saver.names, "\\text{This gives the following matrix}$$$$"+sp.latex(self.matrix)))
                        saver.names += 1
                self.saved.append((saver.names, "\\text{Now, all the elements below the current row}$$$$\\text{in the current column are 0}$$$$"+sp.latex(self.matrix)))
                saver.names += 1

            self.saved.append((saver.names, "\\text{The matrix is now in row echelon form}$$$$"+sp.latex(self.matrix)))
            saver.names += 1
            row_ech = self.matrix[:, :]

            # Solve equation Ax=b for an upper triangular matrix A
            x = [0 for i in range(n)]
            self.saved.append((saver.names, "\\text{Now use back substitution to find the solutions}"))
            saver.names += 1
            for i in range(n - 1, -1, -1):
                x[i] = self.matrix.row(i).col(n)[0] / self.matrix.row(i).col(i)[0]
                if x[i] == sp.nan: #####################################################
                    x[i] = 1
                if x[i] == 0:
                    x[i] = 1
                self.saved.append((saver.names, "\\text{On row }"+sp.latex(self.matrix.row(i))
                +"\\text{dividing }"+sp.latex(self.matrix.row(i).col(n)[0])+"\\text{ by }"
                +sp.latex(self.matrix.row(i).col(i)[0])+"$$$$\\text{gives the solution }"+sp.latex(x[i])))
                self.matrix[i, i] = 1
                self.matrix[i, n] = x[i]
                saver.names += 1
                for k in range(i - 1, -1, -1):
                    self.saved.append((saver.names, "\\text{For row }"+sp.latex(self.matrix.row(k))
                    +"$$$$\\text{Remove the value }"+sp.latex(self.matrix.row(k).col(i)[0])
                    +"\\text{ and multiply by the solution }"+sp.latex(x[i])+"$$$$\\text{to subtract from the constant}"))
                    saver.names += 1
                    self.matrix[k, n] -= self.matrix.row(k).col(i)[0] * x[i]
                    self.matrix[k, i] = 0
                    self.saved.append((saver.names, "\\text{This gives the matrix}$$$$"+sp.latex(self.matrix)))
                    saver.names += 1
            self.saved.append((saver.names, "\\text{Now the matrix is in the form}$$$$"+sp.latex(self.matrix)+"$$$$\\text{where }"+sp.latex(x)+"\\text{ are the solutions}"))
            saver.names += 1
            return True, x, row_ech

    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved
            # saver.text = saver.text + self.text

    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
        # for i in saver.text:
        #     text2image.toImage(i[1], i[0])

    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Gaussian")
        # for i in saver.text:
        #     compare_text2image.toImage(i[1], i[0], "Gaussian")

class CramersRule:
    def __init__(self, matrix):
        self.matrix = matrix
        self.equations = matrix.rows
        self.unknowns = matrix.cols - 1
        # self.atoms = list(ascii_lowercase)
        # for x in range(self.unknowns//26):
        #     self.atoms += ["".join([i, str(x)]) for i in list(ascii_lowercase)]
        self.saved = []
        # self.text = []

    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        if self.equations < self.unknowns:
            message = "\\text{There are infinitely many}$$$$\\text{solutions (or there are no solutions)}"
            self.saved.append((saver.names, message))
            return ["No unique solutions"]
        elif self.equations > self.unknowns:
            message = "\\text{There are no solutions }$$$$\\text{(this is an overdetermined system)}"
            self.saved.append((saver.names, message))
            return ["No unique solutions"]
        else:
            # Applying Rouché–Capelli theorem
            aug = self.matrix[:, :]
            coef = self.matrix[:, :]
            self.saved.append((saver.names, """\\text{Rouch\\'e–Capelli theorem is used to identify}
            $$$$\\text{inconsistent systems. This is done by comparing}$$$$\\text{the ranks of the augmented and coefficient matrices.}"""))
            saver.names += 1
            coef.col_del(self.unknowns)
            self.saved.append((saver.names, "\\text{The rank of the augmented matrix}$$$$"+sp.latex(aug)+"$$$$\\text{is }"+sp.latex(aug.rank())))
            saver.names += 1
            self.saved.append((saver.names, "\\text{The rank of the coefficient matrix}$$$$"+sp.latex(coef)+"$$$$\\text{is }"+sp.latex(coef.rank())))
            saver.names += 1
            if aug.rank() > coef.rank():
                self.saved.append((saver.names, "\\text{Since the rank of the augmented matrix is}$$$$\\text{larger than the rank of the coefficient matrix,}"
                "$$$$\\text{the system of linear equations is}$$$$\\text{inconsistent and no solutions exist.}"))
                saver.names += 1
                return False, [], None
            self.saved.append((saver.names, "\\text{Since the rank of the augmented matrix is}$$$$\\text{NOT larger than the rank of the coefficient matrix,}"
            +"$$$$\\text{the system of linear equations is consistent}"))
            saver.names += 1

            self.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1
            if self.unknowns == -1 and self.equations == 0:
                return []
            solutions = []
            mat_coeff = self.matrix[:, :]
            mat_coeff.col_del(-1)
            det_mat_coeff = naiveDeterminant(mat_coeff).calc()
            self.saved.append((saver.names, "\\text{The matrix of coefficients is}$$$$"+sp.latex(mat_coeff)+"$$$$\\text{with a determinant of }"+sp.latex(det_mat_coeff)))
            saver.names += 1
            if det_mat_coeff == 0:
                self.saved.append((saver.names, "\\text{Since the determinant is }"+sp.latex(det_mat_coeff)+",$$$$\\text{no solutions exist}"))
                saver.names += 1
                return []
            for i in range(self.unknowns):
                self.saved.append((saver.names, "\\text{In the matrix}$$$$"+sp.latex(self.matrix[:, :])))
                saver.names += 1
                mat = self.matrix[:, :]
                mat.col_swap(i, -1)
                self.saved.append((saver.names, sp.latex(self.matrix.col(i))+"\\text{ and }"+sp.latex(self.matrix.col(-1))+"\\text{ are swapped to give}$$$$"
                +sp.latex(mat[:, :])+"$$$$\\text{These are columns }"+sp.latex(i+1)+"\\text{ and the column of constants.}"))
                saver.names += 1
                mat.col_del(-1)
                det_new_matrix = naiveDeterminant(mat).calc()
                solution = det_new_matrix/det_mat_coeff
                self.saved.append((saver.names, "\\text{Then, the last column is removed}$$$$\\text{from the matrix to give}$$$$"+sp.latex(mat[:, :])+"$$$$\\text{with a determinant of }"+sp.latex(det_new_matrix)))
                saver.names += 1
                self.saved.append((saver.names, "\\text{Dividing the determinants of this matrix }"+sp.latex(det_new_matrix)
                +"$$$$\\text{by that of the matrix of coefficients }"+sp.latex(det_mat_coeff)+"$$$$\\text{gives a solution of }"+sp.latex(solution)))
                saver.names += 1
                solutions.append(solution)
            self.saved.append((saver.names, "\\text{Therefore, the solutions are}$$$$"+sp.latex(solutions)))
            saver.names += 1
            return solutions

    def addSaved(self, check):
        if check == True:
            saver.saved = saver.saved + self.saved
            # saver.text = saver.text + self.text

    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
        # for i in saver.text:
        #     text2image.toImage(i[1], i[0])

    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Cramers")
        # for i in saver.text:
            # compare_text2image.toImage(i[1], i[0], "Cramers")

class Cholesky:
    def __init__(self, matrix):
        self.matrix = matrix
        self.equations = matrix.rows
        self.unknowns = matrix.cols - 1
        # self.atoms = list(ascii_lowercase)
        # for x in range(self.unknowns//26):
        #     self.atoms += ["".join([i, str(x)]) for i in list(ascii_lowercase)]
        self.saved = []
        # self.text = []

    def check(self):
        if self.equations < self.unknowns:
            message = "\\text{There are infinitely many}$$$$\\text{solutions (or there are no solutions)}"
            self.saved.append((saver.names, message))
            return False
        elif self.equations > self.unknowns:
            message = "\\text{There are no solutions }$$$$\\text{(this is an overdetermined system)}"
            self.saved.append((saver.names, message))
            return False
        else:
            # https://www.gaussianwaves.com/2013/04/tests-for-positive-definiteness-of-a-matrix/
            self.saved.append((saver.names, "\\text{First, we check that the matrix of coefficients}$$$$\\text{is both symmetric and positive definite.}"
            +"$$$$\\text{The matrix of coefficients is symmetric, if}$$$$\\text{the matrix of coefficients is equal to its transpose.}"
            +"$$$$\\text{The matrix of coefficients is positive definite,}$$$$\\text{if the determinant of each upper left square}$$$$\\text{(sub)matrix is positive.}"))
            saver.names += 1
            square = self.matrix[:, :]
            square.col_del(-1)
            transposed = square.T
            self.saved.append((saver.names, sp.latex(square)+"\\text{ is the matrix of coefficients}"))
            saver.names += 1
            self.saved.append((saver.names, sp.latex(transposed)+"\\text{ is the transposed matrix of coefficients}"))
            saver.names += 1
            if square == transposed:
                self.saved.append((saver.names, "\\text{Since the matrix of coefficients and its}$$$$\\text{transpose are equal, the matrix is symmetric.}"))
                saver.names += 1
                pass
            else:
                self.saved.append((saver.names, "\\text{Since the matrix of coefficients and its}$$$$\\text{transpose are NOT equal, the matrix is NOT symmetric.}"))
                saver.names += 1
                return False
            determinants = []
            det = naiveDeterminant(square).calc()
            self.saved.append((saver.names, "\\text{Now check that each of the upper left}$$$$\\text{square (sub)matrices has a positive determinant.}"))
            saver.names += 1
            self.saved.append((saver.names, "\\text{The determinant of }$$$$"+sp.latex(square)+"\\text{ is } "+str(det)))
            saver.names += 1
            determinants.append(det)
            while square.cols > 1:
                square.col_del(-1)
                square.row_del(-1)
                det = naiveDeterminant(square).calc()
                self.saved.append((saver.names, "\\text{The determinant of }$$$$"+sp.latex(square)+"\\text{ is } "+str(det)))
                saver.names += 1
                determinants.append(det)
            for i in determinants:
                if i < 0:
                    self.saved.append((saver.names, "\\text{Since the determinant for an upper left submatrix}"
                    +"$$$$\\text{is }"+str(1)+"\\text{, the matrix of coefficients is NOT}$$$$\\text{positive definite.}"
                    +"$$$$\\text{ Therefore, the system of linear equation is}$$$$\\text{NOT compatiable with Cholesky Decomposition.}"))
                    saver.names += 1
                    return False
            self.saved.append((saver.names, "\\text{Since the determinant for all upper left submatrices}$$$$\\text{is positive, the matrix of coefficients is positive}"
            +"$$$$\\text{ definite. Also, since the matrix of coefficients}$$$$\\text{is also equal to its own transpose, the matrix}"
            +"$$$$\\text{of coefficients is symmetric. Therefore, the}$$$$\\text{system of linear equation is compatible with}$$$$\\text{Cholesky Decomposition.}"))
            saver.names += 1
            return True

    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        if self.unknowns == -1 and self.equations == 0:
            return []
        check_compatible = self.check()
        if check_compatible == True:
            A = self.matrix[:, :]
            n = self.equations

            # Create zero matrix for L
            L = sp.Matrix(n, n, [0]*n*n)
            self.saved.append((saver.names, "\\text{Now, create an empty }"+sp.latex(n)+"x"+sp.latex(n)
            +"\\text{ matrix for the}$$$$\\text{lower triangular matrix formed by}$$$$\\text{Cholesky Decomposition}"))
            saver.names += 1
            self.saved.append((saver.names, sp.latex(L)))
            saver.names += 1

            # Perform the Cholesky decomposition
            self.saved.append((saver.names, "\\text{Then, the formula }$$$$l_{ki} = \\frac{a_{ki}-\sum_{j=1}^{i-1} l_{ij}\cdot l_{kj}}{l_{ii}}$$$$\\text{ is applied to the lower left elements}"))
            saver.names += 1
            self.saved.append((saver.names, "\\text{The formula is rearranged to }$$$$l_{ii} = \sqrt{a_{ii}-\sum_{j=1}^{i-1} l_{ij}^2}$$$$\\text{ for diagonal elements } (k=i)"))
            saver.names += 1
            for i in range(n):
                for k in range(i+1):
                    tmp_sum = sum(L.row(i).col(j)[0] * L.row(k).col(j)[0] for j in range(k))
                    self.saved.append((saver.names, "\\text{For the element }l_{"+str(i+1)+str(k+1)+"""}, 
                    \\text{ the sum is }$$$$\sum_{j=1}^{"""+str(k)+"} l_{"+str(k+1)+"j}\cdot l_{"+str(i+1)+"j}"))
                    saver.names += 1
                    self.saved.append((saver.names, "\\text{This gives a value of }"+sp.latex(tmp_sum)))
                    saver.names += 1
                    if (i == k): # Diagonal elements
                        L[i, k] = sp.sqrt(A.row(i).col(i)[0] - tmp_sum)
                        self.saved.append((saver.names, """\\text{For this diagonal element, the formula is } 
                        $$$$l_{"""+str(i+1)+str(i+1)+"} = \sqrt{a_{"+str(i+1)+str(i+1)+"}-"+sp.latex(tmp_sum)+"}"))
                        saver.names += 1
                        self.saved.append((saver.names, """\\text{Therefore, the value of the element is } 
                        $$$$l_{"""+str(i+1)+str(i+1)+"} = \sqrt{"+sp.latex(A.row(i).col(i)[0])+"-"+sp.latex(tmp_sum)+"}="+sp.latex(L[i, k])))
                        saver.names += 1
                    else:
                        L[i, k] = (1.0 / L.row(k).col(k)[0] * (A.row(i).col(k)[0] - tmp_sum))
                        self.saved.append((saver.names, """\\text{For this non-diagonal element, the formula is }
                        $$$$l_{"""+str(i+1)+str(k+1)+"} = \\frac{a_{"+str(i+1)+str(k+1)+"}-"+sp.latex(tmp_sum)+"}{l_{"+str(k+1)+str(k+1)+"}}"))
                        self.saved.append((saver.names, """\\text{Therefore, the value of the element is } 
                        $$$$l_{"""+str(i+1)+str(k+1)+"} = \\frac{"""+sp.latex(A.row(i).col(i)[0])+"-"+sp.latex(tmp_sum)+"}{"+sp.latex(L.row(k).col(k)[0])+"}="+sp.latex(L[i, k])))
                        saver.names += 1
                    self.saved.append((saver.names, "\\text{The lower triangular matrix is }$$$$"+sp.latex(L)+"$$$$\\text{so far}"))
                    saver.names += 1

            # Forward substitution
            pre_change_L = L[:, :]
            self.saved.append((saver.names, "\\text{Forward substitution is now used}$$$$\\text{to change the column of constants }"+sp.latex(A.col(-1))))
            saver.names += 1
            L = L.col_insert(n+1, A.col(-1))
            self.saved.append((saver.names, "\\text{Starting with the lower triangular matrix}$$$$\\text{with the column of constants}$$$$"+sp.latex(L)))
            saver.names += 1
            x = [0 for i in range(n)]
            for i in range(0, n):
                x[i] = L.row(i).col(n)[0] / L.row(i).col(i)[0]
                self.saved.append((saver.names, "\\text{On row }"+sp.latex(L.row(i))+",$$$$\\text{dividing }"+sp.latex(L.row(i).col(n)[0])
                +"\\text{ by }"+sp.latex(L.row(i).col(i)[0])+"$$$$\\text{gives }"+sp.latex(x[i])))
                L[i, i] = 1
                saver.names += 1
                if x[i] == sp.nan: #####################################################
                    self.saved.append((saver.names, "\\text{Since the solution is undefined, it is set to 1}"))
                    saver.names += 1
                    x[i] = 1
                L[i, n] = x[i]
                self.saved.append((saver.names, "\\text{The solution is substituted back into the matrix}"))
                saver.names += 1
                for k in range(i + 1, n):
                    self.saved.append((saver.names, "\\text{For row }$$$$"+sp.latex(L.row(k))+", $$$$\\text{multiply }"+sp.latex(L.row(k).col(i)[0])
                    +"\\text{ by }"+sp.latex(x[i])+"$$$$\\text{and subtract from }"+sp.latex(L[k, n])))
                    saver.names += 1
                    L[k, n] -= L.row(k).col(i)[0] * x[i]
                    L[k, i] = 0
                    self.saved.append((saver.names, "\\text{This results in a value of }"+sp.latex(L[k, n])))
                    saver.names += 1
                    self.saved.append((saver.names, "\\text{The lower triangular matrix is}$$$$"+sp.latex(L)+"$$$$\\text{so far}"))
                    saver.names += 1
                self.saved.append((saver.names, "\\text{The resultant lower triangular matrix is}$$$$"+sp.latex(L)))
                saver.names += 1

            # Transposed matrix
            pre_change_L = pre_change_L.T
            L = pre_change_L.col_insert(n+1,sp.Matrix(n, 1, x))
            self.saved.append((saver.names, """\\text{The matrix of coefficients of the}
            $$$$\\text{lower triangular matrix is then transposed}$$$$\\text{and the new columnn of coefficients is appended}$$$$"""+sp.latex(L)))
            saver.names += 1

            # Back substitution
            self.saved.append((saver.names, "\\text{Back substitution is now used to find the solutions}"))
            saver.names += 1
            x = [0 for i in range(n)]
            for i in range(n - 1, -1, -1):
                x[i] = L.row(i).col(n)[0] / L.row(i).col(i)[0]
                self.saved.append((saver.names, "\\text{On row }"+sp.latex(L.row(i))+", $$$$\\text{dividing }"+sp.latex(L.row(i).col(n)[0])
                +"\\text{ by }"+sp.latex(L.row(i).col(i)[0])+"$$$$\\text{gives }"+sp.latex(x[i])))
                saver.names += 1
                if x[i] == sp.nan: #####################################################
                    self.saved.append((saver.names, "\\text{Since the solution is undefined, it is set to 1}"))
                    saver.names += 1
                    x[i] = 1
                L[i, i] = 1
                L[i, n] = x[i]
                self.saved.append((saver.names, "\\text{The solution is substituted back into the matrix}"))
                saver.names += 1
                for k in range(i - 1, -1, -1):
                    self.saved.append((saver.names, "\\text{For row }$$$$"+sp.latex(L.row(k))+", $$$$\\text{multiply }"+sp.latex(L.row(k).col(i)[0])
                    +"\\text{ by }"+sp.latex(x[i])+"$$$$\\text{and subtract from }"+sp.latex(L[k, n])))
                    saver.names += 1
                    L[k, n] -= L.row(k).col(i)[0] * x[i]
                    self.saved.append((saver.names, "\\text{This results in a value of }"+sp.latex(L[k, n])))
                    saver.names += 1
                    L[k, i] = 0
                    # print(L[k, n])
                    # print(round(L[k, n], 4))
                    self.saved.append((saver.names, "\\text{The lower triangular matrix is}$$$$"+sp.latex(L)+"$$$$\\text{so far}"))
                    saver.names += 1
            self.saved.append((saver.names, "\\text{Therefore, the final matrix is}$$$$"+sp.latex(L)+"$$$$\\text{where }"+sp.latex(x)+"$$$$\\text{ are the solutions}"))
            saver.names += 1
            return x
        else:
            return []

    def addSaved(self, check):
        if check == True:
            saver.saved = saver.saved + self.saved
            # saver.text = saver.text + self.text

    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0]) ######################
        # for i in saver.text:
        #     text2image.toImage(i[1], i[0]) ######################

    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Cholesky") ######################
        # for i in saver.text:
        #     compare_text2image.toImage(i[1], i[0], "Cholesky") ######################

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
# new = GaussianElimination(x)
# sp.pprint(new.calc())
# new.addSaved(True)
# new.latex2img()