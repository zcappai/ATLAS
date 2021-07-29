import sympy as sp
from determinant import naiveDeterminant
from text2image import formula_as_file
from emptyimg import empty
import saver


class Eigenvalue:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []
        # self.text = []
    
    def calc(self):
        self.saved.append((saver.names, sp.latex(self.matrix)))
        saver.names += 1
        I = sp.eye(self.size)
        lamda = sp.Symbol('lamda')
        lamda_I = lamda*I
        new_matrix = self.matrix - lamda_I
        self.saved.append((saver.names, """\\text{First, subtract }\lambda\\text{ multiplied by}$$$$
        \\text{the identity matrix from the matrix}$$$$"""+sp.latex(self.matrix)+str('-')+sp.latex(lamda)+sp.latex(I)))
        saver.names += 1
        self.saved.append((saver.names, "\\text{This results in}$$$$"+sp.latex(new_matrix)))
        saver.names += 1
        characteristic = new_matrix.det()
        expanded_det = sp.expand(characteristic)
        self.saved.append((saver.names, """\\text{Then, calculate the determinant of this matrix}$$$$
        \\text{and equate it to 0, giving the following equation}$$$$"""+sp.latex(expanded_det)+"=0"))
        saver.names += 1
        solved_lamda = sp.roots(expanded_det, lamda)
        eigenvalues = []
        self.saved.append((saver.names, "\\text{Finally, solve this equation to get the eigenvalues.}"
        +"$$$$\\text{The method of solving the equation depends on the indices.}"
        +"$$$$\\text{Larger indices may require approximation of solutions.}"))
        saver.names += 1
        for i in solved_lamda.items():
            solution = i[0].evalf(chop=True)
            # solution = i[0]
            amount = i[1]
            while amount > 0:
                eigenvalues.append(solution)
                amount -= 1
                self.saved.append((saver.names, sp.latex(lamda)+"="+sp.latex(solution)))
                saver.names += 1
        return eigenvalues

    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved
            # saver.text = saver.text + self.text

    def latex2img(self):
        for i in saver.saved:
            formula_as_file(i[1], i[0])
        # for i in saver.text:
        #     toImage(i[1], i[0])

# empty()
# x = sp.Matrix([[1,1,1],[2,-3,4],[3,4,5]])
# x = sp.Matrix([[1,1,0],[1,0,1],[0,1,1]])
# x = sp.Matrix([[4/5, -3/5, 0],[3/5, 4/5, 0],[1, 2, 2]])
# sp.pprint(x)
# new = Eigenvalue(x)
# sp.pprint(new.calc())
# new.addSaved(True)
# new.latex2img()