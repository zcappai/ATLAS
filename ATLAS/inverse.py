from pydoc import text
import sympy as sp
from determinant import naiveDeterminant
from emptyimg import empty
import text2image
import compare_text2image

class naiveInverse:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []
        self.text = []
        self.names = 0

    def check(self):
        det = naiveDeterminant(self.matrix).calc()
        if det == 0:
            self.saved.append((self.names, sp.latex(self.matrix)))
            self.names += 1
            self.text.append((self.names, "No Inverse Exists"))
            self.names += 1
            return False, "No Inverse Exists (Determinant of the matrix is 0)"
        else:
            return True, "Inverse Exists!"

    def calc(self):
        curr = []
        self.saved.append((self.names, sp.latex(self.matrix)))
        self.names += 1
        if self.size == 1:
            only_value = self.matrix[0]
            self.text.append((self.names, "Since the matrix has only 1 values, the reciprocal is taken"))
            self.names += 1
            self.saved.append((self.names, sp.latex(sp.Matrix([1/only_value]))))
            self.names += 1
            return sp.Matrix([1/only_value])
        self.text.append((self.names, "First, we find the minors of each element"))
        self.names += 1
        self.text.append((self.names, "The minor ignores the values on the current row & column..."))
        self.names += 1
        self.text.append((self.names, "...and calculates the determinant of the remaining values"))
        self.names += 1
        minors = []
        for i in range(self.size):
            for j in range(self.size):
                curr_submatrix = self.matrix.minor_submatrix(i, j)
                self.text.append((self.names, "The element "+sp.latex(self.matrix.row(i).col(j)[0])+" gives the matrix"))
                self.names += 1
                self.saved.append((self.names, sp.latex(curr_submatrix)))
                self.names += 1
                det = naiveDeterminant(curr_submatrix).calc()
                minors.append(det)
                self.text.append((self.names, "This has a determinant of {}".format(det)))
                self.names += 1
                curr.append(curr_submatrix)
        matrix_minors = sp.Matrix(self.size, self.size, minors)
        self.text.append((self.names, "Therefore, the matrix of minors is"))
        self.names += 1
        self.saved.append((self.names, sp.latex(matrix_minors)))
        self.names += 1
        self.text.append((self.names, "To find the matrix of cofactors, we multiply alternative elements by -1..."))
        self.names += 1
        self.text.append((self.names, "...such that no 2 vertically or horizontally adjacent elements are multiplied by -1"))
        self.names += 1
        neg_toggle = 0
        cofactors = []
        if self.size % 2 == 0:
            for i in range(self.size):
                curr_row = matrix_minors.row(i)
                for i in curr_row:
                    if neg_toggle % 2 == 0:
                        cofactors.append(i)
                        neg_toggle += 1
                    elif neg_toggle % 2 == 1:
                        cofactors.append(-i)
                        neg_toggle += 1
                neg_toggle += 1
        else:
            for i in matrix_minors:
                if neg_toggle % 2 == 0:
                    cofactors.append(i)
                    neg_toggle += 1
                elif neg_toggle % 2 == 1:
                    cofactors.append(-i)
                    neg_toggle += 1
        matrix_cofactors = sp.Matrix(self.size, self.size, cofactors)
        self.text.append((self.names, "Therefore, the matrix of cofactors is"))
        self.names += 1
        self.saved.append((self.names, sp.latex(matrix_cofactors)))
        self.names += 1
        self.text.append((self.names, "Next, to find the adjugate, we transpose the matrix of cofactors"))
        self.names += 1
        self.text.append((self.names, "Therefore, the adjugate is"))
        self.names += 1
        adjugate = matrix_cofactors.transpose()
        self.saved.append((self.names, sp.latex(adjugate)))
        self.names += 1
        self.text.append((self.names, "Then, we find the determinant of the original matrix"))
        self.names += 1
        self.saved.append((self.names, sp.latex(self.matrix)))
        self.names += 1
        self.text.append((self.names, "Giving a determinant of"))
        self.names += 1
        final_det = naiveDeterminant(self.matrix).calc()
        self.saved.append((self.names, sp.latex(final_det)))
        self.names += 1
        self.text.append((self.names, "Finally, we multiply 1/det by the adjugate as follows"))
        self.names += 1
        self.saved.append((self.names, "\\frac{"+sp.latex(1)+"}{"+sp.latex(final_det)+"}"+sp.latex(adjugate)+"="+sp.latex((1/final_det)*adjugate)))
        self.names += 1
        inverse = (1/final_det)*adjugate
        self.text.append((self.names, "Therefore, the inverse of the matrix is"))
        self.names += 1
        self.saved.append((self.names, sp.latex(inverse)))
        self.names += 1
        return inverse

    def latex2img(self):
        for i in self.saved:
            text2image.formula_as_file(i[1], i[0])
        for i in self.text:
            text2image.toImage(i[1], i[0])

    def compare_latex2img(self, subfolder):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder)
        for i in self.text:
            compare_text2image.toImage(i[1], i[0], subfolder)

