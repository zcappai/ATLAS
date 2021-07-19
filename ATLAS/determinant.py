import sympy as sp
import text2image
import compare_text2image
from emptyimg import empty
import saver

class naiveDeterminant:
    # saver.names = 0
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = self.matrix.rows
        self.saved = []
        self.text = []
        self.det = 0
    
    # Calculates the determinant of a matrix
    def calc(self):
        # global saver.names
        curr = []
        self.saved.append((saver.names, self.matrix))
        saver.names += 1
        if self.size == 0:
            self.text.append((saver.names, "A matrix of size 0 has a determinant of 1"))
            saver.names += 1
            self.det = 1
            self.final_det = (saver.names, self.det)
            return self.det
        elif self.size == 1:
            self.saved.append((saver.names, self.matrix))
            saver.names += 1
            self.text.append((saver.names, "A matrix of size 1 has a determinant equal to its only value"))
            saver.names += 1
            self.det = self.matrix[0]
            self.final_det = (saver.names, self.det)
            return self.det
        else:
            self.text.append((saver.names, "Take the first row of the matrix"))
            saver.names += 1
            self.saved.append((saver.names, self.matrix[0,:]))
            saver.names += 1
            self.text.append((saver.names, "Take the minors of each element respectively"))
            saver.names += 1
            for i in range(self.size):
                curr_element = self.matrix[i]
                curr_submatrix = self.matrix.minor_submatrix(0, i)
                curr.append((curr_element, curr_submatrix))
                self.saved.append((saver.names, curr_submatrix))
                saver.names += 1
            self.text.append((saver.names, "To form the following expression"))
            saver.names += 1
            self.saved.append((saver.names, curr))
            saver.names += 1
            neg_toggle = 0
            for i in range(self.size):
                if neg_toggle % 2 == 0:
                    if self.size - 1 == 1:
                        # self.text.append((saver.names, "Add "+str(curr[i][0])+str("x")+str(curr[i][1][0])+" to the determinant"))
                        # saver.names += 1
                        self.det += curr[i][0] * curr[i][1][0]
                    else:
                        sub_det = naiveDeterminant(curr[i][1]).calc()
                        self.text.append((saver.names, "The determinant of the minor"))
                        saver.names += 1
                        self.saved.append((saver.names, curr[i][1]))
                        saver.names += 1
                        self.text.append((saver.names, "is"))
                        saver.names += 1
                        self.det += curr[i][0] * sub_det
                        self.saved.append((saver.names, sub_det))
                        saver.names += 1
                elif neg_toggle % 2 == 1:
                    if self.size - 1 == 1:
                        # self.text.append((saver.names, "Subtract "+str(curr[i][0])+str("x")+str(curr[i][1][0])+" from the determinant"))
                        # saver.names += 1
                        self.det -= curr[i][0] * curr[i][1][0]
                    else:
                        sub_det = naiveDeterminant(curr[i][1]).calc()
                        self.text.append((saver.names, "The determinant of the minor"))
                        saver.names += 1
                        self.saved.append((saver.names, curr[i][1]))
                        saver.names += 1
                        self.text.append((saver.names, "is"))
                        saver.names += 1
                        self.det -= curr[i][0] * sub_det
                        self.saved.append((saver.names, sub_det))
                        saver.names += 1
                neg_toggle += 1
            self.final_det = (saver.names, self.det)
            return self.det

    def addSaved(self, check):
        if check == True:
            saver.saved = saver.saved + self.saved
            saver.text = saver.text + self.text

    # Converts the matrices and expressions to images
    def latex2img(self):
        symb_toggle = 0
        for i in saver.saved:
            tex = ""
            expr = i[1]
            try:
                for j in expr:
                    for k in j:
                        tex += sp.latex(k)
                    if symb_toggle == 0:
                        tex += '-'
                        symb_toggle = 1
                    elif symb_toggle == 1:
                        tex += '+'
                        symb_toggle = 0
                symb_toggle = 0
                text2image.formula_as_file(tex[:-1], i[0])
            except:
                text2image.formula_as_file(sp.latex(i[1]), i[0])
        for i in saver.text:
            count = i[0]
            message = i[1]
            text2image.toImage(message, count)
        text2image.toImage("Therefore, the determinant of the matrix is", self.final_det[0])
        text2image.formula_as_file(str(self.final_det[1]), self.final_det[0]+1)

    # Converts the matrices and expressions to images
    def compare_latex2img(self, subfolder):
        symb_toggle = 0
        for i in saver.saved:
            tex = ""
            expr = i[1]
            try:
                for j in expr:
                    for k in j:
                        tex += sp.latex(k)
                    if symb_toggle == 0:
                        tex += '-'
                        symb_toggle = 1
                    elif symb_toggle == 1:
                        tex += '+'
                        symb_toggle = 0
                symb_toggle = 0
                compare_text2image.formula_as_file(tex[:-1], i[0], subfolder)
            except:
                compare_text2image.formula_as_file(sp.latex(i[1]), i[0], subfolder)
        for i in saver.text:
            count = i[0]
            message = i[1]
            compare_text2image.toImage(message, count, subfolder)
        compare_text2image.toImage("Therefore, the determinant of the matrix is", self.final_det[0], subfolder)
        compare_text2image.formula_as_file(str(self.final_det[1]), self.final_det[0]+1, subfolder)

