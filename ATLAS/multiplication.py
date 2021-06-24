import sympy as sp
# from latex2image import formula_as_file
from emptyimg import empty
from text2image import toImage, formula_as_file

class naiveMultiplication:
    def __init__(self, leftdim, rightdim, shareddim, leftmatrix, rightmatrix):
        self.leftmatrix = leftmatrix
        self.rightmatrix = rightmatrix
        self.leftdim = leftdim
        self.rightdim = rightdim
        self.shareddim = shareddim
        self.saved = []
        self.text = []
    
    def calc(self):
        res = sp.Matrix([[0 for x in range(self.rightdim)] for y in range (self.leftdim)])
        names = 1
        for i in range(self.leftdim):
            for j in range(self.rightdim):
                res[i, j] = 0
                for x in range(self.shareddim):
                    self.text.append((names, "The resultant matrix so far is"))
                    names += 1
                    self.saved.append((names, sp.latex(sp.Matrix(res))))
                    names += 1
                    self.text.append((names, "L({},{}) * R({},{}) is".format(i,x,x,j)))
                    names += 1
                    res[i, j] += (self.leftmatrix.row(i).col(x)[0] * self.rightmatrix.row(x).col(j)[0])
                    self.saved.append((names, sp.latex(self.leftmatrix.row(i).col(x)[0])+"*"+sp.latex(self.rightmatrix.row(x).col(j)[0])))
                    names += 1
                    self.text.append((names, "This is added to ({},{}) in the resultant matrix".format(i,j)))
                    names += 1
        self.text.append((names, "The final matrix is"))
        names += 1
        self.saved.append((names, sp.latex(res)))
        names += 1

    def latex2img(self):
        original = "L="+sp.latex(sp.Matrix(self.leftmatrix))+" * "+"R="+sp.latex(sp.Matrix(self.rightmatrix))
        formula_as_file(original, 'images/0.png')
        for i in self.saved:
            formula_as_file(i[1], 'images/'+str(i[0])+'.png')
        for i in self.text:
            toImage(i[1], i[0])

class Strassen:
    def __init__(self, leftmatrix, rightmatrix, size):
        self.leftmatrix = leftmatrix
        self.rightmatrix = rightmatrix
        self.size = size
        self.saved = []
        self.text = []
    
    def calc(self):
        if self.size % 2 == 0:
            sub_size = self.size // 2
            l_sub1 = self.leftmatrix[:sub_size, :sub_size] # top-left
            l_sub2 = self.leftmatrix[:sub_size, sub_size:] # top-right
            l_sub3 = self.leftmatrix[sub_size:, :sub_size] # bottom-left
            l_sub4 = self.leftmatrix[sub_size:, sub_size:] # bottom-right

            r_sub1 = self.rightmatrix[:sub_size, :sub_size] # top-left
            r_sub2 = self.rightmatrix[:sub_size, sub_size:] # top-right
            r_sub3 = self.rightmatrix[sub_size:, :sub_size] # bottom-left
            r_sub4 = self.rightmatrix[sub_size:, sub_size:] # bottom-right
            M1 = (l_sub1 + l_sub4)*(r_sub1 + r_sub4)
            M2 = (l_sub3 + l_sub4)*r_sub1
            M3 = None
            M4 = None
            M5 = None
            M6 = None
            M7 = None
        elif self.size % 2 == 1:
            pass

# empty()
a = sp.Matrix([[1,2,3,4],[4,5,6,6],[7,8,9,2],[7,6,9,4]])
# b = sp.Matrix([[1,5],[2,7],[3,2]])
# x = naiveMultiplication(2, 2, 3, a, b)
c = sp.Matrix([[1,2],[3,4]])
d = sp.Matrix([[3,4],[1,2]])
x = Strassen(a, d, 4)
x.calc()
# x.latex2img()