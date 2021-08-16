import sympy as sp
import text2image
import compare_text2image
import saver
from single_image import single_view

# Laplace Expansion
class naiveDeterminant:
    saved = []
    # Constructor takes square matrix argument
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = self.matrix.rows
        self.det = 0
    
    # Calculates the determinant of a matrix
    def calc(self):
        curr = [] # Stores element and its submatrix
        naiveDeterminant.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        # 0 x 0 matrix
        if self.size == 0:
            naiveDeterminant.saved.append((saver.names, "\\text{A matrix of size 0 has}$$$$\\text{a determinant of 1}"))
            saver.names += 1
            self.det = 1
            for key, value in naiveDeterminant.saved:
                if key == "single":
                    naiveDeterminant.saved.remove((key, value))
            naiveDeterminant.saved.append(single_view(naiveDeterminant.saved))
            return self.det
        # 1 x 1 matrix
        elif self.size == 1:
            naiveDeterminant.saved.append((saver.names, "\\text{A matrix of size 1 has a}$$$$\\text{determinant equal to its only value}"))
            saver.names += 1
            self.det = self.matrix[0]
            for key, value in naiveDeterminant.saved:
                if key == "single":
                    naiveDeterminant.saved.remove((key, value))
            naiveDeterminant.saved.append(single_view(naiveDeterminant.saved))
            return self.det
        # 2 x 2 or larger matrix
        else:
            naiveDeterminant.saved.append((saver.names, "\\text{Take the first row of the matrix}$$$$"+sp.latex(self.matrix[0,:])))
            saver.names += 1
            naiveDeterminant.saved.append((saver.names, "\\text{Take the minors of each element respectively}"))
            saver.names += 1
            # Finding and storing element with corresponding submatrix
            for i in range(self.size):
                curr_element = self.matrix[i]
                curr_submatrix = self.matrix.minor_submatrix(0, i)
                curr.append((curr_element, curr_submatrix))
                naiveDeterminant.saved.append((saver.names, "\\text{The submatrix of the element}$$$$a_{1"+str(i+1)+"}="+sp.latex(curr_element)+"\\text{ is }"+sp.latex(curr_submatrix)))
                saver.names += 1
            symb_toggle = 0
            minor_expr = ""
            # Forms Laplace Expansion expression in LaTeX
            for j in curr:
                minor_expr += sp.latex(j[0])+sp.latex(j[1])
                if symb_toggle == 0:
                    minor_expr += '-'
                    symb_toggle = 1
                elif symb_toggle == 1:
                    minor_expr += '+'
                    symb_toggle = 0
            minor_expr = minor_expr[:-1]
            naiveDeterminant.saved.append((saver.names, "\\text{This forms the following expression}$$$$"+minor_expr))
            saver.names += 1
            neg_toggle = 0 # To alternate signs between adjacent elements
            self.final_equation = ""
            # Recursively calculates determinant of matrix
            for i in range(self.size):
                # Deals with +ve parts of Laplace Expansion expression
                if neg_toggle % 2 == 0:
                    # For 1 x 1 submatrices
                    if self.size - 1 == 1:
                        self.det += curr[i][0] * curr[i][1][0]
                        self.final_equation += "+"+sp.latex(curr[i][0])+"*"+sp.latex(curr[i][1][0])
                    # For submatrices larger than 1 x 1
                    else:
                        naiveDeterminant.saved.append((saver.names, "\\text{Take the determinant of the matrix}"))
                        saver.names += 1
                        # Calculating determinant of submatrix
                        sub = naiveDeterminant(curr[i][1])
                        sub_det = sub.calc()
                        self.final_equation += "+"+sp.latex(curr[i][0])+"*"+sp.latex(sub_det)
                        # Adding to current determinant value
                        self.det += curr[i][0] * sub_det
                        naiveDeterminant.saved.append((saver.names, "\\text{The determinant of the minor}$$$$"+sp.latex(curr[i][1])+"\\text{ is }"+sp.latex(sub_det)))
                        saver.names += 1
                # Deals with -ve parts of Laplace Expansion expression
                elif neg_toggle % 2 == 1:
                    # For 1 x 1 submatrices
                    if self.size - 1 == 1:
                        self.det -= curr[i][0] * curr[i][1][0]
                        self.final_equation += "+"+sp.latex(curr[i][0])+"*"+sp.latex(curr[i][1][0])
                    # For submatrices larger than 1 x 1
                    else:
                        naiveDeterminant.saved.append((saver.names, "\\text{Take the determinant of the matrix}"))
                        saver.names += 1
                        # Calculating determinant of submatrix
                        sub = naiveDeterminant(curr[i][1])
                        sub_det = sub.calc()
                        self.final_equation += "-"+sp.latex(curr[i][0])+"*"+sp.latex(sub_det)
                        # Adding to current determinant value
                        self.det -= curr[i][0] * sub_det
                        naiveDeterminant.saved.append((saver.names, "\\text{The determinant of the minor}$$$$"+sp.latex(curr[i][1])+"\\text{ is }"+sp.latex(sub_det)))
                        saver.names += 1
                neg_toggle += 1 # Alternating elements in expression have opposite sign
            naiveDeterminant.saved.append((saver.names, "\\text{The expression becomes}$$$$"+self.final_equation[1:]+"$$$$\\text{giving a value of }"+sp.latex(self.det)))
            saver.names += 1
            naiveDeterminant.saved.append((saver.names, "\\text{Therefore, the determinant}$$$$\\text{of the matrix is }"+sp.latex(self.det)))
            saver.names += 1
            for key, value in naiveDeterminant.saved:
                if key == "single":
                    naiveDeterminant.saved.remove((key, value))
            naiveDeterminant.saved.append(single_view(naiveDeterminant.saved))
            return self.det

    # Adds steps from class variable list to shared list
    def addSaved(self, check):
        if check == True:
            saver.saved += naiveDeterminant.saved

    # Converts the matrices and expressions to images for single method
    def latex2img(self):
        for i in saver.saved:
            text2image.convertLatex(i[1], i[0])
        naiveDeterminant.saved = []

    # Converts the matrices and expressions to images for method comparison
    def compare_latex2img(self):
        for i in naiveDeterminant.saved:
            compare_text2image.convertLatex(i[1], i[0], "Laplace")
        naiveDeterminant.saved = []

