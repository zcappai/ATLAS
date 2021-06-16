import sympy as sp
from eigenvalue import Eigenvalue
from solving import GaussianElimination
from text2image import toImage
from string import ascii_lowercase
from latex2image import formula_as_file
from emptyimg import empty

class Eigenvector:
    saved = []
    text = []
    def __init__(self, matrix, size):
        self.matrix = matrix
        self.size = size
        self.atoms = list(ascii_lowercase)
        for x in range(self.size//26 + 1):
            self.atoms += ["".join([i, str(x)]) for i in list(ascii_lowercase)]
    
    def calc(self):
        names = 1
        Eigenvector.text.append((names, "First, calculate the eigenvalues of the matrix"))
        names += 1
        Eigenvector.text.append((names, "Giving eigenvalues of"))
        names += 1
        eigenvalues = Eigenvalue(self.matrix, self.size).calc()
        for i in eigenvalues:
            Eigenvector.saved.append((names, sp.latex(sp.Symbol("lamda"))+"="+str(i)))
            names += 1
        eigenvectors = []
        symbols = self.atoms[:self.size]
        I = sp.eye(self.size)
        Eigenvector.text.append((names, "Then, taking each eigenvalue in turn, calculate the eigenvector"))
        names += 1
        for e_value in eigenvalues:
            Eigenvector.text.append((names, "Looking at the eigenvalue"))
            names += 1
            Eigenvector.saved.append((names, sp.latex(sp.Symbol("lamda"))+"="+sp.latex(e_value)))
            names += 1
            vector_arr = []
            Eigenvector.text.append((names, "Subtract from the matrix, the identity matrix multiplied by the eigenvalue"))
            names += 1
            e_I = e_value*I
            new_matrix = self.matrix - e_I
            Eigenvector.saved.append((names, sp.latex(self.matrix)+"-"+sp.latex(round(e_value, 4))+sp.latex(I)))
            names += 1
            Eigenvector.text.append((names, "To give the following matrix"))
            names += 1
            Eigenvector.saved.append((names, sp.latex(new_matrix)))
            names += 1
            Eigenvector.text.append((names, "Converting as follows..."))
            names += 1
            new_matrix = new_matrix.col_insert(self.size, sp.Matrix([0]*self.size))
            Eigenvector.saved.append((names, sp.latex(new_matrix)))
            names += 1
            Eigenvector.text.append((names, "...allows it to be solved as a system of linear equations"))
            names += 1
            solved, solution_message, reduced = GaussianElimination(new_matrix, self.size, self.size).calc()
            if solved == True:
                Eigenvector.text.append((names, "Using Gaussian Elimination, the matrix is converted to row echelon form"))
                names += 1
                Eigenvector.saved.append((names, sp.latex(reduced)))
                names += 1
                Eigenvector.text.append((names, "This is solved using back substitution into"))
                names += 1
                reduced.col_del(self.size)
                col_vec = sp.Matrix(self.size, 1, symbols)
                new_mat = reduced * col_vec
                sub_val = 1
                Eigenvector.saved.append((names, sp.latex(reduced)+sp.latex(col_vec)))
                names += 1
                for i in range(1, self.size + 1):
                    vector_arr.append(sub_val)
                    Eigenvector.text.append((names, "By setting and substituting the value of"))
                    names += 1
                    Eigenvector.saved.append((names, sp.latex(symbols[-i])+"="+sp.latex(sub_val)))
                    names += 1
                    Eigenvector.text.append((names, "This matrix becomes"))
                    names += 1
                    new_mat = new_mat.subs(symbols[-i], sub_val)
                    Eigenvector.saved.append((names, sp.latex(new_mat)))
                    names += 1
                    if i < self.size:
                        Eigenvector.text.append((names, "Such that the next row in the matrix can be solved for variable "+str(symbols[-(i+1)])))
                        names += 1
                        Eigenvector.text.append((names, "Giving a value of"))
                        names += 1
                        sub_val = sp.solve(new_mat[self.size-(i+1)], symbols[-(i+1)])[0]
                        Eigenvector.saved.append((names, sp.latex(symbols[-(i+1)])+"="+sp.latex(sub_val)))
                        names += 1
                vector_arr.reverse()
                eigenvector = sp.Matrix(self.size, 1, vector_arr)
                eigenvectors.append((e_value, eigenvector))
                Eigenvector.text.append((names, "Therefore, the eigenvector for the eigenvalue"))
                names += 1
                Eigenvector.saved.append((names, sp.latex(e_value)))
                names += 1
                Eigenvector.text.append((names, "is"))
                names += 1
                Eigenvector.saved.append((names, sp.latex(eigenvector)))
                names += 1
        Eigenvector.text.append((names, "Therefore, the eigenvalues and eigenvectors for the matrix"))
        names += 1
        Eigenvector.saved.append((names, sp.latex(self.matrix)))
        names += 1
        Eigenvector.text.append((names, "are"))
        names += 1
        for i in eigenvectors:
            Eigenvector.saved.append((names, sp.latex(sp.Symbol("lamda"))+"="+sp.latex(i[0])+", "+sp.latex(sp.Symbol("v"))+"="+sp.latex(i[1])))
            names += 1
        return eigenvectors

    def latex2img(self):
        formula_as_file(sp.latex(self.matrix), 'images/0.png')
        for i in Eigenvector.saved:
            formula_as_file(i[1], 'images/'+str(i[0])+'.png')
        for i in Eigenvector.text:
            toImage(i[1], i[0])

# empty()
# x = sp.Matrix([[1,1,1],[2,-3,4],[3,4,5]])
# sp.pprint(x)
# new = Eigenvector(x, 3)
# y = new.calc()
# new.latex2img()
# for i in y:
#     sp.pprint(i[0])
#     sp.pprint(i[1])
#     print()