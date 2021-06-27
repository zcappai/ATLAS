from emptyimg import empty
import sympy as sp
# from latex2image import formula_as_file
from text2image import toImage, formula_as_file
from string import ascii_lowercase

class GaussianElimination:
    def __init__(self, matrix, equations, unknowns):
        self.matrix = matrix
        self.equations = equations
        self.unknowns = unknowns
        self.atoms = list(ascii_lowercase)
        for x in range(self.unknowns//26):
            self.atoms += ["".join([i, str(x)]) for i in list(ascii_lowercase)]
        self.saved = []
        self.text = []
    
    def calc(self):
        names = 0
        if self.equations < self.unknowns:
            message = "There are infinitely many solutions (or there are no solutions)"
            self.text.append((names, message))
            return False, message, None
        elif self.equations > self.unknowns:
            message = "There are no solutions (this is an overdetermined system)"
            self.text.append((names, message))
            return False, message, None
        else:
            ############################ REFACTOR
            n = self.unknowns
            a = self.matrix[:, :]
            x = [0]*n
            names += 1
            self.saved.append((names, sp.latex(a[:, :])))
            names += 1

            # Applying Gauss Elimination
            for i in range(n):
                # if a.row(i).col(i)[0] == 0.0:
                #     return False, "No solutions exists!", None
                
                for j in range(i+1, n):
                    ratio = a.row(j).col(i)[0]/a.row(i).col(i)[0]
                    if a.row(i).col(i)[0] != 0:
                        self.text.append((names, "The ratio between element "+str(i+1)+" of rows"))
                        names += 1
                        self.saved.append((names, sp.latex(a[:, :].row(j))))
                        names += 1
                        self.saved.append((names, sp.latex(a[:, :].row(i))))
                        names += 1
                        self.text.append((names, "Gives the ratio of"))
                        names += 1
                        self.saved.append((names, sp.latex(ratio)))
                        names += 1
                        self.text.append((names, "This ratio is substracted from row "+str(j+1)+" by multiplying the ratio by values from row "+str(i+1)))
                        names += 1
                        self.saved.append((names, sp.latex(a[:, :])))
                        names += 1
                        for k in range(n + 1):
                            a[j, k] -= ratio * a.row(i).col(k)[0]
                            self.saved.append((names, sp.latex(a[:, :])))
                            names += 1
            self.text.append((names, "The matrix is now in row echelon form"))
            names += 1
            self.text.append((names, "Back substitution is now required to calculate the variable values"))
            names += 1

            # Back Substitution
            symbols = self.atoms[:self.unknowns]
            x[n-1] = a.row(n-1).col(n)[0]/a.row(n-1).col(n-1)[0]
            if a.row(n-1).col(n-1)[0] == 0:
                x[n-1] = 1
            else:
                self.text.append((names, "Starting from the final row of the matrix, we calculate"))
                names += 1
                self.saved.append((names, str(symbols[-1])+"="+sp.latex(a.row(n-1).col(n)[0])+"/"+sp.latex(a.row(n-1).col(n-1)[0])+"="+str(x[n-1])))
                names += 1
            for i in range(n-2,-1,-1):
                zeroed = False
                for zero in a.row(i):
                    if zero != 0:
                        zeroed = True
                        break
                if zeroed == True:
                    self.text.append((names, "For the next variable, the constant is"))
                    names += 1
                    x[i] = a.row(i).col(n)[0]
                    self.saved.append((names, str(x[i])))
                    names += 1
                    self.text.append((names, "Subtract the coefficient of the known variables multiplied by the known variables, respectively"))
                    names += 1
                    for j in range(i+1,n):
                        self.saved.append((names, str(x[i])+"-"+str(a.row(i).col(j)[0])+"*"+str(x[j])+"="+str(x[i] - a.row(i).col(j)[0]*x[j])))
                        names += 1
                        x[i] = x[i] - a.row(i).col(j)[0]*x[j]
                    self.text.append((names, "Then divide by the coefficient of the variable in question"))
                    names += 1
                    self.saved.append((names, str(symbols[i])+"="+str(x[i])+"/"+str(a.row(i).col(i)[0])+"="+str(x[i]/a.row(i).col(i)[0])))
                    names += 1
                    x[i] = x[i]/a.row(i).col(i)[0]
                elif zeroed == False:
                    x[i] = 1

            # Displaying solution
            # message = ""
            # for i in range(self.equations):
            #     message += "{} = {}, ".format(symbols[i],x[i])

            self.text.append((names, "The solutions to the system of linear equations"))
            names += 1
            original_constants = self.matrix[:, :].col(-1)
            self.matrix.col_del(-1)
            self.saved.append((names, sp.latex(self.matrix)+sp.latex(sp.Matrix(self.unknowns, 1, symbols))+"="+sp.latex(original_constants)))
            names += 1
            self.text.append((names, "are"))
            names += 1
            self.saved.append((names, x))
            names += 1
            return True, x, a

    def latex2img(self):
        for i in self.saved:
            formula_as_file(i[1], i[0]) ######################
        for i in self.text:
            toImage(i[1], i[0]) ######################

# empty()
# x = sp.Matrix([[1,1,1,9],[2,-3,4,13],[3,4,5,40]])

# x = sp.Matrix([[0,0,0,0],[0,2,5,0],[0,4,1,0]])
# x = sp.Matrix([[3,0,0,0],[0,5,5,0],[0,4,4,0]])
# x = sp.Matrix([[-6,0,0,0],[0,-4,5,0],[0,4,-5,0]])
# new = GaussianElimination(x, 3, 3)
# sp.pprint(new.calc())
# new.latex2img()