class Sarrus:
    def __init__(self, matrix):
        self.matrix = matrix
        self.saved = []
        self.text = []
        # self.saver.names = 0
        self.det = 0
    
    def calc(self):
        # global saver.names
        size = self.matrix.rows
        # print(saver.saved)
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        if size != 3:
            self.text.append((saver.names, "Sarrus' method cannot be used for {}x{} matrices".format(size, size)))
            saver.names += 1
            return "N/A"
        else:
            self.text.append((saver.names, "First, multiply values along the leading diagonal"))
            saver.names += 1
            R1 = self.matrix[0, 0] * self.matrix[1, 1] * self.matrix[2, 2]
            self.saved.append((saver.names, "R_1="+sp.latex(self.matrix[0, 0])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 2])+"={}".format(R1)))
            saver.names += 1
            R2 = self.matrix[1, 0] * self.matrix[2, 1] * self.matrix[0, 2]
            self.text.append((saver.names, "Then, multiply values along the first diagonal below the leading diagonal"))
            saver.names += 1
            self.text.append((saver.names, "By assuming an identical matrix is below the original..."))
            saver.names += 1
            self.text.append((saver.names, "...so that the final element of the multiplication is the top-right element"))
            saver.names += 1
            self.saved.append((saver.names, "R_2="+sp.latex(self.matrix[1, 0])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 2])+"={}".format(R2)))
            saver.names += 1
            R3 = self.matrix[2, 0] * self.matrix[0, 1] * self.matrix[1, 2]
            self.text.append((saver.names, "Then, multiply values along the second diagonal below the leading diagonal"))
            saver.names += 1
            self.text.append((saver.names, "By making the same assumption as the previous multiplication"))
            saver.names += 1
            self.saved.append((saver.names, "R_3="+sp.latex(self.matrix[2, 0])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 2])+"={}".format(R3)))
            saver.names += 1
            R = R1 + R2 + R3
            self.text.append((saver.names, "Now, add together the products"))
            saver.names += 1
            self.saved.append((saver.names, "R=R_1+R_2+R_3="+sp.latex(R1)+"+"+sp.latex(R2)+"+"+sp.latex(R3)+"={}".format(R)))
            saver.names += 1

            self.text.append((saver.names, "Now do the same for the leftward diagonals, starting with the leading leftward diagonal"))
            saver.names += 1
            L1 = self.matrix[0, 2] * self.matrix[1, 1] * self.matrix[2, 0]
            self.saved.append((saver.names, "L_1="+sp.latex(self.matrix[0, 2])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 0])+"={}".format(L1)))
            saver.names += 1
            L2 = self.matrix[1, 2] * self.matrix[2, 1] * self.matrix[0, 0]
            self.text.append((saver.names, "Then, multiply values along the first diagonal below the leading leftward diagonal"))
            saver.names += 1
            self.saved.append((saver.names, "L_2="+sp.latex(self.matrix[1, 2])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 0])+"={}".format(L2)))
            saver.names += 1
            L3 = self.matrix[2, 2] * self.matrix[0, 1] * self.matrix[1, 0]
            self.text.append((saver.names, "Then, multiply values along the second diagonal below the leading leftwrad diagonal"))
            saver.names += 1
            self.saved.append((saver.names, "L_3="+sp.latex(self.matrix[2, 2])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 0])+"={}".format(L3)))
            saver.names += 1
            L = L1 + L2 + L3
            self.text.append((saver.names, "Now, add together the products"))
            saver.names += 1
            self.saved.append((saver.names, "L=L_1+L_2+L_3="+sp.latex(L1)+"+"+sp.latex(L2)+"+"+sp.latex(L3)+"={}".format(L)))
            saver.names += 1

            self.det = R - L
            self.text.append((saver.names, "Finally, subtract the sum of the left diagonal multiplications from the right diagonal multiplications"))
            saver.names += 1
            self.saved.append((saver.names, "det=R-L="+sp.latex(R)+"-"+sp.latex(L)+"={}".format(self.det)))
            saver.names += 1
            self.text.append((saver.names, "Therefore, the determinant of the matrix is"))
            saver.names += 1
            self.saved.append((saver.names, sp.latex(self.det)))
            saver.names += 1
            return self.det

    def addSaved(self, check):
        if check == True:
            saver.saved = saver.saved + self.saved
            saver.text = saver.text + self.text

    # Converts the matrices and expressions to images
    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
        for i in saver.text:
            text2image.toImage(i[1], i[0])

    # Converts the matrices and expressions to images
    def compare_latex2img(self, subfolder):
        for i in saver.saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder)
        for i in saver.text:
            compare_text2image.toImage(i[1], i[0], subfolder)