class CayleyHamilton:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []
        self.text = []
        self.names = 0

    def check(self):
        det = naiveDeterminant(self.matrix).calc()
        if det == 0:
            self.saved.append((self.names, sp.latex(self.matrix)))
            self.names += 1
            self.text.append((self.names, "No Inverse Exists"))
            self.names += 1
            return False, "No Inverse Exists (Determinant of the matrix is 0)"
        else:
            return True, "Inverse Exists!"

    def calc(self):
        self.saved.append((self.names, sp.latex(self.matrix)))
        self.names += 1
        if self.size == 0:
            return sp.Matrix([])
        elif self.size == 1:
            only_value = self.matrix[0]
            self.text.append((self.names, "Since the matrix has only 1 values, the reciprocal is taken"))
            self.names += 1
            self.saved.append((self.names, sp.latex(sp.Matrix([1/only_value]))))
            self.names += 1
            return sp.Matrix([1/only_value])
        else:
            I = sp.eye(self.size)
            M = sp.Symbol('M')
            M_I = M*I
            new_matrix = self.matrix - M_I
            self.text.append((self.names, "First, subtract M multiplied by the identity matrix from the matrix"))
            self.names += 1
            self.saved.append((self.names, sp.latex(self.matrix)+str('-')+sp.latex(M)+sp.latex(I)))
            self.names += 1
            self.text.append((self.names, "To form the following matrix"))
            self.names += 1
            self.saved.append((self.names, sp.latex(new_matrix)))
            self.names += 1
            self.text.append((self.names, "Then, calculate the determinant of this matrix"))
            self.names += 1
            characteristic = naiveDeterminant(new_matrix).calc()
            self.text.append((self.names, "Giving the following expression"))
            self.names += 1
            self.saved.append((self.names, sp.latex(characteristic)))
            self.names += 1
            expanded_det = sp.expand(characteristic)
            self.text.append((self.names, "This expression can be simplified to the following expression"))
            self.names += 1
            self.saved.append((self.names, sp.latex(expanded_det)))
            self.names += 1
            constant = expanded_det.as_coefficients_dict().get(1)
            self.text.append((self.names, "By the Cayley-Hamilton theorem"))
            self.names += 1
            self.saved.append((self.names, sp.latex(expanded_det)+"=O"))
            self.names += 1
            self.text.append((self.names, "Where M is the matrix, O is the empty matrix and the constant is multiplied by I"))
            self.names += 1
            rearrange1 = expanded_det - constant
            self.text.append((self.names, "If there is a constant, it must be taken to the other side, as follows"))
            self.names += 1
            self.saved.append((self.names, sp.latex(rearrange1)+"="+sp.latex(-constant)+"I"))
            self.names += 1
            rearrange2 = rearrange1/(-constant)
            self.text.append((self.names, "Then, the equation is divided by the constant, as follows"))
            self.names += 1
            self.saved.append((self.names, sp.latex(rearrange2)+"=I"))
            self.names += 1
            rearrange3 = rearrange2/M
            self.text.append((self.names, "Then, the equation is divided by the variable M, as follows"))
            self.names += 1
            self.saved.append((self.names, sp.latex(sp.expand(rearrange3))+"=M^{-1}"))
            self.names += 1
            inverse = rearrange3.subs(M, self.matrix)
            self.text.append((self.names, "Finally, the matrix is substituted into the variable M to calculate the inverse"))
            self.names += 1
            self.saved.append((self.names, "M^{-1}="+sp.latex(inverse)))
            self.names += 1
            return inverse

    def latex2img(self):
        for i in self.saved:
            text2image.formula_as_file(i[1], i[0])
        for i in self.text:
            text2image.toImage(i[1], i[0])

    def compare_latex2img(self, subfolder):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder)
        for i in self.text:
            compare_text2image.toImage(i[1], i[0], subfolder)

