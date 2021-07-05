import sympy as sp
from text2image import toImage, formula_as_file
from emptyimg import empty

class naiveDeterminant:
    names = 0
    saved = []
    text = []
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = self.matrix.rows
        self.det = 0
    
    # Calculates the determinant of a matrix
    def calc(self):
        curr = []
        naiveDeterminant.saved.append((naiveDeterminant.names, self.matrix))
        naiveDeterminant.names += 1
        if self.size == 0:
            naiveDeterminant.text.append((naiveDeterminant.names, "A matrix of size 0 has a determinant of 1"))
            naiveDeterminant.names += 1
            self.det = 1
            self.final_det = (naiveDeterminant.names, self.det)
            return self.det
        elif self.size == 1:
            naiveDeterminant.saved.append((naiveDeterminant.names, self.matrix))
            naiveDeterminant.names += 1
            naiveDeterminant.text.append((naiveDeterminant.names, "A matrix of size 1 has a determinant equal to its only value"))
            naiveDeterminant.names += 1
            self.det = self.matrix[0]
            self.final_det = (naiveDeterminant.names, self.det)
            return self.det
        else:
            naiveDeterminant.text.append((naiveDeterminant.names, "Take the first row of the matrix"))
            naiveDeterminant.names += 1
            naiveDeterminant.saved.append((naiveDeterminant.names, self.matrix[0,:]))
            naiveDeterminant.names += 1
            naiveDeterminant.text.append((naiveDeterminant.names, "Take the minors of each element respectively"))
            naiveDeterminant.names += 1
            for i in range(self.size):
                curr_element = self.matrix[i]
                curr_submatrix = self.matrix.minor_submatrix(0, i)
                curr.append((curr_element, curr_submatrix))
                naiveDeterminant.saved.append((naiveDeterminant.names, curr_submatrix))
                naiveDeterminant.names += 1
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
                        sub_det = naiveDeterminant(curr[i][1]).calc()
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
                        sub_det = naiveDeterminant(curr[i][1]).calc()
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
            return self.det

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
                formula_as_file(tex[:-1], i[0])
            except:
                formula_as_file(sp.latex(i[1]), i[0])
        for i in naiveDeterminant.text:
            count = i[0]
            message = i[1]
            toImage(message, count)
        toImage("Therefore, the determinant of the matrix is", self.final_det[0])
        formula_as_file(str(self.final_det[1]), self.final_det[0]+1)

class Sarrus:
    def __init__(self, matrix):
        self.matrix = matrix
        self.saved = []
        self.text = []
        self.names = 0
    
    def calc(self):
        self.saved.append((self.names, sp.latex(self.matrix)))
        self.names += 1
        self.text.append((self.names, "First, multiply values along the leading diagonal"))
        self.names += 1
        R1 = self.matrix[0, 0] * self.matrix[1, 1] * self.matrix[2, 2]
        self.saved.append((self.names, "R_1="+sp.latex(self.matrix[0, 0])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 2])+"={}".format(R1)))
        self.names += 1
        R2 = self.matrix[1, 0] * self.matrix[2, 1] * self.matrix[0, 2]
        self.text.append((self.names, "Then, multiply values along the first diagonal below the leading diagonal"))
        self.names += 1
        self.text.append((self.names, "By assuming an identical matrix is below the original..."))
        self.names += 1
        self.text.append((self.names, "...so that the final element of the multiplication is the top-right element"))
        self.names += 1
        self.saved.append((self.names, "R_2="+sp.latex(self.matrix[1, 0])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 2])+"={}".format(R2)))
        self.names += 1
        R3 = self.matrix[2, 0] * self.matrix[0, 1] * self.matrix[1, 2]
        self.text.append((self.names, "Then, multiply values along the second diagonal below the leading diagonal"))
        self.names += 1
        self.text.append((self.names, "By making the same assumption as the previous multiplication"))
        self.names += 1
        self.saved.append((self.names, "R_3="+sp.latex(self.matrix[2, 0])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 2])+"={}".format(R3)))
        self.names += 1
        R = R1 + R2 + R3
        self.text.append((self.names, "Now, add together the products"))
        self.names += 1
        self.saved.append((self.names, "R=R_1+R_2+R_3="+sp.latex(R1)+"+"+sp.latex(R2)+"+"+sp.latex(R3)+"={}".format(R)))
        self.names += 1

        self.text.append((self.names, "Now do the same for the leftward diagonals, starting with the leading leftward diagonal"))
        self.names += 1
        L1 = self.matrix[0, 2] * self.matrix[1, 1] * self.matrix[2, 0]
        self.saved.append((self.names, "L_1="+sp.latex(self.matrix[0, 2])+"*"+sp.latex(self.matrix[1, 1])+"*"+sp.latex(self.matrix[2, 0])+"={}".format(L1)))
        self.names += 1
        L2 = self.matrix[1, 2] * self.matrix[2, 1] * self.matrix[0, 0]
        self.text.append((self.names, "Then, multiply values along the first diagonal below the leading leftward diagonal"))
        self.names += 1
        self.saved.append((self.names, "L_2="+sp.latex(self.matrix[1, 2])+"*"+sp.latex(self.matrix[2, 1])+"*"+sp.latex(self.matrix[0, 0])+"={}".format(L2)))
        self.names += 1
        L3 = self.matrix[2, 2] * self.matrix[0, 1] * self.matrix[1, 0]
        self.text.append((self.names, "Then, multiply values along the second diagonal below the leading leftwrad diagonal"))
        self.names += 1
        self.saved.append((self.names, "L_3="+sp.latex(self.matrix[2, 2])+"*"+sp.latex(self.matrix[0, 1])+"*"+sp.latex(self.matrix[1, 0])+"={}".format(L3)))
        self.names += 1
        L = L1 + L2 + L3
        self.text.append((self.names, "Now, add together the products"))
        self.names += 1
        self.saved.append((self.names, "L=L_1+L_2+L_3="+sp.latex(L1)+"+"+sp.latex(L2)+"+"+sp.latex(L3)+"={}".format(L)))
        self.names += 1

        det = R - L
        self.text.append((self.names, "Finally, subtract the sum of the left diagonal multiplications from the right diagonal multiplications"))
        self.names += 1
        self.saved.append((self.names, "det=R-L="+sp.latex(R)+"-"+sp.latex(L)+"={}".format(det)))
        self.names += 1
        return det

    # Converts the matrices and expressions to images
    def latex2img(self):
        for i in self.saved:
            formula_as_file(i[1], i[0])
        for i in self.text:
            toImage(i[1], i[0])
        toImage("Therefore, the determinant of the matrix is ", self.names)
        self.names += 1
        formula_as_file(str(self.det), self.names)

empty()
# a = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])
# a = sp.Matrix([[3,4,7],[6,5,1],[9,4,7]])
# det = Sarrus(a)
# print(det.calc())
# det.latex2img()