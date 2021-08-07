import sympy as sp
from eigenvalue import Eigenvalue
from solving import GaussianElimination
import text2image
import compare_text2image
from string import ascii_lowercase
# from emptyimg import empty
import saver

class Eigenvector:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []
    
    def calc(self):
        eigenvalues = Eigenvalue(self.matrix).calc()
        eigenvalues = [round(num, 4) for num in eigenvalues]
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        self.saved.append((saver.names, "\\text{First, calculate the eigenvalues of the matrix}$$$$"
        +sp.latex(self.matrix)+"$$$$\\text{giving eigenvalues of}$$$$"+sp.latex(eigenvalues)))
        saver.names += 1
        eigenvectors = []
        I = sp.eye(self.size)
        self.saved.append((saver.names, "\\text{Take each eigenvalue in turn}$$$$\\text{and calculate the eigenvector}"))
        saver.names += 1
        unique_eigenvalues = set(eigenvalues)
        for e_value in unique_eigenvalues:
            self.saved.append((saver.names, "\\text{Looking at the eigenvalue}$$$$"+sp.latex(sp.Symbol("lamda"))+"="+sp.latex(e_value)))
            saver.names += 1
            e_I = e_value*I
            new_matrix = self.matrix - e_I
            self.saved.append((saver.names, "\\text{Subtract from the matrix, the identity}$$$$\\text{matrix multiplied by the eigenvalue}$$$$"
            +sp.latex(self.matrix)+"-"+sp.latex(round(e_value, 4))+sp.latex(I)))
            saver.names += 1
            self.saved.append((saver.names, "\\text{This gives the following matrix}$$$$"+sp.latex(new_matrix)))
            saver.names += 1
            new_matrix = new_matrix.col_insert(self.size, sp.Matrix([0]*self.size))
            self.saved.append((saver.names, "\\text{Converting it to}$$$$"+sp.latex(new_matrix)+"$$$$\\text{allows it to be solved as}$$$$\\text{a system of linear equations}"))
            saver.names += 1
            solved, solutions, row_ech = GaussianElimination(new_matrix).calc()
            row_ech = row_ech.n(4)
            unique = eigenvalues.count(e_value)
            if solved == True and unique == 1:
                self.saved.append((saver.names, "\\text{Using Gaussian Elimination, the}$$$$\\text{matrix is converted to row echelon form}$$$$"+sp.latex(row_ech)))
                saver.names += 1
                self.saved.append((saver.names, "\\text{This is solved using back substitution}$$$$\\text{giving solutions of}$$$$"+sp.latex(solutions)))
                saver.names += 1
                eigenvector = sp.Matrix(self.size, 1, solutions)
                eigenvectors.append((e_value, eigenvector))
                self.saved.append((saver.names, "\\text{Therefore, for the eigenvalue }"+sp.latex(e_value)+",$$$$\\text{the eigenvector is }"+sp.latex(eigenvector)))
                saver.names += 1
            elif solved == True and unique > 1:
                self.saved.append((saver.names, "\\text{Using Gaussian Elimination, the}$$$$\\text{matrix is converted to row echelon form}$$$$"+sp.latex(row_ech)))
                saver.names += 1
                self.saved.append((saver.names, "\\text{Since the eigenvalue }"+sp.latex(e_value)
                +"\\text{ has a multiplicity}$$$$\\text{which is greater than 1, it cannot be solved by}$$$$"
                +"\\text{back substitution on the row echelon form matrix}"))
                saver.names += 1
                row_ech.col_del(self.size)
                atoms = list(ascii_lowercase)
                vars = sp.Matrix(self.size, 1, atoms[:self.size])
                prod = row_ech*vars
                self.saved.append((saver.names, "\\text{The matrix in row echelon form is multiplied}$$$$\\text{by a column vector of unknown variables}$$$$"
                +sp.latex(row_ech)+"*"+sp.latex(vars)+"="+sp.latex(prod)))
                saver.names += 1
                solutions = []
                for i in prod:
                    if i != 0:
                        self.saved.append((saver.names, "\\text{Then, the expression}$$$$"+sp.latex(i)+"=0"+"$$$$\\text{can be solved for a variable by equating it to 0}"
                        "$$$$\\text{giving a solution of}"+sp.latex(sp.solve(i)[0])))
                        saver.names += 1
                    solutions.append(sp.solve(i))
                for i in solutions:
                    try:
                        for key, value in i[0].items():
                            self.saved.append((saver.names, "\\text{Substituting }"+sp.latex(key)+"="+sp.latex(value)+"$$$$\\text{back into column vector of unknowns}"
                            +"$$$$\\text{such that }"+sp.latex(vars)+"\\rightarrow"+sp.latex(vars.subs(key, value))))
                            saver.names += 1
                            vars = vars.subs(key, value)
                    except:
                        pass
                free = list(vars.free_symbols)
                self.saved.append((saver.names, "\\text{For the free variables }"+sp.latex(free)+",$$$$\\text{each variable is set to 1 and the others are set to 0,}"
                +"$$$$\\text{allowing the different eigenvectors to be calculated}"))
                saver.names += 1
                for i in range(len(free)):
                    curr = free[i]
                    self.saved.append((saver.names, "\\text{The free variable }"+sp.latex(curr)+"\\text{ is set to 1}"))
                    saver.names += 1
                    rem = free[:i] + free[i+1:]
                    self.saved.append((saver.names, "\\text{The remaining variables }"+sp.latex(rem)+"\\text{ are set to 0}"))
                    saver.names += 1
                    self.saved.append((saver.names, "\\text{Substituting }"+sp.latex(curr)+"="+"1$$$$\\text{gives }"
                    +sp.latex(vars)+"\\rightarrow"+sp.latex(vars.subs(curr, 1))))
                    saver.names += 1
                    subbed = vars.subs(curr, 1)
                    for j in rem:
                        self.saved.append((saver.names, "\\text{Substituting }"+sp.latex(j)+"="+"0$$$$\\text{gives }"
                        +sp.latex(subbed)+"\\rightarrow"+sp.latex(subbed.subs(j, 0))))
                        saver.names += 1
                        subbed = subbed.subs(j, 0)
                    self.saved.append((saver.names, "\\text{For the eigenvalue }"+sp.latex(e_value)+",$$$$\\text{the eigenvector is }"+sp.latex(subbed)))
                    eigenvectors.append((e_value, subbed))
                    saver.names += 1
        self.saved.append((saver.names, "\\text{Therefore, the eigenvalues and eigenvectors for}$$$$"+sp.latex(self.matrix)+"$$$$\\text{are}"))
        saver.names += 1
        for i in eigenvectors:
            self.saved.append((saver.names, sp.latex(sp.Symbol("lamda"))+"="+sp.latex(i[0])+", "+sp.latex(sp.Symbol("v"))+"="+sp.latex(i[1])))
            saver.names += 1
        return eigenvectors

    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved

    def latex2img(self):
        for i in saver.saved:
            text2image.formula_as_file(i[1], i[0])
        # for i in saver.text:
        #     toImage(i[1], i[0])

    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.formula_as_file(i[1], i[0], "Gaussian")
        # for i in saver.text:
        #     toImage(i[1], i[0])


def getMethods():
    methods = []
    methods.append(("Gaussian", Eigenvector))
    return methods

# empty()
# x = sp.Matrix([[1,1,1],[2,-3,4],[3,4,5]])
# x = sp.Matrix([[2,-1,-1,0],[-1,3,-1,-1],[-1,-1,3,-1],[0,-1,-1,2]])
# sp.pprint(x)
# new = Eigenvector(x)
# y = new.calc()
# for i in y:
#     sp.pprint(i[0])
#     sp.pprint(i[1])
#     print()
# new.latex2img()