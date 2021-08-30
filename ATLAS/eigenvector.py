import sympy as sp
from eigenvalue import Characteristic
from solving import GaussianElimination
import text2image
import compare_text2image
from string import ascii_lowercase
import saver
from single_image import single_view

# Eigenvector By Characteristic Polynomial + Gaussian Elimination
class CharGauss:
    # Constructor takes a square matrix as argument
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []

    # Calculates eigenvectors
    def calc(self):
        # Calculating eigenvalues of matrix
        eigenvalues = Characteristic(self.matrix).calc()
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        self.saved.append((saver.names, "\\text{First, calculate the eigenvalues of the matrix}$$$$"
        +sp.latex(self.matrix)+"$$$$\\text{giving eigenvalues of}$$$$"+sp.latex(eigenvalues)))
        saver.names += 1
        eigenvectors = [] # List for eigenvalue-eigenvector pairs
        I = sp.eye(self.size) # Identity matrix
        self.saved.append((saver.names, "\\text{Take each eigenvalue in turn}$$$$\\text{and calculate the eigenvector}"))
        saver.names += 1
        # Removes duplicate eigenvalues
        unique_eigenvalues = set(eigenvalues)
        # Calculates eigenvector for each eigenvalue
        for e_value in unique_eigenvalues:
            self.saved.append((saver.names, "\\text{Looking at the eigenvalue}$$$$"+sp.latex(sp.Symbol("lamda"))+"="+sp.latex(e_value)))
            saver.names += 1
            # Subtracting identity matrix multiplied by eigenvalue from matrix
            e_I = e_value*I
            new_matrix = self.matrix - e_I
            self.saved.append((saver.names, "\\text{Subtract from the matrix, the identity}$$$$\\text{matrix multiplied by the eigenvalue}$$$$"
            +sp.latex(self.matrix)+"-"+sp.latex(round(e_value, 4))+sp.latex(I)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{This gives the following matrix}$$$$"+sp.latex(new_matrix)))
            saver.names += 1
            # Adding column of constants with only 0s
            new_matrix = new_matrix.col_insert(self.size, sp.Matrix([0]*self.size))
            self.saved.append((saver.names, "\\text{Converting it to}$$$$"+sp.latex(new_matrix)+"$$$$\\text{allows it to be solved as}$$$$\\text{a system of linear equations}"))
            saver.names += 1
            # Calculating solutions to matrix
            solved, solutions, row_ech = GaussianElimination(new_matrix[:, :]).calc()
            row_ech = row_ech.n(4)
            # Identifying repeated eigenvalues
            unique = eigenvalues.count(e_value)
            # If solution is found and eigenvalue is NOT repeated
            if solved == True and unique == 1:
                self.saved.append((saver.names, "\\text{Using Gaussian Elimination, the}$$$$\\text{matrix is converted to row echelon form}$$$$"+sp.latex(row_ech)))
                saver.names += 1
                self.saved.append((saver.names, "\\text{This is solved using back substitution}$$$$\\text{giving solutions of}$$$$"+sp.latex(solutions)))
                saver.names += 1
                # Eigenvector generated using solutions
                eigenvector = sp.Matrix(self.size, 1, solutions)
                eigenvectors.append((e_value, eigenvector))
                self.saved.append((saver.names, "\\text{Therefore, for the eigenvalue }"+sp.latex(e_value)+",$$$$\\text{the eigenvector is }"+sp.latex(eigenvector)))
                saver.names += 1
            # If solution is found and eigenvalue is repeated
            elif solved == True and unique > 1:
                self.saved.append((saver.names, "\\text{Using Gaussian Elimination, the}$$$$\\text{matrix is converted to row echelon form}$$$$"+sp.latex(row_ech)))
                saver.names += 1
                self.saved.append((saver.names, "\\text{Since the eigenvalue }"+sp.latex(e_value)
                +"\\text{ has a multiplicity}$$$$\\text{which is greater than 1, it cannot be solved by}$$$$"
                +"\\text{back substitution on the row echelon form matrix}"))
                saver.names += 1
                row_ech.col_del(self.size)
                # Creating list of variables
                atoms = list(ascii_lowercase)
                # Generating eigenvector of variables
                vars = sp.Matrix(self.size, 1, atoms[:self.size])
                # Product of row echelon matrix and eigenvector
                prod = row_ech*vars
                self.saved.append((saver.names, "\\text{The matrix in row echelon form is multiplied}$$$$\\text{by a column vector of unknown variables}$$$$"
                +sp.latex(row_ech)+"*"+sp.latex(vars)+"="+sp.latex(prod)))
                saver.names += 1
                solutions = [] # List for eigenvector values
                # Solving each expression within product eigenvector
                for i in prod:
                    if i != 0:
                        self.saved.append((saver.names, "\\text{Then, the equation}$$$$"+sp.latex(i)+"=0"+"$$$$\\text{can be solved for a variable by equating it to 0}"
                        "$$$$\\text{giving a solution of}"+sp.latex(sp.solve(i)[0])))
                        saver.names += 1
                        solutions.append(sp.solve(i))
                # Substituting each solution into eigenvector of variables
                for i in solutions:
                    for key, value in i[0].items():
                        self.saved.append((saver.names, "\\text{Substituting }"+sp.latex(key)+"="+sp.latex(value)+"$$$$\\text{back into column vector of unknowns}"
                        +"$$$$\\text{such that }"+sp.latex(vars)+"\\rightarrow"+sp.latex(vars.subs(key, value))))
                        saver.names += 1
                        vars = vars.subs(key, value)
                # Finding all unknowns in eigenvector of variables
                free = list(vars.free_symbols)
                self.saved.append((saver.names, "\\text{For the free variables }"+sp.latex(free)+",$$$$\\text{each variable is set to 1 and the others are set to 0,}"
                +"$$$$\\text{allowing the different eigenvectors to be calculated}"))
                saver.names += 1
                # For each unknown in eigenvector of variables
                for i in range(len(free)):
                    variable = free[i] # 1 unknown
                    self.saved.append((saver.names, "\\text{The free variable }"+sp.latex(variable)+"\\text{ is set to 1}"))
                    saver.names += 1
                    rem = free[:i] + free[i+1:] # Remaining unknowns
                    self.saved.append((saver.names, "\\text{The remaining variables }"+sp.latex(rem)+"\\text{ are set to 0}"))
                    saver.names += 1
                    self.saved.append((saver.names, "\\text{Substituting }"+sp.latex(variable)+"="+"1$$$$\\text{gives }"
                    +sp.latex(vars)+"\\rightarrow"+sp.latex(vars.subs(variable, 1))))
                    saver.names += 1
                    # Substituting 1 for 1st unknown
                    subbed = vars.subs(variable, 1)
                    # Substituting 0 for remaining unknowns 
                    for j in rem:
                        self.saved.append((saver.names, "\\text{Substituting }"+sp.latex(j)+"="+"0$$$$\\text{gives }"
                        +sp.latex(subbed)+"\\rightarrow"+sp.latex(subbed.subs(j, 0))))
                        saver.names += 1
                        subbed = subbed.subs(j, 0)
                    self.saved.append((saver.names, "\\text{For the eigenvalue }"+sp.latex(e_value)+",$$$$\\text{the eigenvector is }"+sp.latex(subbed)))
                    saver.names += 1
                    eigenvectors.append((e_value, subbed))
                    saver.names += 1
        self.saved.append((saver.names, "\\text{Therefore, the eigenvalues and eigenvectors for}$$$$"+sp.latex(self.matrix)+"$$$$\\text{are}"))
        saver.names += 1
        # Generating images with eigenvalue and eigenvector together
        for i in eigenvectors:
            self.saved.append((saver.names, sp.latex(sp.Symbol("lamda"))+"="+sp.latex(i[0])+", "+sp.latex(sp.Symbol("v"))+"="+sp.latex(i[1])))
            saver.names += 1
        self.saved.append(single_view(self.saved))
        return eigenvectors

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
            compare_text2image.convertLatex(i[1], i[0], "Gaussian")

# Stores method class and name for subfolder
def getMethods():
    methods = []
    methods.append(("Gaussian", CharGauss))
    return methods