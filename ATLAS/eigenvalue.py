import sympy as sp
import text2image
import compare_text2image
from determinant import naiveDeterminant
import saver

# Characteristic Equation
class Characteristic:
    # Constructor takes a square matrix as argument
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []

    # Calculates eigenvalues
    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        I = sp.eye(self.size) # Identity matrix
        lamda = sp.Symbol('lamda')
        lamda_I = lamda*I
        # Subtracting identity matrix multiplied by variable from matrix
        new_matrix = self.matrix - lamda_I
        self.saved.append((saver.names, """\\text{First, subtract }\lambda\\text{ multiplied by}$$$$
        \\text{the identity matrix from the matrix}$$$$"""+sp.latex(self.matrix)+str('-')+sp.latex(lamda)+sp.latex(I)))
        saver.names += 1
        self.saved.append((saver.names, "\\text{This results in}$$$$"+sp.latex(new_matrix)))
        saver.names += 1
        # Calculating characteristic polynomial
        characteristic = sp.expand(naiveDeterminant(new_matrix).calc())
        self.saved.append((saver.names, """\\text{Then, calculate the determinant of this matrix}$$$$
        \\text{and equate it to 0, giving the following equation}$$$$"""+sp.latex(characteristic)+"=0"))
        saver.names += 1
        # Solving characteristic equation for eigenvalues
        solved_lamda = sp.roots(characteristic, lamda)
        eigenvalues = [] # List for eigenvalues
        self.saved.append((saver.names, "\\text{Finally, solve this equation to get the eigenvalues.}"
        +"$$$$\\text{The method of solving the equation depends on the indices.}"
        +"$$$$\\text{Larger indices may require approximation of solutions.}"))
        saver.names += 1
        # Converting eigenvalues to numerical form
        for i in solved_lamda.items():
            solution = i[0].evalf(chop=True)
            amount = i[1]
            # Dealing with repeated eigenvalues
            while amount > 0:
                eigenvalues.append(solution)
                amount -= 1
                self.saved.append((saver.names, sp.latex(lamda)+"="+sp.latex(solution)))
                saver.names += 1
        return eigenvalues

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
            compare_text2image.convertLatex(i[1], i[0], "Characteristic")

# Stores method class and name for subfolder
def getMethods():
    methods = []
    methods.append(("Characteristic", Characteristic))
    return methods