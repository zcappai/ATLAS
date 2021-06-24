import sympy as sp
from determinant import naiveDeterminant
# from latex2image import formula_as_file
from emptyimg import empty
from text2image import toImage, formula_as_file

class naiveInverse:
    def __init__(self, matrix, size):
        self.matrix = matrix
        self.size = size
        self.saved = []
        self.text = []

    def check(self):
        det = naiveDeterminant(self.matrix, self.size).calc()
        if det == 0:
            formula_as_file(sp.latex(self.matrix), 'images/0.png')
            toImage("No Inverse Exists", 1)
            return False, "No Inverse Exists (Determinant of the matrix is 0)"
        else:
            return True, "Inverse Exists!"

    def calc(self):
        curr = []
        names = 1
        self.text.append((names, "First, we find the minors of each element"))
        names += 1
        self.text.append((names, "The minor ignores the values on the current row & column..."))
        names += 1
        self.text.append((names, "...and calculates the determinant of the remaining values"))
        names += 1
        for i in range(self.size):
            for j in range(self.size):
                curr_submatrix = self.matrix.minor_submatrix(i, j)
                self.text.append((names, "The minor of "+sp.latex(self.matrix.row(i).col(j)[0])+" is"))
                names += 1
                self.saved.append((names, sp.latex(curr_submatrix[0])))
                names += 1
                curr.append(curr_submatrix)
        minors = []
        for i in curr:
            if self.size - 1 == 1:
                minors.append(i[0])
            else:
                det = naiveDeterminant(i, self.size - 1).calc()
                minors.append(det)
        matrix_minors = sp.Matrix(self.size, self.size, minors)
        self.text.append((names, "Therefore, the matrix of minors is"))
        names += 1
        self.saved.append((names, sp.latex(matrix_minors)))
        names += 1
        self.text.append((names, "To find the matrix of cofactors, we multiply alternative elements by -1..."))
        names += 1
        self.text.append((names, "...such that no 2 vertically or horizontally adjacent elements are multiplied by -1"))
        names += 1
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
        self.text.append((names, "Therefore, the matrix of cofactors is"))
        names += 1
        self.saved.append((names, sp.latex(matrix_cofactors)))
        names += 1
        self.text.append((names, "Next, to find the adjugate, we transpose the matrix of cofactors"))
        names += 1
        self.text.append((names, "Therefore, the adjugate is"))
        names += 1
        adjugate = matrix_cofactors.transpose()
        self.saved.append((names, sp.latex(adjugate)))
        names += 1
        self.text.append((names, "Then, we find the determinant of the original matrix"))
        names += 1
        self.saved.append((names, sp.latex(self.matrix)))
        names += 1
        self.text.append((names, "Giving a determinant of"))
        names += 1
        final_det = naiveDeterminant(self.matrix, self.size).calc()
        self.saved.append((names, sp.latex(final_det)))
        names += 1
        self.text.append((names, "Finally, we multiply 1/det by the adjugate as follows"))
        names += 1
        self.saved.append((names, "\\frac{"+sp.latex(1)+"}{"+sp.latex(final_det)+"}"+sp.latex(adjugate)+"="+sp.latex((1/final_det)*adjugate)))
        names += 1
        inverse = (1/final_det)*adjugate
        self.text.append((names, "Therefore, the inverse of the matrix is"))
        names += 1
        self.saved.append((names, sp.latex(inverse)))
        names += 1

    def latex2img(self):
        formula_as_file(sp.latex(self.matrix), 'images/0.png')
        for i in self.saved:
            formula_as_file(i[1], 'images/'+str(i[0])+'.png')
        for i in self.text:
            toImage(i[1], i[0])

# empty()
# a = sp.Matrix([[2,6,3,5],[3,5,6,4],[2,4,3,5],[3,5,7,4]])
# sp.pprint(a)
# inverse = naiveInverse(a, 4)
# print(inverse.check())
# sp.pprint(inverse.calc())
# inverse.latex2img()

# a = sp.Matrix([[2,6,5],[3,14,1],[4,5,7]])
# sp.pprint(a)
# inverse = naiveInverse(a, 3)
# print(inverse.check())
# sp.pprint(inverse.calc())