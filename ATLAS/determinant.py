import sympy as sp
import text2image
import compare_text2image
from emptyimg import empty

class naiveDeterminant:
    names = 0
    saved = []
    text = []
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = self.matrix.rows
        self.det = 0
    
    # Calculates the determinant of a matrix
    def calc(self):
        curr = []
        naiveDeterminant.saved.append((naiveDeterminant.names, self.matrix))
        naiveDeterminant.names += 1
        if self.size == 0:
            naiveDeterminant.text.append((naiveDeterminant.names, "A matrix of size 0 has a determinant of 1"))
            naiveDeterminant.names += 1
            self.det = 1
            self.final_det = (naiveDeterminant.names, self.det)
            return self.det
        elif self.size == 1:
            naiveDeterminant.saved.append((naiveDeterminant.names, self.matrix))
            naiveDeterminant.names += 1
            naiveDeterminant.text.append((naiveDeterminant.names, "A matrix of size 1 has a determinant equal to its only value"))
            naiveDeterminant.names += 1
            self.det = self.matrix[0]
            self.final_det = (naiveDeterminant.names, self.det)
            return self.det
        else:
            naiveDeterminant.text.append((naiveDeterminant.names, "Take the first row of the matrix"))
            naiveDeterminant.names += 1
            naiveDeterminant.saved.append((naiveDeterminant.names, self.matrix[0,:]))
            naiveDeterminant.names += 1
            naiveDeterminant.text.append((naiveDeterminant.names, "Take the minors of each element respectively"))
            naiveDeterminant.names += 1
            for i in range(self.size):
                curr_element = self.matrix[i]
                curr_submatrix = self.matrix.minor_submatrix(0, i)
                curr.append((curr_element, curr_submatrix))
                naiveDeterminant.saved.append((naiveDeterminant.names, curr_submatrix))
                naiveDeterminant.names += 1
            naiveDeterminant.text.append((naiveDeterminant.names, "To form the following expression"))
            naiveDeterminant.names += 1
            naiveDeterminant.saved.append((naiveDeterminant.names, curr))
            naiveDeterminant.names += 1
            neg_toggle = 0
            for i in range(self.size):
                if neg_toggle % 2 == 0:
                    if self.size - 1 == 1:
                        # naiveDeterminant.text.append((naiveDeterminant.names, "Add "+str(curr[i][0])+str("x")+str(curr[i][1][0])+" to the determinant"))
                        # naiveDeterminant.names += 1
                        self.det += curr[i][0] * curr[i][1][0]
                    else:
                        sub_det = naiveDeterminant(curr[i][1]).calc()
                        naiveDeterminant.text.append((naiveDeterminant.names, "The determinant of the minor"))
                        naiveDeterminant.names += 1
                        naiveDeterminant.saved.append((naiveDeterminant.names, curr[i][1]))
                        naiveDeterminant.names += 1
                        naiveDeterminant.text.append((naiveDeterminant.names, "is"))
                        naiveDeterminant.names += 1
                        self.det += curr[i][0] * sub_det
                        naiveDeterminant.saved.append((naiveDeterminant.names, sub_det))
                        naiveDeterminant.names += 1
                elif neg_toggle % 2 == 1:
                    if self.size - 1 == 1:
                        # naiveDeterminant.text.append((naiveDeterminant.names, "Subtract "+str(curr[i][0])+str("x")+str(curr[i][1][0])+" from the determinant"))
                        # naiveDeterminant.names += 1
                        self.det -= curr[i][0] * curr[i][1][0]
                    else:
                        sub_det = naiveDeterminant(curr[i][1]).calc()
                        naiveDeterminant.text.append((naiveDeterminant.names, "The determinant of the minor"))
                        naiveDeterminant.names += 1
                        naiveDeterminant.saved.append((naiveDeterminant.names, curr[i][1]))
                        naiveDeterminant.names += 1
                        naiveDeterminant.text.append((naiveDeterminant.names, "is"))
                        naiveDeterminant.names += 1
                        self.det -= curr[i][0] * sub_det
                        naiveDeterminant.saved.append((naiveDeterminant.names, sub_det))
                        naiveDeterminant.names += 1
                neg_toggle += 1
            self.final_det = (naiveDeterminant.names, self.det)
            return self.det

    # Converts the matrices and expressions to images
    def latex2img(self):
        symb_toggle = 0
        for i in naiveDeterminant.saved:
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
        for i in naiveDeterminant.text:
            count = i[0]
            message = i[1]
            text2image.toImage(message, count)
        text2image.toImage("Therefore, the determinant of the matrix is", self.final_det[0])
        text2image.formula_as_file(str(self.final_det[1]), self.final_det[0]+1)

    # Converts the matrices and expressions to images
    def compare_latex2img(self, subfolder):
        symb_toggle = 0
        for i in naiveDeterminant.saved:
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
        for i in naiveDeterminant.text:
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
        self.names = 0
        self.det = 0
    
    def calc(self):
        size = self.matrix.rows
        if size != 3:
            self.text.append((self.names, "Sarrus' method cannot be used for {}x{} matrices".format(size, size)))
            self.names += 1
            return "N/A"
        else:
            self.saved.append((self.names, sp.latex(self.matrix)))
            self.names += 1
            self.text.append((self.names, "First, multiply values along the leading diagonal"))
            self.names += 1
            R1 = self.matrix[0, 0] * self.matrix[1, 1] * self.matrix[2, 2]
            self.saved.append((self.names, "R_1="+sp.latex(self.matrix[0, 0])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 2])+"={}".format(R1)))
            self.names += 1
            R2 = self.matrix[1, 0] * self.matrix[2, 1] * self.matrix[0, 2]
            self.text.append((self.names, "Then, multiply values along the first diagonal below the leading diagonal"))
            self.names += 1
            self.text.append((self.names, "By assuming an identical matrix is below the original..."))
            self.names += 1
            self.text.append((self.names, "...so that the final element of the multiplication is the top-right element"))
            self.names += 1
            self.saved.append((self.names, "R_2="+sp.latex(self.matrix[1, 0])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 2])+"={}".format(R2)))
            self.names += 1
            R3 = self.matrix[2, 0] * self.matrix[0, 1] * self.matrix[1, 2]
            self.text.append((self.names, "Then, multiply values along the second diagonal below the leading diagonal"))
            self.names += 1
            self.text.append((self.names, "By making the same assumption as the previous multiplication"))
            self.names += 1
            self.saved.append((self.names, "R_3="+sp.latex(self.matrix[2, 0])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 2])+"={}".format(R3)))
            self.names += 1
            R = R1 + R2 + R3
            self.text.append((self.names, "Now, add together the products"))
            self.names += 1
            self.saved.append((self.names, "R=R_1+R_2+R_3="+sp.latex(R1)+"+"+sp.latex(R2)+"+"+sp.latex(R3)+"={}".format(R)))
            self.names += 1

            self.text.append((self.names, "Now do the same for the leftward diagonals, starting with the leading leftward diagonal"))
            self.names += 1
            L1 = self.matrix[0, 2] * self.matrix[1, 1] * self.matrix[2, 0]
            self.saved.append((self.names, "L_1="+sp.latex(self.matrix[0, 2])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 0])+"={}".format(L1)))
            self.names += 1
            L2 = self.matrix[1, 2] * self.matrix[2, 1] * self.matrix[0, 0]
            self.text.append((self.names, "Then, multiply values along the first diagonal below the leading leftward diagonal"))
            self.names += 1
            self.saved.append((self.names, "L_2="+sp.latex(self.matrix[1, 2])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 0])+"={}".format(L2)))
            self.names += 1
            L3 = self.matrix[2, 2] * self.matrix[0, 1] * self.matrix[1, 0]
            self.text.append((self.names, "Then, multiply values along the second diagonal below the leading leftwrad diagonal"))
            self.names += 1
            self.saved.append((self.names, "L_3="+sp.latex(self.matrix[2, 2])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 0])+"={}".format(L3)))
            self.names += 1
            L = L1 + L2 + L3
            self.text.append((self.names, "Now, add together the products"))
            self.names += 1
            self.saved.append((self.names, "L=L_1+L_2+L_3="+sp.latex(L1)+"+"+sp.latex(L2)+"+"+sp.latex(L3)+"={}".format(L)))
            self.names += 1

            self.det = R - L
            self.text.append((self.names, "Finally, subtract the sum of the left diagonal multiplications from the right diagonal multiplications"))
            self.names += 1
            self.saved.append((self.names, "det=R-L="+sp.latex(R)+"-"+sp.latex(L)+"={}".format(self.det)))
            self.names += 1
            self.text.append((self.names, "Therefore, the determinant of the matrix is"))
            self.names += 1
            self.saved.append((self.names, sp.latex(self.det)))
            self.names += 1
            return self.det

    # Converts the matrices and expressions to images
    def latex2img(self):
        for i in self.saved:
            text2image.formula_as_file(i[1], i[0])
        for i in self.text:
            text2image.toImage(i[1], i[0])

    # Converts the matrices and expressions to images
    def compare_latex2img(self, subfolder):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder)
        for i in self.text:
            compare_text2image.toImage(i[1], i[0], subfolder)

