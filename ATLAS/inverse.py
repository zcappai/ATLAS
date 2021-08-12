import sympy as sp
import text2image
from determinant import naiveDeterminant
import compare_text2image
import saver

# Cramer's Rule
class naiveInverse:
    # Constructor takes square matrix as argument
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []

    # Checks the input matrix is invertible
    def check(self):
        # Calculates determinant of matrix
        det = naiveDeterminant(self.matrix).calc()
        # Invertible if determinant is non-zero
        if det == 0:
            self.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{No Inverse Exists}$$$$\\text{(Determinant of the matrix is 0)}"))
            saver.names += 1
            return False
        else:
            return True

    # Calculates the inverse matrix
    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        # Dealing with 1 x 1 matrix
        if self.size == 1:
            only_value = self.matrix[0]
            inverse = sp.Matrix([1/only_value])
            self.saved.append((saver.names, "\\text{Since the matrix has only 1 values,}$$$$\\text{the reciprocal is taken, giving an inverse of}$$$$"+sp.latex(sp.Matrix([1/only_value]))))
            saver.names += 1
            return inverse
        self.saved.append((saver.names, "\\text{First, we find the minors of each element.}$$$$\\text{The minor of an element ignores the values}"
        +"$$$$\\text{of the current row \& column and calculates}$$$$\\text{the determinant of the remaining values.}"))
        saver.names += 1
        minors = [] # Storing minors of each element
        # Calculating the minor of each element iteratively
        for i in range(self.size):
            for j in range(self.size):
                # Submatrix of current element
                curr_submatrix = self.matrix.minor_submatrix(i, j)
                # Minor of current element
                det = naiveDeterminant(curr_submatrix).calc()
                minors.append(det)
                self.saved.append((saver.names, "\\text{The element }a_{"+str(i+1)+str(j+1)+"}="+sp.latex(self.matrix.row(i).col(j)[0])
                +"$$$$\\text{ gives the matrix}"+sp.latex(curr_submatrix)+"$$$$\\text{with a determinant of }"+sp.latex(det)))
                saver.names += 1
        # Constructing the matrix of minors
        matrix_minors = sp.Matrix(self.size, self.size, minors)
        self.saved.append((saver.names, "\\text{Therefore, the matrix of minors is}$$$$"+sp.latex(matrix_minors)))
        saver.names += 1
        self.saved.append((saver.names, "\\text{To find the matrix of cofactors, we multiply}$$$$\\text{alternative elements by -1, such that no 2}"
        +"$$$$\\text{vertically or horizontally adjacent elements are}$$$$\\text{multiplied by -1.}"))
        saver.names += 1
        neg_toggle = 0
        cofactors = [] # Storing cofactors of each element
        # Calculating the cofactor of each element iteratively
        for i in range(self.size):
            curr_row = matrix_minors.row(i)
            # Multiplying alternative elements of row by -1
            # And appending to new list
            for i in curr_row:
                if neg_toggle % 2 == 0:
                    cofactors.append(i)
                    neg_toggle += 1
                elif neg_toggle % 2 == 1:
                    cofactors.append(-i)
                    neg_toggle += 1
            # For even-dimension matrix
            if self.size % 2 == 0:
                neg_toggle += 1
        # Constructing matrix of cofactors
        matrix_cofactors = sp.Matrix(self.size, self.size, cofactors)
        self.saved.append((saver.names, "\\text{Therefore, the matrix of cofactors is}$$$$"+sp.latex(matrix_cofactors)))
        saver.names += 1
        self.saved.append((saver.names, "\\text{Next, to find the adjugate, we transpose}$$$$\\text{the matrix of cofactors}"))
        saver.names += 1
        # Calculating adjugate of matrix of cofactors
        adjugate = matrix_cofactors.transpose()
        self.saved.append((saver.names, "\\text{Therefore, the adjugate is}$$$$"+sp.latex(adjugate)))
        saver.names += 1
        # Calculating determinant of input matrix
        final_det = naiveDeterminant(self.matrix).calc()
        self.saved.append((saver.names, "\\text{Then, we find the determinant of the original matrix}$$$$"+sp.latex(self.matrix)+"$$$$\\text{giving a determinant of }"+sp.latex(final_det)))
        saver.names += 1
        self.saved.append((saver.names, "\\text{Finally, we multiply }\\frac{1}{det}\\text{ by the adjugate}$$$$\\frac{"
        +sp.latex(1)+"}{"+sp.latex(final_det)+"}"+sp.latex(adjugate)+"="+sp.latex((1/final_det)*adjugate)))
        saver.names += 1
        # Calculating inverse of input matrix
        inverse = (1/final_det)*adjugate
        self.saved.append((saver.names, "\\text{Therefore, the inverse of the matrix is}$$$$"+sp.latex(inverse)))
        saver.names += 1
        return inverse

    # Adds steps from instance variable list to shared list
    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved

    # Converts the matrices and expressions to images for single method
    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])

    # Converts the matrices and expressions to images for method comparison
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Cramer")

