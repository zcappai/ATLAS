from emptyimg import empty
import sympy as sp
# from latex2image import formula_as_file
from text2image import toImage, formula_as_file
from string import ascii_lowercase

class GaussianElimination:
    def __init__(self, matrix):
        self.matrix = matrix
        self.equations = matrix.rows
        self.unknowns = matrix.cols - 1
        self.atoms = list(ascii_lowercase)
        for x in range(self.unknowns//26):
            self.atoms += ["".join([i, str(x)]) for i in list(ascii_lowercase)]
        self.saved = []
        self.text = []

    def latex2img(self):
        for i in self.saved:
            formula_as_file(i[1], i[0]) ######################
        for i in self.text:
            toImage(i[1], i[0]) ######################

    def calc(self):
        names = 0
        if self.equations < self.unknowns:
            message = "There are infinitely many solutions (or there are no solutions)"
            self.text.append((names, message))
            return False, [], None
        elif self.equations > self.unknowns:
            message = "There are no solutions (this is an overdetermined system)"
            self.text.append((names, message))
            return False, [], None
        else:
            # Applying Rouché–Capelli theorem
            aug = self.matrix[:, :]
            coef = self.matrix[:, :]
            self.text.append((names, "Rouch\'e–Capelli theorem is used to identify inconsistent systems"))
            names += 1
            self.text.append((names, "This is done by comparing the ranks of the augmented and coefficient matrices"))
            names += 1
            coef.col_del(self.unknowns)
            self.text.append((names, "The augmented matrix rank is {}".format(aug.rank())))
            names += 1
            self.text.append((names, "The coefficient matrix rank is {}".format(coef.rank())))
            names += 1
            if aug.rank() > coef.rank():
                self.text.append((names, "Therefore, the system of linear equations is inconsistent and no solutions exist"))
                names += 1
                return False, [], None
            self.text.append((names, "Therefore, the system of linear equations is consistent"))
            names += 1

            ## REFACTOR!!!!!!!
            n = self.equations
            for i in range(0, n):
                # Search for maximum in this column
                maxEl = abs(self.matrix.row(i).col(i)[0])
                maxRow = i
                for k in range(i + 1, n):
                    if abs(self.matrix.row(k).col(i)[0]) > maxEl:
                        maxEl = abs(self.matrix.row(k).col(i)[0])
                        maxRow = k

                # Swap maximum row with current row (column by column)
                self.matrix.row_swap(maxRow, i)
                # Make all rows below this one 0 in current column
                for k in range(i + 1, n):
                    c = self.matrix.row(k).col(i)[0] / self.matrix.row(i).col(i)[0]
                    if c == sp.nan:
                        pass
                    else:
                        self.matrix.row_op(k, lambda a, j: a - c*self.matrix[i, j])
            row_ech = self.matrix[:, :]
            # sp.pprint(self.matrix)
            # Solve equation Ax=b for an upper triangular matrix A
            x = [0 for i in range(n)]
            for i in range(n - 1, -1, -1):
                x[i] = self.matrix.row(i).col(n)[0] / self.matrix.row(i).col(i)[0]
                if x[i] == sp.nan: #####################################################
                    x[i] = 1
                for k in range(i - 1, -1, -1):
                    self.matrix[k, n] -= self.matrix.row(k).col(i)[0] * x[i]

            return True, x, row_ech

# empty()
# x = sp.Matrix([[1,1,1,9],[2,-3,4,13],[3,4,5,40]])
# x = sp.Matrix([[0, 0, 0, 0],[1, 0, 1, 0],[-1, 0, -1, 0]])
# sp.pprint(x)
# new = GaussianElimination(x)
# sp.pprint(new.calc())
# new.latex2img()
    
    # def calc(self):
    #     names = 0
    #     if self.equations < self.unknowns:
    #         message = "There are infinitely many solutions (or there are no solutions)"
    #         self.text.append((names, message))
    #         return False, [], None
    #     elif self.equations > self.unknowns:
    #         message = "There are no solutions (this is an overdetermined system)"
    #         self.text.append((names, message))
    #         return False, [], None
    #     else:
    #         ############################ REFACTOR
    #         n = self.unknowns
    #         a = self.matrix[:, :]
    #         x = [0]*n
    #         names += 1
    #         self.saved.append((names, sp.latex(a[:, :])))
    #         names += 1

    #         # Applying Rouché–Capelli theorem
    #         aug = a[:, :]
    #         coef = a[:, :]
    #         self.text.append((names, "Rouch\'e–Capelli theorem is used to identify inconsistent systems"))
    #         names += 1
    #         self.text.append((names, "This is done by comparing the ranks of the augmented and coefficient matrices"))
    #         names += 1
    #         coef.col_del(self.unknowns)
    #         self.text.append((names, "The augmented matrix rank is {}".format(aug.rank())))
    #         names += 1
    #         self.text.append((names, "The coefficient matrix rank is {}".format(coef.rank())))
    #         names += 1
    #         if aug.rank() > coef.rank():
    #             self.text.append((names, "Therefore, the system of linear equations is inconsistent and no solutions exist"))
    #             names += 1
    #             return False, [], None
    #         self.text.append((names, "Therefore, the system of linear equations is consistent"))
    #         names += 1

    #         # Applying Gauss Elimination
    #         for i in range(n):
    #             # if a.row(i).col(i)[0] == 0.0:
    #             #     return False, "No solutions exists!", None
    #             sp.pprint(a)
    #             for j in range(i+1, n):
    #                 print(a.row(j).col(i), a.row(i).col(i))
    #                 ratio = a.row(j).col(i)[0]/a.row(i).col(i)[0]
    #                 print(ratio)
    #                 if a.row(i).col(i)[0] != 0:
    #                     self.text.append((names, "The ratio between element "+str(i+1)+" of rows"))
    #                     names += 1
    #                     self.saved.append((names, sp.latex(a[:, :].row(j))))
    #                     names += 1
    #                     self.saved.append((names, sp.latex(a[:, :].row(i))))
    #                     names += 1
    #                     self.text.append((names, "Gives the ratio of"))
    #                     names += 1
    #                     self.saved.append((names, sp.latex(ratio)))
    #                     names += 1
    #                     self.text.append((names, "This ratio is substracted from row "+str(j+1)+" by multiplying the ratio by values from row "+str(i+1)))
    #                     names += 1
    #                     self.saved.append((names, sp.latex(a[:, :])))
    #                     names += 1
    #                     for k in range(n + 1):
    #                         a[j, k] -= ratio * a.row(i).col(k)[0]
    #                         sp.pprint(a)
    #                         self.saved.append((names, sp.latex(a[:, :])))
    #                         names += 1
    #                     print()
    #         self.text.append((names, "The matrix is now in row echelon form"))
    #         names += 1
    #         self.text.append((names, "Back substitution is now required to calculate the variable values"))
    #         names += 1

    #         # Back Substitution
    #         symbols = self.atoms[:self.unknowns]
    #         x[n-1] = a.row(n-1).col(n)[0]/a.row(n-1).col(n-1)[0]
    #         if a.row(n-1).col(n-1)[0] == 0:
    #             x[n-1] = 1
    #         else:
    #             self.text.append((names, "Starting from the final row of the matrix, we calculate"))
    #             names += 1
    #             self.saved.append((names, str(symbols[-1])+"="+sp.latex(a.row(n-1).col(n)[0])+"/"+sp.latex(a.row(n-1).col(n-1)[0])+"="+str(x[n-1])))
    #             names += 1
    #         for i in range(n-2,-1,-1):
    #             zeroed = False
    #             for zero in a.row(i):
    #                 if zero != 0:
    #                     zeroed = True
    #                     break
    #             if zeroed == True:
    #                 self.text.append((names, "For the next variable, the constant is"))
    #                 names += 1
    #                 x[i] = a.row(i).col(n)[0]
    #                 self.saved.append((names, str(x[i])))
    #                 names += 1
    #                 self.text.append((names, "Subtract the coefficient of the known variables multiplied by the known variables, respectively"))
    #                 names += 1
    #                 for j in range(i+1,n):
    #                     self.saved.append((names, str(x[i])+"-"+str(a.row(i).col(j)[0])+"*"+str(x[j])+"="+str(x[i] - a.row(i).col(j)[0]*x[j])))
    #                     names += 1
    #                     x[i] = x[i] - a.row(i).col(j)[0]*x[j]
    #                 self.text.append((names, "Then divide by the coefficient of the variable in question"))
    #                 names += 1
    #                 self.saved.append((names, str(symbols[i])+"="+str(x[i])+"/"+str(a.row(i).col(i)[0])+"="+str(x[i]/a.row(i).col(i)[0])))
    #                 names += 1
    #                 x[i] = x[i]/a.row(i).col(i)[0]
    #             elif zeroed == False:
    #                 x[i] = 1

    #         # Displaying solution
    #         # message = ""
    #         # for i in range(self.equations):
    #         #     message += "{} = {}, ".format(symbols[i],x[i])

    #         self.text.append((names, "The solutions to the system of linear equations"))
    #         names += 1
    #         original_constants = self.matrix[:, :].col(-1)
    #         self.matrix.col_del(-1)
    #         self.saved.append((names, sp.latex(self.matrix)+sp.latex(sp.Matrix(self.unknowns, 1, symbols))+"="+sp.latex(original_constants)))
    #         names += 1
    #         self.text.append((names, "are"))
    #         names += 1
    #         self.saved.append((names, x))
    #         names += 1
    #         return True, x, a