# class Strassen:
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self.size = matrix.rows
#         self.saved = []
#         self.text = []
#         self.names = 0

#     def check(self):
#         det = naiveDeterminant(self.matrix).calc()
#         if det == 0:
#             self.saved.append((self.names, sp.latex(self.matrix)))
#             self.names += 1
#             self.text.append((self.names, "No Inverse Exists"))
#             self.names += 1
#             return False, "No Inverse Exists (Determinant of the matrix is 0)"
#         else:
#             return True, "Inverse Exists!"

#     def calc(self):
#         final_rows = self.matrix.rows
#         final_cols = self.matrix.cols
#         if self.matrix.rows % 2 == 1:
#             self.matrix = self.matrix.col_join(sp.zeros(1, self.matrix.cols))
#         if self.matrix.cols % 2 == 1:
#             self.matrix = self.matrix.row_join(sp.zeros(self.matrix.rows, 1))
#         sp.pprint(self.matrix)

#         row_half = (self.matrix.rows) // 2
#         col_half = (self.matrix.cols) // 2

#         a11 = self.matrix[:row_half, :col_half] # top-left
#         a12 = self.matrix[:row_half, col_half:] # top-right
#         a21 = self.matrix[row_half:, :col_half] # bottom-left
#         a22 = self.matrix[row_half:, col_half:] # bottom-right

#         R1 = naiveInverse(a11).calc()
#         print("R1")
#         sp.pprint(R1)
#         R2 = a21 * R1
#         print("R2")
#         sp.pprint(R2)
#         R3 = R1 * a12
#         print("R3")
#         sp.pprint(R3)
#         R4 = a21 * R3
#         print("R4")
#         sp.pprint(R4)
#         R5 = R4 - a22
#         print("R5")
#         sp.pprint(R5)
#         R6 = naiveInverse(R5).calc()
#         print("R6")
#         sp.pprint(R6)
#         c12 = R3 * R6
#         c21 = R6 * R2
#         R7 = R3 * c21
#         c11 = R1 - R7
#         c22 = -R6

#         top_half = c11.row_join(c12)
#         bottom_half = c21.row_join(c22)
#         final_matrix = top_half.col_join(bottom_half)

#         if final_matrix.cols != final_cols:
#             final_matrix.col_del(final_matrix.cols - 1)
#         if final_matrix.rows != final_rows:
#             final_matrix.row_del(final_matrix.rows - 1)

#         return final_matrix

def getMethods():
    methods = []
    methods.append(("Standard", naiveInverse))
    methods.append(("Cayley", CayleyHamilton))
    return methods

# empty()
# a = sp.Matrix([[2,6,3,5],[3,5,6,4],[2,4,3,5],[3,5,7,4]])
# a = sp.Matrix([[2,6,3],[3,5,6],[2,4,3]])
# a = sp.Matrix([8])
# sp.pprint(a)
# inverse = CayleyHamilton(a)
# print(inverse.check())
# sp.pprint(inverse.calc())
# inverse.latex2img()

# a = sp.Matrix([[2,6,5],[3,14,1],[4,5,7]])
# a = sp.Matrix([])
# a = sp.Matrix([8])
# sp.pprint(a)
# inverse = naiveInverse(a)
# print(inverse.check())
# sp.pprint(inverse.calc())
# inverse.latex2img()