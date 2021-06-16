from os import name
import sympy as sp
from latex2image import formula_as_file
from emptyimg import empty
from text2image import toImage

class naiveMultiplication:
    saved = []
    text = []
    def __init__(self, leftdim, rightdim, shareddim, leftmatrix, rightmatrix):
        self.leftmatrix = leftmatrix
        self.rightmatrix = rightmatrix
        self.leftdim = leftdim
        self.rightdim = rightdim
        self.shareddim = shareddim
    
    def calc(self):
        res = sp.Matrix([[0 for x in range(self.rightdim)] for y in range (self.leftdim)])
        names = 1
        for i in range(self.leftdim):
            for j in range(self.rightdim):
                res[i, j] = 0
                for x in range(self.shareddim):
                    naiveMultiplication.text.append((names, "The resultant matrix so far is"))
                    names += 1
                    naiveMultiplication.saved.append((names, sp.latex(sp.Matrix(res))))
                    names += 1
                    naiveMultiplication.text.append((names, "L({},{}) * R({},{}) is".format(i,x,x,j)))
                    names += 1
                    res[i, j] += (self.leftmatrix.row(i).col(x)[0] * self.rightmatrix.row(x).col(j)[0])
                    naiveMultiplication.saved.append((names, sp.latex(self.leftmatrix.row(i).col(x)[0])+"*"+sp.latex(self.rightmatrix.row(x).col(j)[0])))
                    names += 1
                    naiveMultiplication.text.append((names, "This is added to ({},{}) in the resultant matrix".format(i,j)))
                    names += 1
        naiveMultiplication.text.append((names, "The final matrix is"))
        names += 1
        naiveMultiplication.saved.append((names, sp.latex(res)))
        names += 1

    def latex2img(self):
        original = "L="+sp.latex(sp.Matrix(self.leftmatrix))+" * "+"R="+sp.latex(sp.Matrix(self.rightmatrix))
        formula_as_file(original, 'images/0.png')
        for i in naiveMultiplication.saved:
            formula_as_file(i[1], 'images/'+str(i[0])+'.png')
        for i in naiveMultiplication.text:
            toImage(i[1], i[0])

# empty()
# a = sp.Matrix([[1,2,3],[4,5,6]])
# b = sp.Matrix([[1,5],[2,7],[3,2]])
# x = naiveMultiplication(2, 2, 3, a, b)
# sp.pprint(a)
# sp.pprint(b)
# x.calc()
# x.latex2img()