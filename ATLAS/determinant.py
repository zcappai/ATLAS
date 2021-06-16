import glob
import os
import sympy as sp
from latex2image import formula_as_file
from text2image import toImage

class naiveDeterminant:
    names = 0
    saved = []
    text = []
    def __init__(self, matrix, size):
        self.matrix = matrix
        self.size = size
        self.det = 0
    
    # Calculates the determinant of a matrix
    def calc(self):
        curr = []
        naiveDeterminant.saved.append((naiveDeterminant.names, self.matrix))
        naiveDeterminant.names += 1
        naiveDeterminant.text.append((naiveDeterminant.names, "Take the first row of the matrix"))
        naiveDeterminant.names += 1
        naiveDeterminant.saved.append((naiveDeterminant.names, self.matrix[0,:]))
        naiveDeterminant.names += 1
        naiveDeterminant.text.append((naiveDeterminant.names, "Take the minors of each element respectively"))
        naiveDeterminant.names += 1
        for i in range(self.size):
            curr_element = self.matrix[i]
            curr_submatrix = self.matrix.minor_submatrix(0, i)
            naiveDeterminant.saved.append((naiveDeterminant.names, curr_submatrix))
            naiveDeterminant.names += 1
            curr.append((curr_element, curr_submatrix))
        naiveDeterminant.text.append((naiveDeterminant.names, "To form the following expression"))
        naiveDeterminant.names += 1
        naiveDeterminant.saved.append((naiveDeterminant.names, curr))
        naiveDeterminant.names += 1
        neg_toggle = 0
        for i in range(self.size):
            if neg_toggle % 2 == 0:
                if self.size - 1 == 1:
                    # naiveDeterminant.text.append((naiveDeterminant.names, "Add "+str(curr[i][0])+str("x")+str(curr[i][1][0])+" to the determinant"))
                    # naiveDeterminant.names += 1
                    self.det += curr[i][0] * curr[i][1][0]
                else:
                    sub_det, ops = naiveDeterminant(curr[i][1], self.size - 1).calc()
                    naiveDeterminant.text.append((naiveDeterminant.names, "The determinant of the minor"))
                    naiveDeterminant.names += 1
                    naiveDeterminant.saved.append((naiveDeterminant.names, curr[i][1]))
                    naiveDeterminant.names += 1
                    naiveDeterminant.text.append((naiveDeterminant.names, "is"))
                    naiveDeterminant.names += 1
                    self.det += curr[i][0] * sub_det
                    naiveDeterminant.saved.append((naiveDeterminant.names, sub_det))
                    naiveDeterminant.names += 1
            elif neg_toggle % 2 == 1:
                if self.size - 1 == 1:
                    # naiveDeterminant.text.append((naiveDeterminant.names, "Subtract "+str(curr[i][0])+str("x")+str(curr[i][1][0])+" from the determinant"))
                    # naiveDeterminant.names += 1
                    self.det -= curr[i][0] * curr[i][1][0]
                else:
                    sub_det, ops = naiveDeterminant(curr[i][1], self.size - 1).calc()
                    naiveDeterminant.text.append((naiveDeterminant.names, "The determinant of the minor"))
                    naiveDeterminant.names += 1
                    naiveDeterminant.saved.append((naiveDeterminant.names, curr[i][1]))
                    naiveDeterminant.names += 1
                    naiveDeterminant.text.append((naiveDeterminant.names, "is"))
                    naiveDeterminant.names += 1
                    self.det -= curr[i][0] * sub_det
                    naiveDeterminant.saved.append((naiveDeterminant.names, sub_det))
                    naiveDeterminant.names += 1
            neg_toggle += 1
        self.final_det = (naiveDeterminant.names, self.det)
        return self.det, curr

    # Converts the matrices and expressions to images
    def latex2img(self):
        symb_toggle = 0
        for i in naiveDeterminant.saved:
            tex = ""
            expr = i[1]
            try:
                for j in expr:
                    for k in j:
                        tex += sp.latex(k)
                    if symb_toggle == 0:
                        tex += '-'
                        symb_toggle = 1
                    elif symb_toggle == 1:
                        tex += '+'
                        symb_toggle = 0
                symb_toggle = 0
                formula_as_file(tex[:-1], 'images/'+str(i[0])+'.png')
            except:
                formula_as_file(sp.latex(i[1]), 'images/'+str(i[0])+'.png')
        for i in naiveDeterminant.text:
            count = i[0]
            message = i[1]
            toImage(message, count)
        toImage("Therefore, the determinant of the matrix is", self.final_det[0])
        formula_as_file(str(self.final_det[1]), 'images/'+str(self.final_det[0]+1)+'.png')

# empty()
# a = sp.Matrix([[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]])
# det = naiveDeterminant(a, 4)
# det.calc()
# det.latex2img()