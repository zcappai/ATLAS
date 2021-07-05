from enum import unique
import sympy as sp
from eigenvalue import Eigenvalue
from solving import GaussianElimination
from text2image import toImage, formula_as_file
from string import ascii_lowercase
from emptyimg import empty

class Eigenvector:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []
        self.text = []
        # self.atoms = list(ascii_lowercase)
        # for x in range(self.size//26 + 1):
        #     self.atoms += ["".join([i, str(x)]) for i in list(ascii_lowercase)]
    
    def calc(self):
        names = 1
        self.text.append((names, "First, calculate the eigenvalues of the matrix"))
        names += 1
        self.text.append((names, "Giving eigenvalues of"))
        names += 1
        eigenvalues = Eigenvalue(self.matrix).calc()
        for i in eigenvalues:
            self.saved.append((names, sp.latex(sp.Symbol("lamda"))+"="+str(i)))
            names += 1
        eigenvectors = []
        # print(eigenvalues)
        # symbols = self.atoms[:self.size]
        I = sp.eye(self.size)
        self.text.append((names, "Then, taking each eigenvalue in turn, calculate the eigenvector"))
        names += 1
        unique_eigenvalues = set(eigenvalues)
        for e_value in unique_eigenvalues:
            self.text.append((names, "Looking at the eigenvalue"))
            names += 1
            self.saved.append((names, sp.latex(sp.Symbol("lamda"))+"="+sp.latex(e_value)))
            names += 1
            # vector_arr = []
            self.text.append((names, "Subtract from the matrix, the identity matrix multiplied by the eigenvalue"))
            names += 1
            e_I = e_value*I
            new_matrix = self.matrix - e_I
            # sp.pprint(new_matrix)
            self.saved.append((names, sp.latex(self.matrix)+"-"+sp.latex(round(e_value, 4))+sp.latex(I)))
            names += 1
            self.text.append((names, "To give the following matrix"))
            names += 1
            self.saved.append((names, sp.latex(new_matrix)))
            names += 1
            self.text.append((names, "Converting as follows..."))
            names += 1
            new_matrix = new_matrix.col_insert(self.size, sp.Matrix([0]*self.size))
            self.saved.append((names, sp.latex(new_matrix)))
            names += 1
            self.text.append((names, "...allows it to be solved as a system of linear equations"))
            names += 1
            solved, solutions, row_ech = GaussianElimination(new_matrix).calc()
            unique = eigenvalues.count(e_value)
            if solved == True and unique == 1:
                self.text.append((names, "Using Gaussian Elimination, the matrix is converted to row echelon form"))
                names += 1
                self.saved.append((names, sp.latex(row_ech)))
                names += 1
                self.text.append((names, "This is solved using back substitution"))
                names += 1
                self.text.append((names, "Giving values of"))
                names += 1
                self.saved.append((names, sp.latex(solutions)))
                names += 1
                eigenvector = sp.Matrix(self.size, 1, solutions)
                eigenvectors.append((e_value, eigenvector))
                self.text.append((names, "Therefore, the eigenvector for the eigenvalue"))
                names += 1
                self.saved.append((names, sp.latex(e_value)))
                names += 1
                self.text.append((names, "is"))
                names += 1
                self.saved.append((names, sp.latex(eigenvector)))
                names += 1
            elif solved == True and unique > 1:
                row_ech.col_del(self.size)
                atoms = list(ascii_lowercase)
                vars = sp.Matrix(self.size, 1, atoms[:self.size])
                prod = row_ech*vars
                solutions = []
                for i in prod:
                    solutions.append(sp.solve(i))
                for i in solutions:
                    try:
                        for key, value in i[0].items():
                            vars = vars.subs(key, value)
                    except:
                        pass
                free = list(vars.free_symbols)
                for i in range(len(free)):
                    curr = free[i]
                    rem = free[:i] + free[i+1:]
                    temp = vars.subs(curr, 1)
                    for j in rem:
                        temp = temp.subs(j, 0)
                    eigenvectors.append((e_value, temp))
        self.text.append((names, "Therefore, the eigenvalues and eigenvectors for the matrix"))
        names += 1
        self.saved.append((names, sp.latex(self.matrix)))
        names += 1
        self.text.append((names, "are"))
        names += 1
        for i in eigenvectors:
            self.saved.append((names, sp.latex(sp.Symbol("lamda"))+"="+sp.latex(i[0])+", "+sp.latex(sp.Symbol("v"))+"="+sp.latex(i[1])))
            names += 1
        return eigenvectors

    def latex2img(self):
        formula_as_file(sp.latex(self.matrix), 0)
        for i in self.saved:
            formula_as_file(i[1], i[0])
        for i in self.text:
            toImage(i[1], i[0])

# empty()
# # x = sp.Matrix([[1,1,1],[2,-3,4],[3,4,5]])
# x = sp.Matrix([[2,-1,-1,0],[-1,3,-1,-1],[-1,-1,3,-1],[0,-1,-1,2]])
# sp.pprint(x)
# new = Eigenvector(x)
# y = new.calc()
# # new.latex2img()
# for i in y:
#     sp.pprint(i[0])
#     sp.pprint(i[1])
#     print()