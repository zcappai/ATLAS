import sympy as sp
from determinant import naiveDeterminant
from latex2image import formula_as_file
from text2image import toImage
from emptyimg import empty


class Eigenvalue:
    saved = []
    text = []
    def __init__(self, matrix, size):
        self.matrix = matrix
        self.size = size
    
    def calc(self):
        names = 1
        I = sp.eye(self.size)
        lamda = sp.Symbol('lamda')
        lamda_I = lamda*I
        new_matrix = self.matrix - lamda_I
        Eigenvalue.text.append((names, "First, subtract λ multiplied by the identity matrix from the matrix"))
        names += 1
        Eigenvalue.saved.append((names, sp.latex(self.matrix)+str('-')+sp.latex(lamda)+sp.latex(I)))
        names += 1
        Eigenvalue.text.append((names, "To form the following matrix"))
        names += 1
        Eigenvalue.saved.append((names, sp.latex(new_matrix)))
        names += 1
        Eigenvalue.text.append((names, "Then, calculate the determinant of this matrix and equate it to 0"))
        names += 1
        determinant, _ = naiveDeterminant(new_matrix, self.size).calc()
        Eigenvalue.text.append((names, "Giving the following equation"))
        names += 1
        Eigenvalue.saved.append((names, sp.latex(determinant)+"=0"))
        names += 1
        Eigenvalue.text.append((names, "This equation can be simplified to the following equation"))
        names += 1
        expanded_det = sp.expand(determinant)
        Eigenvalue.saved.append((names, sp.latex(expanded_det)+"=0"))
        names += 1
        solved_lamda = sp.solve(expanded_det, lamda)
        solutions = []
        Eigenvalue.text.append((names, "Finally, solve this equation to get the eigenvalues"))
        names += 1
        for i in solved_lamda:
            solution = i.evalf(chop=True)
            solutions.append(solution)
            Eigenvalue.saved.append((names, sp.latex(lamda)+"="+sp.latex(solution)))
            names += 1
        return solutions

    def latex2img(self):
        formula_as_file(sp.latex(self.matrix), 'images/0.png')
        for i in  Eigenvalue.saved:
            formula_as_file(i[1], 'images/'+str(i[0])+'.png')
        for i in Eigenvalue.text:
            toImage(i[1], i[0])

# x = sp.Matrix([[1,1,1],[2,-3,4],[3,4,5]])
# sp.pprint(x)
# new = Eigenvalue(x, 3)
# sp.pprint(new.calc())
# new.latex2img()