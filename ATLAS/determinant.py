import sympy as sp
import text2image
import compare_text2image
from emptyimg import empty
import saver

class naiveDeterminant:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = self.matrix.rows
        self.saved = []
        # self.text = []
        self.det = 0
    
    # Calculates the determinant of a matrix
    def calc(self):
        curr = []
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        if self.size == 0:
            self.saved.append((saver.names, "\\text{A matrix of size 0 has}$$$$\\text{a determinant of 1}"))
            saver.names += 1
            self.det = 1
            self.final_det = (saver.names, self.det)
            return self.det
        elif self.size == 1:
            self.saved.append((saver.names, "\\text{A matrix of size 1 has a}$$$$\\text{determinant equal to its only value}"))
            saver.names += 1
            self.det = self.matrix[0]
            self.final_det = (saver.names, self.det)
            return self.det
        else:
            self.saved.append((saver.names, "\\text{Take the first row of the matrix}$$$$"+sp.latex(self.matrix[0,:])))
            saver.names += 1
            self.saved.append((saver.names, "\\text{Take the minors of each element respectively}"))
            saver.names += 1
            for i in range(self.size):
                curr_element = self.matrix[i]
                curr_submatrix = self.matrix.minor_submatrix(0, i)
                curr.append((curr_element, curr_submatrix))
                self.saved.append((saver.names, "\\text{The submatrix of the element}$$$$a_{1"+str(i+1)+"}="+sp.latex(curr_element)+"\\text{ is }"+sp.latex(curr_submatrix)))
                saver.names += 1
            symb_toggle = 0
            minor_expr = ""
            for j in curr:
                minor_expr += sp.latex(j[0])+sp.latex(j[1])
                if symb_toggle == 0:
                    minor_expr += '-'
                    symb_toggle = 1
                elif symb_toggle == 1:
                    minor_expr += '+'
                    symb_toggle = 0
                # symb_toggle = 0
            minor_expr = minor_expr[:-1]
            self.saved.append((saver.names, "\\text{This forms the following expression}$$$$"+minor_expr))
            saver.names += 1
            neg_toggle = 0
            self.final_equation = ""
            for i in range(self.size):
                if neg_toggle % 2 == 0:
                    if self.size - 1 == 1:
                        self.det += curr[i][0] * curr[i][1][0]
                        self.final_equation += "+"+sp.latex(curr[i][0])+"*"+sp.latex(curr[i][1][0])
                    else:
                        self.saved.append((saver.names, "\\text{Take the determinant of the matrix}"))
                        saver.names += 1
                        sub = naiveDeterminant(curr[i][1])
                        sub_det = sub.calc()
                        sub.addSaved(True)
                        self.final_equation += "+"+sp.latex(curr[i][0])+"*"+sp.latex(sub_det)
                        self.det += curr[i][0] * sub_det
                        self.saved.append((saver.names, "\\text{The determinant of the minor}$$$$"+sp.latex(curr[i][1])+"\\text{ is }"+sp.latex(sub_det)))
                        saver.names += 1
                elif neg_toggle % 2 == 1:
                    if self.size - 1 == 1:
                        self.det -= curr[i][0] * curr[i][1][0]
                        self.final_equation += "+"+sp.latex(curr[i][0])+"*"+sp.latex(curr[i][1][0])
                    else:
                        self.saved.append((saver.names, "\\text{Take the determinant of the matrix}"))
                        saver.names += 1
                        sub = naiveDeterminant(curr[i][1])
                        sub_det = sub.calc()
                        sub.addSaved(True)
                        self.final_equation += "-"+sp.latex(curr[i][0])+"*"+sp.latex(sub_det)
                        self.det -= curr[i][0] * sub_det
                        self.saved.append((saver.names, "\\text{The determinant of the minor}$$$$"+sp.latex(curr[i][1])+"\\text{ is }"+sp.latex(sub_det)))
                        saver.names += 1
                neg_toggle += 1
            self.final_det = self.det
            self.saved.append((saver.names, "\\text{The expression becomes}$$$$"+sp.latex(self.final_equation[1:])+"$$$$\\text{giving a value of }"+sp.latex(self.final_det)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{Therefore, the determinant}$$$$\\text{of the matrix is }"+sp.latex(self.final_det)))
            saver.names += 1
            return self.det

    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved
            # saver.text += self.text

    # Converts the matrices and expressions to images
    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
            # tex = ""
            # expr = i[1]
            # try:
            #     for j in expr:
            #         for k in j:
            #             tex += sp.latex(k)
            #         if symb_toggle == 0:
            #             tex += '-'
            #             symb_toggle = 1
            #         elif symb_toggle == 1:
            #             tex += '+'
            #             symb_toggle = 0
            #     symb_toggle = 0
            #     text2image.formula_as_file(tex[:-1], i[0])
            # except:
            #     text2image.formula_as_file(sp.latex(i[1]), i[0])
        # for i in saver.text:
        #     count = i[0]
        #     message = i[1]
        #     text2image.toImage(message, count)
        # text2image.formula_as_file("\\text{Therefore, the determinant}$$$$\\text{of the matrix is }"+sp.latex(self.final_det), saver.names)
        # saver.names += 1

    # Converts the matrices and expressions to images for method comparison
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Standard")
            # tex = ""
            # expr = i[1]
            # try:
            #     for j in expr:
            #         for k in j:
            #             tex += sp.latex(k)
            #         if symb_toggle == 0:
            #             tex += '-'
            #             symb_toggle = 1
            #         elif symb_toggle == 1:
            #             tex += '+'
            #             symb_toggle = 0
            #     symb_toggle = 0
            #     compare_text2image.formula_as_file(tex[:-1], i[0], "Standard")
            # except:
            #     compare_text2image.formula_as_file(sp.latex(i[1]), i[0], "Standard")
        # for i in saver.text:
        #     count = i[0]
        #     message = i[1]
        #     compare_text2image.toImage(message, count, "Standard")
        # compare_text2image.formula_as_file("\\text{Therefore, the determinant}$$$$\\text{of the matrix is }"+sp.latex(self.final_det), saver.names, "Standard")
        # saver.names += 1

class Sarrus:
    def __init__(self, matrix):
        self.matrix = matrix
        self.saved = []
        # self.text = []
        self.det = 0
    
    def calc(self):
        size = self.matrix.rows
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        if size != 3:
            self.saved.append((saver.names, "\\text{Sarrus' method cannot be used}$$$$\\text{for "+sp.latex(size)+"x"+sp.latex(size)+" matrices}"))
            saver.names += 1
            return "N/A"
        else:
            R1 = self.matrix[0, 0] * self.matrix[1, 1] * self.matrix[2, 2]
            self.saved.append((saver.names, "\\text{First, multiply the values along the leading diagonal}$$$$"
            +"R_1="+sp.latex(self.matrix[0, 0])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 2])+"={}".format(R1)))
            saver.names += 1
            R2 = self.matrix[1, 0] * self.matrix[2, 1] * self.matrix[0, 2]
            self.saved.append((saver.names, """\\text{Then, multiply the values along the first}$$$$\\text{subdiagonal by assuming an identical matrix}
            $$$$\\text{is directly below the original matrix so that}$$$$\\text{the final element of the multiplication is the}$$$$\\text{element at } a_{13}$$$$"""
            +"R_2="+sp.latex(self.matrix[1, 0])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 2])+"={}".format(R2)))
            saver.names += 1
            R3 = self.matrix[2, 0] * self.matrix[0, 1] * self.matrix[1, 2]
            self.saved.append((saver.names, """\\text{Then, multiply the values along the second}$$$$\\text{subdiagonal by making the same assumption}
            $$$$\\text{as the previous multiplication, so the final}$$$$\\text{2 elements are at } a_{12} \\text{ and } a_{23}$$$$"""
            +"R_3="+sp.latex(self.matrix[2, 0])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 2])+"={}".format(R3)))
            saver.names += 1
            R = R1 + R2 + R3
            self.saved.append((saver.names, "\\text{Now, add together the products}$$$$"
            +"R=R_1+R_2+R_3="+sp.latex(R1)+"+"+sp.latex(R2)+"+"+sp.latex(R3)+"={}".format(R)))
            saver.names += 1

            L1 = self.matrix[0, 2] * self.matrix[1, 1] * self.matrix[2, 0]
            self.saved.append((saver.names, "\\text{Now do the same for the anti-diagonals,}$$$$\\text{starting with the leading anti-diagonal.}$$$$"
            +"\\text{It is important to remember that the anti-diagonal}$$$$\\text{is the leading diagonal going from right to left.}$$$$"
            +"L_1="+sp.latex(self.matrix[0, 2])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 0])+"={}".format(L1)))
            saver.names += 1
            L2 = self.matrix[1, 2] * self.matrix[2, 1] * self.matrix[0, 0]
            self.saved.append((saver.names, "\\text{Then, multiply the values along the anti-subdiagonal}$$$$"
            +"L_2="+sp.latex(self.matrix[1, 2])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 0])+"={}".format(L2)))
            saver.names += 1
            L3 = self.matrix[2, 2] * self.matrix[0, 1] * self.matrix[1, 0]
            self.saved.append((saver.names, "\\text{Then, multiply the values along the second anti-subdiagonal}$$$$"
            +"L_3="+sp.latex(self.matrix[2, 2])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 0])+"={}".format(L3)))
            saver.names += 1
            L = L1 + L2 + L3
            self.saved.append((saver.names, "\\text{Now, add together the products}$$$$"
            +"L=L_1+L_2+L_3="+sp.latex(L1)+"+"+sp.latex(L2)+"+"+sp.latex(L3)+"={}".format(L)))
            saver.names += 1

            self.det = R - L
            self.saved.append((saver.names, "\\text{Finally, subtract the sum of the anti-diagonal}$$$$\\text{multiplications from the diagonal multiplications.}$$$$"
            +"det=R-L="+sp.latex(R)+"-"+sp.latex(L)+"={}".format(self.det)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{Therefore, the determinant is }"+sp.latex(self.det)))
            saver.names += 1
            return self.det

    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved
            # saver.text = saver.text + self.text

    # Converts the matrices and expressions to images
    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
        # for i in saver.text:
        #     text2image.toImage(i[1], i[0])

    # Converts the matrices and expressions to images
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Sarrus")
        # for i in saver.text:
        #     compare_text2image.toImage(i[1], i[0], "Sarrus")

class LU:
    def __init__(self, matrix):
        self.matrix = matrix
        self.saved = []
        # self.text = []
        self.det = 0

    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        size = self.matrix.rows
        L = sp.Matrix(size, size, [0]*size*size)
        self.saved.append((saver.names, "\\text{First, create an empty matrix representing}$$$$\\text{the lower triangular (L) matrix}$$$$"+sp.latex(L)))
        saver.names += 1
        for i in range(size):
            for j in range(size):
                if i > j:
                    L[i, j] = sp.symbols('L_{}{}'.format(i+1,j+1))
                elif i == j:
                    L[i, j] = 1
        self.saved.append((saver.names, """\\text{Populate the lower triangular matrix}$$$$\\text{with symbols in the bottom-left corner}"
        +"$$$$\\text{and 1's along the leading diagonal}$$$$"""+sp.latex(L)))
        saver.names += 1
        U = sp.Matrix(size, size, [0]*size*size)
        self.saved.append((saver.names, "\\text{Next, create an empty matrix representing}$$$$\\text{the upper triangular (U) matrix}$$$$"+sp.latex(U)))
        saver.names += 1
        for i in range(size):
            for j in range(size):
                if i == j or i < j:
                    U[i, j] = sp.symbols('U_{}{}'.format(i+1,j+1))
        self.saved.append((saver.names, """\\text{Populate the upper triangular matrix with symbols in the}$$$$
        \\text{top-right corner and along the leading diagonal}$$$$"""+sp.latex(U)))
        saver.names += 1
        LU = L*U
        self.saved.append((saver.names, "\\text{Next, multiply the L and U matrices}$$$$\\text{to form the resultant matrix}$$$$"
        +sp.latex(LU)+", $$$$\\text{which is equivalent to the original matrix}"))
        saver.names += 1
        self.saved.append((saver.names, sp.latex(LU)+"="+sp.latex(self.matrix)))
        saver.names += 1
        self.saved.append((saver.names, "\\text{By comparison of corresponding elements,}$$$$\\text{deduce the L and U matrix elements}"))
        saver.names += 1
        for i in range(size):
            for j in range(size):
                try:
                    curr_var = LU[i, j]
                    curr_num = self.matrix[i, j]
                    self.saved.append((saver.names, "\\text{For element } a_{"+str(i+1)+str(j+1)+"} \\text{ in LU,}$$$$"+sp.latex(curr_var)+"="+sp.latex(curr_num)))
                    saver.names += 1
                    symb = list(curr_var.free_symbols)[0]
                    solution = sp.solve(curr_var-curr_num, symb)[0]
                    self.saved.append((saver.names, "\\text{This can be solved for }"+sp.latex(symb)+"$$$$\\text{ giving a value of }"+sp.latex(solution)))
                    saver.names += 1
                    if symb in U:
                        U = U.subs(symb, solution)
                        LU = LU.subs(symb, solution)
                        self.saved.append((saver.names, "\\text{This value is substituted back into U and LU to give}$$$$U="+sp.latex(U)+", LU="+sp.latex(LU)))
                        saver.names += 1
                    elif symb in L:
                        L = L.subs(symb, solution)
                        LU = LU.subs(symb, solution)
                        self.saved.append((saver.names, "\\text{This value is substituted back into L and LU to give}$$$$L="+sp.latex(L)+", LU="+sp.latex(LU)))
                        saver.names += 1
                except:
                    pass
        L_det = 1
        U_det = 1
        for i in range(size):
            L_det *= L[i, i]
            U_det *= U[i, i]
        self.saved.append((saver.names, "\\text{Now, multiply along the leading diagonal}"))
        saver.names += 1
        self.saved.append((saver.names, "L="+sp.latex(L)+"\\rightarrow{}".format(L_det)+"$$$$U="+sp.latex(U)+"\\rightarrow{}".format(U_det)))
        saver.names += 1
        self.det = L_det * U_det
        self.saved.append((saver.names, """\\text{The determinant of the matrix is calculated}$$$$
        \\text{from multiplying the 2 previous values}$$$$
        \\text{det}={"""+sp.latex(L_det)+"}*{"+sp.latex(U_det)+"}={"+sp.latex(self.det)+"}"))
        saver.names += 1
        self.saved.append((saver.names, "\\text{Therefore, the determinant is }"+sp.latex(self.det)))
        saver.names += 1
        return self.det

    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved
            # saver.text = saver.text + self.text

    # Converts the matrices and expressions to images
    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
        # for i in saver.text:
        #     text2image.toImage(i[1], i[0])

    # Converts the matrices and expressions to images
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], "LU")
        # for i in saver.text:
        #     compare_text2image.toImage(i[1], i[0], "LU")

