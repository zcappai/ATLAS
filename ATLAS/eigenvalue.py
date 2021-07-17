import sympy as sp
from determinant import naiveDeterminant
from text2image import toImage, formula_as_file
from emptyimg import empty


class Eigenvalue:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []
        self.text = []
    
    def calc(self):
        names = 1
        I = sp.eye(self.size)
        lamda = sp.Symbol('lamda')
        lamda_I = lamda*I
        new_matrix = self.matrix - lamda_I
        self.text.append((names, "First, subtract λ multiplied by the identity matrix from the matrix"))
        names += 1
        self.saved.append((names, sp.latex(self.matrix)+str('-')+sp.latex(lamda)+sp.latex(I)))
        names += 1
        self.text.append((names, "To form the following matrix"))
        names += 1
        self.saved.append((names, sp.latex(new_matrix)))
        names += 1
        self.text.append((names, "Then, calculate the determinant of this matrix and equate it to 0"))
        names += 1
        characteristic = naiveDeterminant(new_matrix).calc()
        self.text.append((names, "Giving the following equation"))
        names += 1
        self.saved.append((names, sp.latex(characteristic)+"=0"))
        names += 1
        self.text.append((names, "This equation can be simplified to the following equation"))
        names += 1
        expanded_det = sp.expand(characteristic)
        # print(expanded_det)
        self.saved.append((names, sp.latex(expanded_det)+"=0"))
        names += 1
        solved_lamda = sp.roots(expanded_det, lamda)
        # print(solved_lamda)
        eigenvalues = []
        self.text.append((names, "Finally, solve this equation to get the eigenvalues"))
        names += 1
        for i in solved_lamda.items():
            # solution = i.evalf(chop=True)
            solution = i[0]
            amount = i[1]
            while amount > 0:
                eigenvalues.append(solution)
                amount -= 1
                self.saved.append((names, sp.latex(lamda)+"="+sp.latex(solution)))
                names += 1
        return eigenvalues

    def latex2img(self):
        formula_as_file(sp.latex(self.matrix), 0)
        for i in  self.saved:
            formula_as_file(i[1], i[0])
        for i in self.text:
            toImage(i[1], i[0])

# class QR:
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self.cols = matrix.cols
#         self.saved = []
#         self.text = []

#     def calc(self):
#         if self.cols == 1:
#             return [self.matrix[0]]
#         U0 = sp.eye(self.cols)
#         checker = True
#         count = 0
#         while checker:
#             e = []
#             for i in range(self.cols):
#                 # sp.pprint(self.matrix)
#                 curr_col = self.matrix.col(i)
#                 modulus = 0
#                 for k in curr_col:
#                     modulus += k**2
#                 modulus = sp.sqrt(modulus)
#                 if i == 0:
#                     e.append((curr_col/modulus).evalf())
#                 else:
#                     new_col = curr_col
#                     for j in e:
#                         new_col -= curr_col.dot(j)*j
#                     modulus_new = 0
#                     for l in new_col:
#                         modulus_new += l**2
#                     modulus_new = sp.sqrt(modulus_new)
#                     e.append((new_col/modulus_new).evalf())

#             Q = sp.Matrix.hstack(*e)
#             R = sp.Matrix(self.cols, self.cols, [0]*self.cols*self.cols)

#             for i in range(self.cols):
#                 a_col = self.matrix.col(i)
#                 for j in range(i+1):
#                     q_col = Q.col(j)
#                     R[j, i] = a_col.dot(q_col)

#             new_x = R*Q
#             diff_check = []
#             # sp.pprint(new_x)
#             for i in range(self.cols):
#                 diff = self.matrix[i, i] - new_x[i, i]
#                 if diff < 1e-15:
#                     diff_check.append(True)
#                 else:
#                     diff_check.append(False)
#             if False not in diff_check:
#                 checker = False
#             self.matrix = new_x
#             U0 = U0*Q
#             count += 1

#         eigenvalues = []
#         for i in range(self.cols):
#             eigenvalues.append(self.matrix[i, i])
#         print(count)
#         return eigenvalues

# x = sp.Matrix([[1,1,1],[2,-3,4],[3,4,5]])
# x = sp.Matrix([[1,1,0],[1,0,1],[0,1,1]])
# x = sp.Matrix([[4/5, -3/5, 0],[3/5, 4/5, 0],[1, 2, 2]])
# sp.pprint(x)
# new = QR(x)
# sp.pprint(new.calc())
# new.latex2img()