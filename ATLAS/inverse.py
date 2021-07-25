import sympy as sp
from determinant import naiveDeterminant
from emptyimg import empty
import text2image
import compare_text2image
import saver

class naiveInverse:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows

    def check(self):
        det = naiveDeterminant(self.matrix).calc()
        if det == 0:
            saver.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1
            saver.saved.append((saver.names, "\\text{No Inverse Exists}"))
            saver.names += 1
            return False, "No Inverse Exists (Determinant of the matrix is 0)"
        else:
            return True, "Inverse Exists!"

    def calc(self):
        curr = []
        saver.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        if self.size == 1:
            only_value = self.matrix[0]
            inverse = sp.Matrix([1/only_value])
            saver.saved.append((saver.names, "\\text{Since the matrix has only 1 values,}$$$$\\text{the reciprocal is taken, giving an inverse of}$$$$"+sp.latex(sp.Matrix([1/only_value]))))
            saver.names += 1
            return inverse
        saver.saved.append((saver.names, "\\text{First, we find the minors of each element.}$$$$\\text{The minor of an element ignores the values}"
        +"$$$$\\text{of the current row & column and calculates}$$$$\\text{the determinant of the remaining values.}"))
        saver.names += 1
        minors = []
        for i in range(self.size):
            for j in range(self.size):
                curr_submatrix = self.matrix.minor_submatrix(i, j)
                det = naiveDeterminant(curr_submatrix).calc()
                minors.append(det)
                saver.saved.append((saver.names, "\\text{The element }a_{"+str(i+1)+str(j+1)+"}="+sp.latex(self.matrix.row(i).col(j)[0])
                +"$$$$\\text{ gives the matrix}"+sp.latex(curr_submatrix)+"$$$$\\text{with a determinant of }"+sp.latex(det)))
                saver.names += 1
                curr.append(curr_submatrix)
        matrix_minors = sp.Matrix(self.size, self.size, minors)
        saver.saved.append((saver.names, "\\text{Therefore, the matrix of minors is}$$$$"+sp.latex(matrix_minors)))
        saver.names += 1
        saver.saved.append((saver.names, "\\text{To find the matrix of cofactors, we multiply}$$$$\\text{alternative elements by -1, such that no 2}"
        +"$$$$\\text{vertically or horizontally adjacent elements are}$$$$\\text{multiplied by -1.}"))
        saver.names += 1
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
        saver.saved.append((saver.names, "\\text{Therefore, the matrix of cofactors is}$$$$"+sp.latex(matrix_cofactors)))
        saver.names += 1
        saver.saved.append((saver.names, "\\text{Next, to find the adjugate, we transpose}$$$$\\text{the matrix of cofactors}"))
        saver.names += 1
        adjugate = matrix_cofactors.transpose()
        saver.saved.append((saver.names, "\\text{Therefore, the adjugate is}$$$$"+sp.latex(adjugate)))
        saver.names += 1
        final_det = naiveDeterminant(self.matrix).calc()
        saver.saved.append((saver.names, "\\text{Then, we find the determinant of the original matrix}$$$$"+sp.latex(self.matrix)+"$$$$\\text{giving a determinant of }"+sp.latex(final_det)))
        saver.names += 1
        saver.saved.append((saver.names, "\\text{Finally, we multiply }\\frac{1}{det}\\text{ by the adjugate}$$$$\\frac{"
        +sp.latex(1)+"}{"+sp.latex(final_det)+"}"+sp.latex(adjugate)+"="+sp.latex((1/final_det)*adjugate)))
        saver.names += 1
        inverse = (1/final_det)*adjugate
        saver.saved.append((saver.names, "\\text{Therefore, the inverse of the matrix is}$$$$"+sp.latex(inverse)))
        saver.names += 1
        return inverse

    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
        # for i in saver.text:
        #     text2image.toImage(i[1], i[0])

    def compare_latex2img(self):
        for i in saver.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Standard")
        # for i in saver.text:
        #     compare_text2image.toImage(i[1], i[0], "Standard")

class CayleyHamilton:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows

    def check(self):
        det = naiveDeterminant(self.matrix).calc()
        if det == 0:
            saver.saved.append((saver.names, sp.latex(self.matrix)))
            saver.names += 1
            saver.saved.append((saver.names, "\\text{No Inverse Exists}"))
            saver.names += 1
            return False, "No Inverse Exists (Determinant of the matrix is 0)"
        else:
            return True, "Inverse Exists!"

    def calc(self):
        saver.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        if self.size == 0:
            return sp.Matrix([])
        elif self.size == 1:
            only_value = self.matrix[0]
            inverse = sp.Matrix([1/only_value])
            saver.saved.append((saver.names, "\\text{Since the matrix has only 1 values,}$$$$\\text{the reciprocal is taken, giving an inverse of}$$$$"+sp.latex(sp.Matrix([1/only_value]))))
            saver.names += 1
            return inverse
        else:
            I = sp.eye(self.size)
            M = sp.Symbol('M')
            M_I = M*I
            new_matrix = self.matrix - M_I
            saver.saved.append((saver.names, "\\text{First, subtract M multiplied by the}$$$$\\text{identity matrix from the matrix}$$$$"+sp.latex(self.matrix)+str('-')+sp.latex(M)+sp.latex(I)))
            saver.names += 1
            saver.saved.append((saver.names, "\\text{To form the following matrix}$$$$"+sp.latex(new_matrix)))
            saver.names += 1
            characteristic = naiveDeterminant(new_matrix).calc()
            expanded_det = sp.expand(characteristic)
            saver.saved.append((saver.names, """\\text{Then, calculate the determinant of the}$$$$\\text{matrix giving the following expression}
            $$$$"""+sp.latex(expanded_det)))
            saver.names += 1
            constant = expanded_det.as_coefficients_dict().get(1)
            saver.saved.append((saver.names, "\\text{By the Cayley-Hamilton theorem}$$$$"+sp.latex(expanded_det)+"=O"))
            saver.names += 1
            saver.saved.append((saver.names, "\\text{Where }M\\text{ is the matrix, }$$$$O\\text{ is the empty matrix}$$$$\\text{and the constant is multiplied by }I"))
            saver.names += 1
            rearrange1 = expanded_det - constant
            saver.saved.append((saver.names, "\\text{If there is a constant, it must}$$$$\\text{be taken to the other side}$$$$"+sp.latex(rearrange1)+"="+sp.latex(-constant)+"I"))
            saver.names += 1
            rearrange2 = rearrange1/(-constant)
            saver.saved.append((saver.names, "\\text{Then, the equation is divided by the constant}$$$$"+sp.latex(rearrange2)+"=I"))
            saver.names += 1
            rearrange3 = rearrange2/M
            saver.saved.append((saver.names, "\\text{Then, the equation is divided by the variable }M$$$$"+sp.latex(sp.expand(rearrange3))+"=M^{-1}"))
            saver.names += 1
            inverse = rearrange3.subs(M, self.matrix)
            saver.saved.append((saver.names, "\\text{Finally, the matrix is substituted into the}$$$$\\text{variable }M\\text{ to calculate the inverse}"))
            saver.names += 1
            saver.saved.append((saver.names, "M^{-1}="+sp.latex(inverse)))
            saver.names += 1
            return inverse

    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
        # for i in saver.text:
        #     text2image.toImage(i[1], i[0])

    def compare_latex2img(self):
        for i in saver.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Cayley")
        # for i in saver.text:
        #     compare_text2image.toImage(i[1], i[0], "Cayley")

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