def getMethods():
    methods = []
    methods.append(("Standard", naiveDeterminant))
    methods.append(("Sarrus", Sarrus))
    methods.append(("LU", LU))
    return methods

# empty()
# a = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])
# a = sp.Matrix([[3,4,7],[6,5,1],[9,4,7]])
# a = sp.Matrix([[2,6,3,5],[3,5,6,4],[2,4,3,5],[3,5,7,4]])
# a = sp.Matrix([[0,0,0],[0,0,0],[0,0,0]])
# det = naiveDeterminant(a)
# print(det.calc())
# det.addSaved(True)
# det.latex2img()

# class QR:
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self.saved = []
#         self.text = []
#         # saver. names = 0
#         self.det = 1

#     def calc(self):
#         cols = self.matrix.cols
#         U0 = sp.eye(cols)
#         e = []
#         for i in range(cols):
#             curr_col = self.matrix.col(i)
#             modulus = 0
#             for k in curr_col:
#                 modulus += k**2
#             modulus = sp.sqrt(modulus)
#             if i == 0:
#                 e.append((curr_col/modulus).evalf())
#             else:
#                 new_col = curr_col
#                 for j in e:
#                     new_col -= curr_col.dot(j)*j
#                 modulus_new = 0
#                 for l in new_col:
#                     modulus_new += l**2
#                 modulus_new = sp.sqrt(modulus_new)
#                 e.append((new_col/modulus_new).evalf())

#         Q = sp.Matrix.hstack(*e)
#         R = sp.Matrix(cols, cols, [0]*cols*cols)

#         for i in range(cols):
#             a_col = self.matrix.col(i)
#             for j in range(i+1):
#                 q_col = Q.col(j)
#                 R[j, i] = a_col.dot(q_col)
#         sp.pprint(Q)
#         sp.pprint(R)
#         for i in range(cols):
#             self.det *= R[i, i]
        
#         return self.det