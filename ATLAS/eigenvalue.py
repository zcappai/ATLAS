import sympy as sp
from determinant import naiveDeterminant
# from latex2image import formula_as_file
from text2image import toImage, formula_as_file
from emptyimg import empty


class Eigenvalue:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = matrix.rows
        self.saved = []
        self.text = []
    
    def calc(self):
        names = 1
        I = sp.eye(self.size)
        lamda = sp.Symbol('lamda')
        lamda_I = lamda*I
        new_matrix = self.matrix - lamda_I
        self.text.append((names, "First, subtract λ multiplied by the identity matrix from the matrix"))
        names += 1
        self.saved.append((names, sp.latex(self.matrix)+str('-')+sp.latex(lamda)+sp.latex(I)))
        names += 1
        self.text.append((names, "To form the following matrix"))
        names += 1
        self.saved.append((names, sp.latex(new_matrix)))
        names += 1
        self.text.append((names, "Then, calculate the determinant of this matrix and equate it to 0"))
        names += 1
        characteristic = naiveDeterminant(new_matrix).calc()
        self.text.append((names, "Giving the following equation"))
        names += 1
        self.saved.append((names, sp.latex(characteristic)+"=0"))
        names += 1
        self.text.append((names, "This equation can be simplified to the following equation"))
        names += 1
        expanded_det = sp.expand(characteristic)
        # print(expanded_det)
        self.saved.append((names, sp.latex(expanded_det)+"=0"))
        names += 1
        solved_lamda = sp.roots(expanded_det, lamda)
        # print(solved_lamda)
        eigenvalues = []
        self.text.append((names, "Finally, solve this equation to get the eigenvalues"))
        names += 1
        for i in solved_lamda.items():
            # solution = i.evalf(chop=True)
            solution = i[0]
            amount = i[1]
            while amount > 0:
                eigenvalues.append(solution)
                amount -= 1
                self.saved.append((names, sp.latex(lamda)+"="+sp.latex(solution)))
                names += 1
        return eigenvalues

    def latex2img(self):
        formula_as_file(sp.latex(self.matrix), 0)
        for i in  self.saved:
            formula_as_file(i[1], i[0])
        for i in self.text:
            toImage(i[1], i[0])

# x = sp.Matrix([[1,1,1],[2,-3,4],[3,4,5]])
# x = sp.Matrix([[4/5, -3/5, 0],[3/5, 4/5, 0],[1, 2, 2]])
# sp.pprint(x)
# new = Eigenvalue(x)
# sp.pprint(new.calc())
# new.latex2img()