class LU:
    def __init__(self, matrix):
        self.matrix = matrix
        self.saved = []
        self.text = []
        self.names = 0
        self.det = 0

    def calc(self):
        self.saved.append((self.names, sp.latex(self.matrix)))
        self.names += 1
        self.text.append((self.names, "First, create an empty matrix representing the lower triangular (L) matrix"))
        self.names += 1
        size = self.matrix.rows
        L = sp.Matrix(size, size, [0]*size*size)
        self.saved.append((self.names, sp.latex(L)))
        self.names += 1
        for i in range(size):
            for j in range(size):
                if i > j:
                    L[i, j] = sp.symbols('L_{}{}'.format(i+1,j+1))
                elif i == j:
                    L[i, j] = 1
        self.text.append((self.names, "Populate it with symbols in the bottom-left corner and 1's along the leading diagonal"))
        self.names += 1
        self.saved.append((self.names, sp.latex(L)))
        self.names += 1
        self.text.append((self.names, "Next, create an empty matrix representing the upper triangular (U) matrix"))
        self.names += 1
        U = sp.Matrix(size, size, [0]*size*size)
        self.saved.append((self.names, sp.latex(U)))
        self.names += 1
        for i in range(size):
            for j in range(size):
                if i == j or i < j:
                    U[i, j] = sp.symbols('U_{}{}'.format(i+1,j+1))
        self.text.append((self.names, "Populate it with symbols in the top-right corner and along the leading diagonal"))
        self.names += 1
        self.saved.append((self.names, sp.latex(U)))
        self.names += 1
        LU = L*U
        self.text.append((self.names, "Next, multiply the L and U matrices to form the resulant matrix"))
        self.names += 1
        self.saved.append((self.names, sp.latex(LU)))
        self.names += 1
        self.text.append((self.names, "This matrix is equivalent to the original problem matrix"))
        self.names += 1
        self.saved.append((self.names, sp.latex(LU)+"="+sp.latex(self.matrix)))
        self.names += 1
        self.text.append((self.names, "Now, by comparison of corresponding elements, deduce the L and U matrix values"))
        self.names += 1
        for i in range(size):
            for j in range(size):
                try:
                    self.text.append((self.names, "For element ({},{})".format(i, j)))
                    self.names += 1
                    curr_var = LU[i, j]
                    curr_num = self.matrix[i, j]
                    self.saved.append((self.names, sp.latex(curr_var)+"="+sp.latex(curr_num)))
                    self.names += 1
                    symb = list(curr_var.free_symbols)[0]
                    solution = sp.solve(curr_var-curr_num, symb)[0]
                    self.text.append((self.names, "This can be solved for"))
                    self.names += 1
                    self.saved.append((self.names, sp.latex(symb)))
                    self.names += 1
                    self.text.append((self.names, "giving a value of {}".format(solution)))
                    self.names += 1
                    if symb in U:
                        U = U.subs(symb, solution)
                        LU = LU.subs(symb, solution)
                        self.text.append((self.names, "This value is substituted back into U and LU to give"))
                        self.names += 1
                        self.saved.append((self.names, "U="+sp.latex(U)))
                        self.names += 1
                        self.saved.append((self.names, "LU="+sp.latex(LU)))
                        self.names += 1
                    elif symb in L:
                        L = L.subs(symb, solution)
                        LU = LU.subs(symb, solution)
                        self.text.append((self.names, "This value is substituted back into L and LU to give"))
                        self.names += 1
                        self.saved.append((self.names, "L="+sp.latex(L)))
                        self.names += 1
                        self.saved.append((self.names, "LU="+sp.latex(LU)))
                        self.names += 1
                except:
                    pass
        L_det = 1
        U_det = 1
        for i in range(size):
            L_det *= L[i, i]
            U_det *= U[i, i]
        self.text.append((self.names, "Now, multiply along the leading diagonal"))
        self.names += 1
        self.saved.append((self.names, "L="+sp.latex(L)+"\\rightarrow{}".format(L_det)))
        self.names += 1
        self.saved.append((self.names, "U="+sp.latex(U)+"\\rightarrow{}".format(U_det)))
        self.names += 1
        self.det = L_det * U_det
        self.text.append((self.names, "Therefore, the determinant is calculated from multiplying the 2 previous values"))
        self.names += 1
        self.saved.append((self.names, "det={}*{}={}".format(L_det, U_det, self.det)))
        self.names += 1
        self.text.append((self.names, "Therefore, the determinant of the matrix is"))
        self.names += 1
        self.saved.append((self.names, sp.latex(self.det)))
        self.names += 1
        return self.det

    # Converts the matrices and expressions to images
    def latex2img(self):
        for i in self.saved:
            text2image.formula_as_file(i[1], i[0])
        for i in self.text:
            text2image.toImage(i[1], i[0])

    # Converts the matrices and expressions to images
    def compare_latex2img(self, subfolder):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder)
        for i in self.text:
            compare_text2image.toImage(i[1], i[0], subfolder)

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
# det = LU(a)
# print(det.calc())
# det.latex2img()