# Cayley-Hamilton Theorem
class CayleyHamilton:
    # Constructor takes square matrix as argument
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []

    # Checks the input matrix is invertible
    def check(self):
        # Calculates determinant of matrix
        det = naiveDeterminant(self.matrix).calc()
        # Invertible if determinant is non-zero
        if det == 0:
            self.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{No Inverse Exists}$$$$\\text{(Determinant of the matrix is 0)}"))
            saver.names += 1
            return False
        else:
            return True

    # Calculates the inverse matrix
    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        # Dealing with empty matrix
        if self.size == 0:
            return sp.Matrix([])
        # Dealing with 1 x 1 matrix
        elif self.size == 1:
            only_value = self.matrix[0]
            inverse = sp.Matrix([1/only_value])
            self.saved.append((saver.names, "\\text{Since the matrix has only 1 values,}$$$$\\text{the reciprocal is taken, giving an inverse of}$$$$"+sp.latex(sp.Matrix([1/only_value]))))
            saver.names += 1
            return inverse
        # Square matrices larger than 1 x 1
        else:
            # Finding characteristic polynomial
            I = sp.eye(self.size) # Identity matrix
            M = sp.Symbol('M')
            M_I = M*I  # Identity matrix multiplied by variable
            new_matrix = self.matrix - M_I
            self.saved.append((saver.names, "\\text{First, subtract M multiplied by the}$$$$\\text{identity matrix from the matrix}$$$$"+sp.latex(self.matrix)+str('-')+sp.latex(M)+sp.latex(I)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{To form the following matrix}$$$$"+sp.latex(new_matrix)))
            saver.names += 1
            # Characteristic polynomial
            characteristic = naiveDeterminant(new_matrix).calc()
            expanded_det = sp.expand(characteristic)
            self.saved.append((saver.names, "\\text{Then, calculate the determinant of the}$$$$\\text{matrix giving the following expression}$$$$"+sp.latex(expanded_det)))
            saver.names += 1
            # Constant in characteristic polynomial
            constant = expanded_det.as_coefficients_dict().get(1)
            self.saved.append((saver.names, "\\text{By the Cayley-Hamilton theorem}$$$$"+sp.latex(expanded_det)+"=O"))
            saver.names += 1
            self.saved.append((saver.names, "\\text{Where }M\\text{ is the matrix, }$$$$O\\text{ is the empty matrix}$$$$\\text{and the constant is multiplied by }I"))
            saver.names += 1
            # Rearranging by taking constant to other side
            rearrange1 = expanded_det - constant
            self.saved.append((saver.names, "\\text{If there is a constant, it must}$$$$\\text{be taken to the other side}$$$$"+sp.latex(rearrange1)+"="+sp.latex(-constant)+"I"))
            saver.names += 1
            # Rearranging by dividing both sides by constant on other side
            rearrange2 = rearrange1/(-constant)
            self.saved.append((saver.names, "\\text{Then, the equation is divided by the constant}$$$$"+sp.latex(rearrange2)+"=I"))
            saver.names += 1
            # Rearranging by dividing both sides by matrix variable
            rearrange3 = rearrange2/M
            self.saved.append((saver.names, "\\text{Then, the equation is divided by the variable }M$$$$"+sp.latex(sp.expand(rearrange3))+"=M^{-1}"))
            saver.names += 1
            # Substituting input matrix into variable M to find inverse
            inverse = rearrange3.subs(M, self.matrix)
            self.saved.append((saver.names, "\\text{Finally, the matrix is substituted into the}$$$$\\text{variable }M\\text{ to calculate the inverse}"))
            saver.names += 1
            self.saved.append((saver.names, "M^{-1}="+sp.latex(inverse)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{Therefore, the inverse of the matrix is}$$$$"+sp.latex(inverse)))
            saver.names += 1
            return inverse

    # Adds steps from class variable list to shared list
    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved

    # Converts the matrices and expressions to images for single method
    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])

    # Converts the matrices and expressions to images for method comparison
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Cayley")

# Stores method class and name for subfolder
def getMethods():
    methods = []
    methods.append(("Cramer", naiveInverse))
    methods.append(("Cayley", CayleyHamilton))
    return methods