# Sarrus' Method
class Sarrus:
    # Constructor takes square matrix argument
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = self.matrix.rows
        self.saved = []
        self.det = 0

    # Calculates the determinant of a matrix
    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        # If input matrix is not a 3 x 3 matrix
        if self.size != 3:
            self.saved.append((saver.names, "\\text{Sarrus' method cannot be used}$$$$\\text{for "+sp.latex(self.size)+"x"+sp.latex(self.size)+" matrices}"))
            saver.names += 1
            self.saved.append(single_view(self.saved))
            return "N/A"
        # If input matrix is a 3 x 3 matrix
        else:
            # Multiplying along diagonals
            R1 = self.matrix[0, 0] * self.matrix[1, 1] * self.matrix[2, 2]
            self.saved.append((saver.names, "\\text{First, multiply the values}$$$$\\text{along the leading diagonal}$$$$"
            +"R_1="+sp.latex(self.matrix[0, 0])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 2])+"={}".format(R1)))
            saver.names += 1
            R2 = self.matrix[1, 0] * self.matrix[2, 1] * self.matrix[0, 2]
            self.saved.append((saver.names, """\\text{Then, multiply the values along the first}$$$$\\text{subdiagonal by assuming an identical matrix}
            $$$$\\text{is directly below the original matrix so that}$$$$\\text{the final element of the multiplication is the}$$$$\\text{element at } a_{13}$$$$"""
            +"R_2="+sp.latex(self.matrix[1, 0])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 2])+"={}".format(R2)))
            saver.names += 1
            R3 = self.matrix[2, 0] * self.matrix[0, 1] * self.matrix[1, 2]
            self.saved.append((saver.names, """\\text{Then, multiply the values}$$$$\\text{along the second subdiagonal by}$$$$\\text{making the same assumption}
            $$$$\\text{as the previous multiplication,}$$$$\\text{so the final 2 elements are at }$$$$a_{12}\\text{ and } a_{23}$$$$"""
            +"R_3="+sp.latex(self.matrix[2, 0])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 2])+"={}".format(R3)))
            saver.names += 1
            # Summing values from diagonal multiplication
            R = R1 + R2 + R3
            self.saved.append((saver.names, "\\text{Now, add together the products}$$$$"
            +"R=R_1+R_2+R_3$$$$="+sp.latex(R1)+"+"+sp.latex(R2)+"+"+sp.latex(R3)+"={}".format(R)))
            saver.names += 1

            # Multiplying along antidiagonals
            L1 = self.matrix[0, 2] * self.matrix[1, 1] * self.matrix[2, 0]
            self.saved.append((saver.names, "\\text{Now do the same for the anti-diagonals,}$$$$\\text{starting with the leading anti-diagonal.}$$$$"
            +"\\text{It is important to remember that the}$$$$\\text{anti-diagonal is the leading diagonal}$$$$\\text{going from right to left.}$$$$"
            +"L_1="+sp.latex(self.matrix[0, 2])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 0])+"={}".format(L1)))
            saver.names += 1
            L2 = self.matrix[1, 2] * self.matrix[2, 1] * self.matrix[0, 0]
            self.saved.append((saver.names, "\\text{Then, multiply the values}$$$$\\text{along the anti-subdiagonal}$$$$"
            +"L_2="+sp.latex(self.matrix[1, 2])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 0])+"={}".format(L2)))
            saver.names += 1
            L3 = self.matrix[2, 2] * self.matrix[0, 1] * self.matrix[1, 0]
            self.saved.append((saver.names, "\\text{Then, multiply the values}$$$$\\text{along the second anti-subdiagonal}$$$$"
            +"L_3="+sp.latex(self.matrix[2, 2])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 0])+"={}".format(L3)))
            saver.names += 1
            # Summing values from antidiagonal multiplication
            L = L1 + L2 + L3
            self.saved.append((saver.names, "\\text{Now, add together the products}$$$$"
            +"L=L_1+L_2+L_3="+sp.latex(L1)+"+"+sp.latex(L2)+"+"+sp.latex(L3)+"={}".format(L)))
            saver.names += 1

            # Calculating determinant of matrix
            self.det = R - L
            self.saved.append((saver.names, "\\text{Finally, subtract the sum of the anti-diagonal}$$$$\\text{multiplications from the diagonal multiplications.}$$$$"
            +"det=R-L="+sp.latex(R)+"-"+sp.latex(L)+"={}".format(self.det)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{Therefore, the determinant is }"+sp.latex(self.det)))
            saver.names += 1
            self.saved.append(single_view(self.saved))
            return self.det

    # Adds steps from instance variable list to shared list
    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved

    # Converts the matrices and expressions to images for single method
    def latex2img(self):
        for i in saver.saved:
            text2image.convertLatex(i[1], i[0])

    # Converts the matrices and expressions to images for method comparison
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.convertLatex(i[1], i[0], "Sarrus")

# LU Decomposition
class LU:
    # Constructor takes square matrix argument
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = self.matrix.rows
        self.saved = []
        self.det = 0

    # Calculates the determinant of a matrix
    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        # Empty lower triangular matrix
        L = sp.Matrix(self.size, self.size, [0]*self.size*self.size)
        self.saved.append((saver.names, "\\text{First, create an empty matrix representing}$$$$\\text{the lower triangular (L) matrix}$$$$"+sp.latex(L)))
        saver.names += 1
        # Populating lower triangular matrix with variables
        for i in range(self.size):
            for j in range(self.size):
                if i > j:
                    L[i, j] = sp.symbols('L_{}{}'.format(i+1,j+1))
                # 1s along leading diagonal
                elif i == j:
                    L[i, j] = 1
        self.saved.append((saver.names, "\\text{Populate the lower triangular matrix}$$$$\\text{with symbols in the bottom-left corner}$$$$"
        +"$$$$\\text{and 1's along the leading diagonal}$$$$"+sp.latex(L)))
        saver.names += 1
        # Empty upper triangular matrix
        U = sp.Matrix(self.size, self.size, [0]*self.size*self.size)
        self.saved.append((saver.names, "\\text{Next, create an empty matrix representing}$$$$\\text{the upper triangular (U) matrix}$$$$"+sp.latex(U)))
        saver.names += 1
        # Populating upper triangular matrix with variables
        for i in range(self.size):
            for j in range(self.size):
                if i <= j:
                    U[i, j] = sp.symbols('U_{}{}'.format(i+1,j+1))
        self.saved.append((saver.names, "\\text{Populate the upper triangular matrix}$$$$\\text{with symbols in the top-right corner}$$$$"
        +"\\text{and along the leading diagonal}$$$$"+sp.latex(U)))
        saver.names += 1
        LU = L*U # Multiplication of lower and upper triangular matrices
        self.saved.append((saver.names, "\\text{Next, multiply the L and U matrices}$$$$\\text{to form the resultant matrix}$$$$"
        +sp.latex(LU)+", $$$$\\text{which is equivalent to the original matrix}"))
        saver.names += 1
        self.saved.append((saver.names, sp.latex(LU)+"="+sp.latex(self.matrix)))
        saver.names += 1
        self.saved.append((saver.names, "\\text{By comparison of corresponding elements,}$$$$\\text{deduce the L and U matrix elements}"))
        saver.names += 1
        # Solving for lower and upper triangular matrix values
        # Iterates through each element of LU matrix and equates to same element in input matrix
        for i in range(self.size):
            for j in range(self.size):
                try:
                    curr_var = LU[i, j] # Current element value in LU matrix
                    curr_num = self.matrix[i, j] # Corresponding element value in input matrix
                    self.saved.append((saver.names, "\\text{For element } a_{"+str(i+1)+str(j+1)+"} \\text{ in LU,}$$$$"+sp.latex(curr_var)+"="+sp.latex(curr_num)))
                    saver.names += 1
                    symb = list(curr_var.free_symbols)[0] # Finds all variables in current element of LU matrix
                    solution = sp.solve(curr_var-curr_num, symb)[0] # Solves for a variable
                    self.saved.append((saver.names, "\\text{This can be solved for }"+sp.latex(symb)+"$$$$\\text{ giving a value of }"+sp.latex(solution)))
                    saver.names += 1
                    # Substituting solution back into U and LU matrices
                    if symb in U:
                        U = U.subs(symb, solution)
                        LU = LU.subs(symb, solution)
                        self.saved.append((saver.names, "\\text{This value is substituted back}$$$$\\text{into U and LU to give}$$$$U="+sp.latex(U)+",$$$$LU="+sp.latex(LU)))
                        saver.names += 1
                    # Substituting solution back into L and LU matrices
                    elif symb in L:
                        L = L.subs(symb, solution)
                        LU = LU.subs(symb, solution)
                        self.saved.append((saver.names, "\\text{This value is substituted back}$$$$\\text{into L and LU to give}$$$$L="+sp.latex(L)+",$$$$LU="+sp.latex(LU)))
                        saver.names += 1
                except:
                    pass
        L_det = 1
        U_det = 1
        # Taking product of leading diagonals
        for i in range(self.size):
            L_det *= L[i, i]
            U_det *= U[i, i]
        self.saved.append((saver.names, "\\text{Now, multiply along the leading diagonal}"))
        saver.names += 1
        self.saved.append((saver.names, "L="+sp.latex(L)+"\\rightarrow{}".format(L_det)+"$$$$U="+sp.latex(U)+"\\rightarrow{}".format(U_det)))
        saver.names += 1
        # Calculates determinant by multiplying leading diagonal products
        self.det = L_det * U_det
        self.saved.append((saver.names, """\\text{The determinant of the matrix is calculated}$$$$
        \\text{from multiplying the 2 previous values}$$$$
        \\text{det}={"""+sp.latex(L_det)+"}*{"+sp.latex(U_det)+"}={"+sp.latex(self.det)+"}"))
        saver.names += 1
        self.saved.append((saver.names, "\\text{Therefore, the determinant is }"+sp.latex(self.det)))
        saver.names += 1
        self.saved.append(single_view(self.saved))
        return self.det

    # Adds steps from instance variable list to shared list
    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved

    # Converts the matrices and expressions to images for single method
    def latex2img(self):
        for i in saver.saved:
            text2image.convertLatex(i[1], i[0])

    # Converts the matrices and expressions to images for method comparison
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.convertLatex(i[1], i[0], "LU")

# Stores method class and name for subfolder
def getMethods():
    methods = []
    methods.append(("Laplace", naiveDeterminant))
    methods.append(("Sarrus", Sarrus))
    methods.append(("LU", LU))
    return methods