class LU:
    def __init__(self, matrix):
        self.matrix = matrix
        self.saved = []
        self.text = []
        # saver. names = 0
        self.det = 0

    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        self.text.append((saver.names, "First, create an empty matrix representing the lower triangular (L) matrix"))
        saver.names += 1
        size = self.matrix.rows
        L = sp.Matrix(size, size, [0]*size*size)
        self.saved.append((saver.names, sp.latex(L)))
        saver.names += 1
        for i in range(size):
            for j in range(size):
                if i > j:
                    L[i, j] = sp.symbols('L_{}{}'.format(i+1,j+1))
                elif i == j:
                    L[i, j] = 1
        self.text.append((saver.names, "Populate it with symbols in the bottom-left corner and 1's along the leading diagonal"))
        saver.names += 1
        self.saved.append((saver.names, sp.latex(L)))
        saver.names += 1
        self.text.append((saver.names, "Next, create an empty matrix representing the upper triangular (U) matrix"))
        saver.names += 1
        U = sp.Matrix(size, size, [0]*size*size)
        self.saved.append((saver.names, sp.latex(U)))
        saver.names += 1
        for i in range(size):
            for j in range(size):
                if i == j or i < j:
                    U[i, j] = sp.symbols('U_{}{}'.format(i+1,j+1))
        self.text.append((saver.names, "Populate it with symbols in the top-right corner and along the leading diagonal"))
        saver.names += 1
        self.saved.append((saver.names, sp.latex(U)))
        saver.names += 1
        LU = L*U
        self.text.append((saver.names, "Next, multiply the L and U matrices to form the resulant matrix"))
        saver.names += 1
        self.saved.append((saver.names, sp.latex(LU)))
        saver.names += 1
        self.text.append((saver.names, "This matrix is equivalent to the original problem matrix"))
        saver.names += 1
        self.saved.append((saver.names, sp.latex(LU)+"="+sp.latex(self.matrix)))
        saver.names += 1
        self.text.append((saver.names, "Now, by comparison of corresponding elements, deduce the L and U matrix values"))
        saver.names += 1
        for i in range(size):
            for j in range(size):
                try:
                    self.text.append((saver.names, "For element ({},{})".format(i, j)))
                    saver.names += 1
                    curr_var = LU[i, j]
                    curr_num = self.matrix[i, j]
                    self.saved.append((saver.names, sp.latex(curr_var)+"="+sp.latex(curr_num)))
                    saver.names += 1
                    symb = list(curr_var.free_symbols)[0]
                    solution = sp.solve(curr_var-curr_num, symb)[0]
                    self.text.append((saver.names, "This can be solved for"))
                    saver.names += 1
                    self.saved.append((saver.names, sp.latex(symb)))
                    saver.names += 1
                    self.text.append((saver.names, "giving a value of {}".format(solution)))
                    saver.names += 1
                    if symb in U:
                        U = U.subs(symb, solution)
                        LU = LU.subs(symb, solution)
                        self.text.append((saver.names, "This value is substituted back into U and LU to give"))
                        saver.names += 1
                        self.saved.append((saver.names, "U="+sp.latex(U)))
                        saver.names += 1
                        self.saved.append((saver.names, "LU="+sp.latex(LU)))
                        saver.names += 1
                    elif symb in L:
                        L = L.subs(symb, solution)
                        LU = LU.subs(symb, solution)
                        self.text.append((saver.names, "This value is substituted back into L and LU to give"))
                        saver.names += 1
                        self.saved.append((saver.names, "L="+sp.latex(L)))
                        saver.names += 1
                        self.saved.append((saver.names, "LU="+sp.latex(LU)))
                        saver.names += 1
                except:
                    pass
        L_det = 1
        U_det = 1
        for i in range(size):
            L_det *= L[i, i]
            U_det *= U[i, i]
        self.text.append((saver.names, "Now, multiply along the leading diagonal"))
        saver.names += 1
        self.saved.append((saver.names, "L="+sp.latex(L)+"\\rightarrow{}".format(L_det)))
        saver.names += 1
        self.saved.append((saver.names, "U="+sp.latex(U)+"\\rightarrow{}".format(U_det)))
        saver.names += 1
        self.det = L_det * U_det
        self.text.append((saver.names, "Therefore, the determinant is calculated from multiplying the 2 previous values"))
        saver.names += 1
        self.saved.append((saver.names, "det={}*{}={}".format(L_det, U_det, self.det)))
        saver.names += 1
        self.text.append((saver.names, "Therefore, the determinant of the matrix is"))
        saver.names += 1
        self.saved.append((saver.names, sp.latex(self.det)))
        saver.names += 1
        return self.det

    def addSaved(self, check):
        if check == True:
            saver.saved = saver.saved + self.saved
            saver.text = saver.text + self.text

    # Converts the matrices and expressions to images
    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
        for i in saver.text:
            text2image.toImage(i[1], i[0])

    # Converts the matrices and expressions to images
    def compare_latex2img(self, subfolder):
        for i in saver.saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder)
        for i in saver.text:
            compare_text2image.toImage(i[1], i[0], subfolder)

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
# det = QR(a)
# print(det.calc())
# det.latex2img()