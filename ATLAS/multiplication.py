import sympy as sp
from emptyimg import empty
import text2image
import compare_text2image

saved = []
text = []
names = 0

class naiveMultiplication:
    def __init__(self, leftmatrix, rightmatrix):
        self.leftmatrix = leftmatrix
        self.rightmatrix = rightmatrix
        self.leftdim = leftmatrix.rows
        self.rightdim = rightmatrix.cols
        self.shareddim = leftmatrix.cols
    
    def calc(self):
        global names
        original = "L="+sp.latex(sp.Matrix(self.leftmatrix))+" * "+"R="+sp.latex(sp.Matrix(self.rightmatrix))
        saved.append((names, original))
        names += 1
        res = sp.Matrix([[0 for x in range(self.rightdim)] for y in range (self.leftdim)])
        for i in range(self.leftdim):
            for j in range(self.rightdim):
                res[i, j] = 0
                for x in range(self.shareddim):
                    text.append((names, "The resultant matrix so far is"))
                    names += 1
                    saved.append((names, sp.latex(sp.Matrix(res))))
                    names += 1
                    text.append((names, "L({},{}) * R({},{}) is".format(i,x,x,j)))
                    names += 1
                    res[i, j] += (self.leftmatrix.row(i).col(x)[0] * self.rightmatrix.row(x).col(j)[0])
                    saved.append((names, sp.latex(self.leftmatrix.row(i).col(x)[0])+"*"+sp.latex(self.rightmatrix.row(x).col(j)[0])))
                    names += 1
                    text.append((names, "This is added to ({},{}) in the resultant matrix".format(i,j)))
                    names += 1
        text.append((names, "The final matrix is"))
        names += 1
        saved.append((names, sp.latex(res)))
        names += 1
        return res

    def latex2img(self):
        global names
        global saved
        global text
        names = 0
        for i in saved:
            text2image.formula_as_file(i[1], i[0])
        for i in text:
            text2image.toImage(i[1], i[0])
        saved = []
        text = []

    def compare_latex2img(self, subfolder):
        global names
        global saved
        global text
        names = 0
        for i in saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder)
        for i in text:
            compare_text2image.toImage(i[1], i[0], subfolder)
        saved = []
        text = []

class Strassen:
    global saved
    global text
    def __init__(self, leftmatrix, rightmatrix):
        self.leftmatrix = leftmatrix
        self.rightmatrix = rightmatrix
    
    def calc(self):
        final_rows = self.leftmatrix.rows
        final_cols = self.rightmatrix.cols
        global names
        original = "L="+sp.latex(self.leftmatrix)+" * "+"R="+sp.latex(self.rightmatrix)
        saved.append((names, original))
        names += 1
        if self.leftmatrix.rows == 0 or self.rightmatrix.rows == 0:
            text.append((names, "Multiplying any matrix by an empty matrix results in an empty matrix"))
            names += 1
            saved.append((names, "[]"))
            names += 1
            return sp.Matrix([])
        # Dynamic padding
        if self.leftmatrix.rows % 2 == 1:
            text.append((names, "The left matrix is padded with a row of zeroes for an even number of rows, as follows"))
            names += 1
            self.leftmatrix = self.leftmatrix.col_join(sp.zeros(1, self.leftmatrix.cols))
            saved.append((names, sp.latex(self.leftmatrix)))
            names += 1
        if self.leftmatrix.cols % 2 == 1:
            text.append((names, "The left matrix is padded with a column of zeroes for an even number of columns, as follows"))
            names += 1
            self.leftmatrix = self.leftmatrix.row_join(sp.zeros(self.leftmatrix.rows, 1))
            saved.append((names, sp.latex(self.leftmatrix)))
            names += 1
        if self.rightmatrix.cols % 2 == 1:
            text.append((names, "The right matrix is padded with a column of zeroes for an even number of columns, as follows"))
            names += 1
            self.rightmatrix = self.rightmatrix.row_join(sp.zeros(self.rightmatrix.rows, 1))
            saved.append((names, sp.latex(self.rightmatrix)))
            names += 1
        if self.rightmatrix.rows % 2 == 1:
            text.append((names, "The right matrix is padded with a row of zeroes for an even number of rows, as follows"))
            names += 1
            self.rightmatrix = self.rightmatrix.col_join(sp.zeros(1, self.rightmatrix.cols))
            saved.append((names, sp.latex(self.rightmatrix)))
            names += 1

        text.append((names, "The halfway points are calculated as dimensions for submatrices"))
        names += 1
        # Submatrix dimensions
        l_row_half = (self.leftmatrix.rows) // 2
        l_col_half = (self.leftmatrix.cols) // 2
        r_row_half = (self.rightmatrix.rows) // 2
        r_col_half = (self.rightmatrix.cols) // 2

        # Split matrices into quarters
        # Left matrix
        a11 = self.leftmatrix[:l_row_half, :l_col_half] # top-left
        a12 = self.leftmatrix[:l_row_half, l_col_half:] # top-right
        a21 = self.leftmatrix[l_row_half:, :l_col_half] # bottom-left
        a22 = self.leftmatrix[l_row_half:, l_col_half:] # bottom-right
        text.append((names, "This produces the following submatrices for the left matrix"))
        names += 1
        saved.append((names, "a_{1,1}="+sp.latex(a11)+",a_{1,2}="+sp.latex(a12)+",a_{2,1}="+sp.latex(a21)+",a_{2,2}="+sp.latex(a22)))
        names += 1

        # Right matrix
        b11 = self.rightmatrix[:r_row_half, :r_col_half] # top-left
        b12 = self.rightmatrix[:r_row_half, r_col_half:] # top-right
        b21 = self.rightmatrix[r_row_half:, :r_col_half] # bottom-left
        b22 = self.rightmatrix[r_row_half:, r_col_half:] # bottom-right
        text.append((names, "and the following submatrices for the right matrix"))
        names += 1
        saved.append((names, "b_{1,1}="+sp.latex(b11)+",b_{1,2}="+sp.latex(b12)+",b_{2,1}="+sp.latex(b21)+",b_{2,2}="+sp.latex(b22)))
        names += 1

        # Multiplying submatrices if one has dimension equal to 1
        if l_row_half == 1 or l_col_half == 1 or r_row_half == 1 or r_col_half == 1:
            text.append((names, "The dimension of a submatrix is 1, so the submatrices will be multiplied using the standard method"))
            names += 1
            saved.append((names, "m_1=(a_{1,1}+a_{2,2})(b_{1,1}+b_{2,2})=("+sp.latex(a11)+"+"+sp.latex(a22)+")("+sp.latex(b11)+"+"+sp.latex(b22)+")"))
            names += 1
            m1 = naiveMultiplication((a11 + a22), (b11 + b22)).calc()
            saved.append((names, "m_1="+sp.latex(m1)))
            names += 1
            saved.append((names, "m_2=(a_{2,1}+a_{2,2})b_{1,1}=("+sp.latex(a21)+"+"+sp.latex(a22)+")"+sp.latex(b11)))
            names += 1
            m2 = naiveMultiplication((a21 + a22), b11).calc()
            saved.append((names, "m_2="+sp.latex(m2)))
            names += 1
            saved.append((names, "m_3=a_{1,1}(b_{1,2}-b_{2,2})="+sp.latex(a11)+"("+sp.latex(b12)+"-"+sp.latex(b22)+")"))
            names += 1
            m3 = naiveMultiplication(a11, (b12 - b22)).calc()
            saved.append((names, "m_3="+sp.latex(m3)))
            names += 1
            saved.append((names, "m_4=a_{2,2}(b_{2,1}-b_{1,1})="+sp.latex(a22)+"("+sp.latex(b21)+"-"+sp.latex(b11)+")"))
            names += 1
            m4 = naiveMultiplication(a22, (b21 - b11)).calc()
            saved.append((names, "m_4="+sp.latex(m4)))
            names += 1
            saved.append((names, "m_5=(a_{1,1}+a_{1,2})b_{2,2}=("+sp.latex(a11)+"+"+sp.latex(a12)+")"+sp.latex(b22)))
            names += 1
            m5 = naiveMultiplication((a11 + a12), b22).calc()
            saved.append((names, "m_5="+sp.latex(m5)))
            names += 1
            saved.append((names, "m_6=(a_{2,1}-a_{1,1})(b_{1,1}+b_{1,2})=("+sp.latex(a21)+"-"+sp.latex(a11)+")("+sp.latex(b11)+"+"+sp.latex(b12)+")"))
            names += 1
            m6 = naiveMultiplication((a21 - a11), (b11 + b12)).calc()
            saved.append((names, "m_6="+sp.latex(m6)))
            names += 1
            saved.append((names, "m_7=(a_{1,2}-a_{2,2})(b_{2,1}+b_{2,2})=("+sp.latex(a12)+"-"+sp.latex(a22)+")("+sp.latex(b21)+"+"+sp.latex(b22)+")"))
            names += 1
            m7 = naiveMultiplication((a12 - a22), (b21 + b22)).calc()
            saved.append((names, "m_7="+sp.latex(m7)))
            names += 1
        # Otherwise, Strassen's called
        else:
            text.append((names, "No submatrices have a dimension of 1, therefore Strassen's method is applied once again"))
            names += 1
            saved.append((names, "m_1=(a_{1,1}+a_{2,2})(b_{1,1}+b_{2,2})=("+sp.latex(a11)+"+"+sp.latex(a22)+")("+sp.latex(b11)+"+"+sp.latex(b22)+")"))
            names += 1
            m1 = Strassen((a11 + a22), (b11 + b22)).calc()
            saved.append((names, "m_2=(a_{2,1}+a_{2,2})b_{1,1}=("+sp.latex(a21)+"+"+sp.latex(a22)+")"+sp.latex(b11)))
            names += 1
            m2 = Strassen((a21 + a22), b11).calc()
            saved.append((names, "m_3=a_{1,1}(b_{1,2}-b_{2,2})="+sp.latex(a11)+"("+sp.latex(b12)+"-"+sp.latex(b22)+")"))
            names += 1
            m3 = Strassen(a11, (b12 - b22)).calc()
            saved.append((names, "m_4=a_{2,2}(b_{2,1}-b_{1,1})="+sp.latex(a22)+"("+sp.latex(b21)+"-"+sp.latex(b11)+")"))
            names += 1
            m4 = Strassen(a22, (b21 - b11)).calc()
            saved.append((names, "m_5=(a_{1,1}+a_{1,2})b_{2,2}=("+sp.latex(a11)+"+"+sp.latex(a12)+")"+sp.latex(b22)))
            names += 1
            m5 = Strassen((a11 + a12), b22).calc()
            saved.append((names, "m_6=(a_{2,1}-a_{1,1})(b_{1,1}+b_{1,2})=("+sp.latex(a21)+"-"+sp.latex(a11)+")("+sp.latex(b11)+"+"+sp.latex(b12)+")"))
            names += 1
            m6 = Strassen((a21 - a11), (b11 + b12)).calc()
            saved.append((names, "m_7=(a_{1,2}-a_{2,2})(b_{2,1}+b_{2,2})=("+sp.latex(a12)+"-"+sp.latex(a22)+")("+sp.latex(b21)+"+"+sp.latex(b22)+")"))
            names += 1
            m7 = Strassen((a12 - a22), (b21 + b22)).calc()
        text.append((names, "The result of multiplication is therefore"))
        names += 1
        saved.append((names, "m_1="+sp.latex(m1)+",m_2="+sp.latex(m2)+",m_3="+sp.latex(m3)))
        names += 1
        saved.append((names, "m_4="+sp.latex(m4)+",m_5="+sp.latex(m5)+",m_6="+sp.latex(m6)))
        names += 1
        saved.append((names, "m_7="+sp.latex(m7)))
        names += 1

        # Calculating final matrix elements
        c11 = m1 + m4 - m5 + m7
        c12 = m3 + m5
        c21 = m2 + m4
        c22 = m1 - m2 + m3 + m6
        text.append((names, "These submatrices can be added and subtracted to produce the elements of the final matrix"))
        names += 1
        saved.append((names, "c_{1,1}=m_1 + m_4 - m_5 + m_7="+sp.latex(c11)))
        names += 1
        saved.append((names, "c_{1,2}=m_3 + m_5="+sp.latex(c12)))
        names += 1
        saved.append((names, "c_{2,1}=m_2 + m_4="+sp.latex(c21)))
        names += 1
        saved.append((names, "c_{2,2}=m_1 - m_2 + m_3 + m_6="+sp.latex(c22)))
        names += 1

        # Joining submatrices to form final matrices
        top_half = c11.row_join(c12)
        bottom_half = c21.row_join(c22)
        final_matrix = top_half.col_join(bottom_half)
        text.append((names, "These can be joined together to produce the following matrix"))
        names += 1
        saved.append((names, sp.latex(final_matrix)))
        names += 1

        # Removing dynamic padding
        if final_matrix.cols != final_cols:
            final_matrix.col_del(final_matrix.cols - 1)
        if final_matrix.rows != final_rows:
            final_matrix.row_del(final_matrix.rows - 1)
        text.append((names, "If there is padding, it is removed to produce the resultant matrix"))
        names += 1
        saved.append((names, sp.latex(final_matrix)))
        names += 1

        return final_matrix
    
    def latex2img(self):
        global names
        global saved
        global text
        names = 0
        for i in saved:
            text2image.formula_as_file(i[1], i[0])
        for i in text:
            text2image.toImage(i[1], i[0])
        saved = []
        text = []

    def compare_latex2img(self, subfolder):
        global names
        global saved
        global text
        names = 0
        for i in saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder)
        for i in text:
            compare_text2image.toImage(i[1], i[0], subfolder)
        saved = []
        text = []

class Laderman:
    global saved
    global text
    def __init__(self, leftmatrix, rightmatrix):
        self.leftmatrix = leftmatrix
        self.rightmatrix = rightmatrix

    def calc(self):
        global names
        l_rows = self.leftmatrix.rows
        l_cols = self.leftmatrix.cols
        r_rows = self.rightmatrix.rows
        r_cols = self.rightmatrix.cols
        original = "L="+sp.latex(self.leftmatrix)+" * "+"R="+sp.latex(self.rightmatrix)
        saved.append((names, original))
        names += 1
        if l_cols != 3 or l_rows != 3 or r_cols != 3 or r_rows != 3:
            text.append((names, "Laderman method only multiplies 3x3 matrices, so it is not compatible"))
            names += 1
            return []
        else:
            a11 = self.leftmatrix[0, 0]
            a12 = self.leftmatrix[0, 1]
            a13 = self.leftmatrix[0, 2]
            a21 = self.leftmatrix[1, 0]
            a22 = self.leftmatrix[1, 1]
            a23 = self.leftmatrix[1, 2]
            a31 = self.leftmatrix[2, 0]
            a32 = self.leftmatrix[2, 1]
            a33 = self.leftmatrix[2, 2]

            b11 = self.rightmatrix[0, 0]
            b12 = self.rightmatrix[0, 1]
            b13 = self.rightmatrix[0, 2]
            b21 = self.rightmatrix[1, 0]
            b22 = self.rightmatrix[1, 1]
            b23 = self.rightmatrix[1, 2]
            b31 = self.rightmatrix[2, 0]
            b32 = self.rightmatrix[2, 1]
            b33 = self.rightmatrix[2, 2]

            text.append((names, "Now, the following multiplications are calculated"))
            names += 1
            m1 = (a11 + a12 + a13 - a21 - a22 - a32 - a33) * b22
            saved.append((names, "m_{1} = (a_{1,1} + a_{1,2} + a_{1,3} - a_{2,1} - a_{2,2} - a_{3,2} - a_{3,3}) * b_{2,2} ="+str(m1)))
            names += 1
            m2 = (a11 - a21) * (-b12 + b22)
            saved.append((names, "m_{2} = (a_{1,1} - a_{2,1}) * (-b_{1,2} + b_{2,2}) ="+str(m2)))
            names += 1
            m3 = a22 * (-b11 + b12 + b21 - b22 - b23 - b31 + b33)
            saved.append((names, "m_{3} = a_{2,2} * (-b_{1,1} + b_{1,2} + b_{2,1} - b_{2,2} - b_{2,3} - b_{3,1} + b_{3,3}) ="+str(m3)))
            names += 1
            m4 = (-a11 + a21 + a22) * (b11 - b12 + b22)
            saved.append((names, "m_{4} = (-a_{1,1} + a_{2,1} + a_{2,2}) * (b_{1,1} - b_{1,2} + b_{2,2}) ="+str(m4)))
            names += 1
            m5 = (a21 + a22) * (-b11 + b12)
            saved.append((names, "m_{5} = (a_{2,1} + a_{2,2}) * (-b_{1,1} + b_{1,2}) ="+str(m5)))
            names += 1
            m6 = a11 * b11
            saved.append((names, "m_{6} = a_{1,1} * b_{1,1} ="+str(m6)))
            names += 1
            m7 = (-a11 + a31 + a32) * (b11 - b13 + b23)
            saved.append((names, "m_{7} = (-a_{1,1} + a_{3,1} + a_{3,2}) * (b_{1,1} - b_{1,3} + b_{2,3}) ="+str(m7)))
            names += 1
            m8 = (-a11 + a31) * (b13 - b23)
            saved.append((names, "m_{8} = (-a_{1,1} + a_{3,1}) * (b_{1,3} - b_{2,3}) ="+str(m8)))
            names += 1
            m9 = (a31 + a32) * (-b11 + b13)
            saved.append((names, "m_{9} = (a_{3,1} + a_{3,2}) * (-b_{1,1} + b_{1,3}) ="+str(m9)))
            names += 1
            m10 = (a11 + a12 + a13 - a22 - a23 - a31 - a32) * b23
            saved.append((names, "m_{10} = (a_{1,1} + a_{1,2} + a_{1,3} - a_{2,2} - a_{2,3} - a_{3,1} - a_{3,2}) * b_{2,3} ="+str(m10)))
            names += 1
            m11 = a32 * (-b11 + b13 + b21 - b22 - b23 - b31 + b32)
            saved.append((names, "m_{11} = a_{3,2} * (-b_{1,1} + b_{1,3} + b_{2,1} - b_{2,2} - b_{2,3} - b_{3,1} + b_{3,2}) ="+str(m11)))
            names += 1
            m12 = (-a13 + a32 + a33) * (b22 + b31 - b32)
            saved.append((names, "m_{12} = (-a_{1,3} + a_{3,2} + a_{3,3}) * (b_{2,2} + b_{3,1} - b_{3,2}) ="+str(m12)))
            names += 1
            m13 = (a13 - a33) * (b22 - b32)
            saved.append((names, "m_{13} = (a_{1,3} - a_{3,3}) * (b_{2,2} - b_{3,2}) ="+str(m13)))
            names += 1
            m14 = a13 * b31
            saved.append((names, "m_{14} = a_{1,3} * b_{3,1} ="+str(m14)))
            names += 1
            m15 = (a32 + a33) * (-b31 + b32)
            saved.append((names, "m_{15} = (a_{3,2} + a_{3,3}) * (-b_{3,1} + b_{3,2}) ="+str(m15)))
            names += 1
            m16 = (-a13 + a22 + a23) * (b23 + b31 - b33)
            saved.append((names, "m_{16} = (-a_{1,3} + a_{2,2} + a_{2,3}) * (b_{2,3} + b_{3,1} - b_{3,3}) ="+str(m16)))
            names += 1
            m17 = (a13 - a23) * (b23 - b33)
            saved.append((names, "m_{17} = (a_{1,3} - a_{2,3}) * (b_{2,3} - b_{3,3}) ="+str(m17)))
            names += 1
            m18 = (a22 + a23) * (-b31 + b33)
            saved.append((names, "m_{18} = (a_{2,2} + a_{2,3}) * (-b_{3,1} + b_{3,3}) ="+str(m18)))
            names += 1
            m19 = a12 * b21
            saved.append((names, "m_{19} = a_{1,2} * b_{2,1} ="+str(m19)))
            names += 1
            m20 = a23 * b32
            saved.append((names, "m_{20} = a_{2,3} * b_{3,2} ="+str(m20)))
            names += 1
            m21 = a21 * b13
            saved.append((names, "m_{21} = a_{2,1} * b_{1,3} ="+str(m21)))
            names += 1
            m22 = a31 * b12
            saved.append((names, "m_{22} = a_{3,1} * b_{1,2} ="+str(m22)))
            names += 1
            m23 = a33 * b33
            saved.append((names, "m_{23} = a_{3,3} * b_{3,3} ="+str(m23)))
            names += 1

            text.append((names, "Then, the calculated values can be summed in the following ways, where..."))
            names += 1
            saved.append((names, "C_{2,3}"))
            names += 1
            text.append((names, "...is the element of the resultant matrix on the 2nd row and 3rd column"))
            names += 1
            C11 = m6 + m14 + m19
            saved.append((names, 'C_{1,1} = m_{6} + m_{14} + m_{19}='+str(C11)))
            names += 1
            C12 = m1 + m4 + m5 + m6 + m12 + m14 + m15
            saved.append((names, 'C_{1,2} = m_{1} + m_{4} + m_{5} + m_{6} + m_{12} + m_{14} + m_{15}='+str(C12)))
            names += 1
            C13 = m6 + m7 + m9 + m10 + m14 + m16 + m18
            saved.append((names, 'C_{1,3} = m_{6} + m_{7} + m_{9} + m_{10} + m_{14} + m_{16} + m_{18}='+str(C13)))
            names += 1
            C21 = m2 + m3 + m4 + m6 + m14 + m16 + m17
            saved.append((names, 'C_{2,1} = m_{2} + m_{3} + m_{4} + m_{6} + m_{14} + m_{16} + m_{17}='+str(C21)))
            names += 1
            C22 = m2 + m4 + m5 + m6 + m20
            saved.append((names, 'C_{2,2} = m_{2} + m_{4} + m_{5} + m_{6} + m_{20}='+str(C22)))
            names += 1
            C23 = m14 + m16 + m17 + m18 + m21
            saved.append((names, 'C_{2,3} = m_{14} + m_{16} + m_{17} + m_{18} + m_{21}='+str(C23)))
            names += 1
            C31 = m6 + m7 + m8 + m11 + m12 + m13 + m14
            saved.append((names, 'C_{3,1} = m_{6} + m_{7} + m_{8} + m_{11} + m_{12} + m_{13} + m_{14}='+str(C31)))
            names += 1
            C32 = m12 + m13 + m14 + m15 + m22
            saved.append((names, 'C_{3,2} = m_{12} + m_{13} + m_{14} + m_{15} + m_{22}='+str(C32)))
            names += 1
            C33 = m6 + m7 + m8 + m9 + m23
            saved.append((names, 'C_{3,3} = m_{6} + m_{7} + m_{8} + m_{9} + m_{23}='+str(C33)))
            names += 1

            C = [C11,C12,C13,C21,C22,C23,C31,C32,C33]
            final_matrix = sp.Matrix(l_rows, l_rows, C)
            text.append((names, "Therefore, the resultant matrix is..."))
            names += 1
            saved.append((names, sp.latex(final_matrix)))
            names += 1
            return final_matrix

    def latex2img(self):
        global names
        global saved
        global text
        names = 0
        for i in saved:
            text2image.formula_as_file(i[1], i[0])
        for i in text:
            text2image.toImage(i[1], i[0])
        saved = []
        text = []

    def compare_latex2img(self, subfolder):
        global names
        global saved
        global text
        names = 0
        for i in saved:
            compare_text2image.formula_as_file(i[1], i[0], subfolder)
        for i in text:
            compare_text2image.toImage(i[1], i[0], subfolder)
        saved = []
        text = []

def getMethods():
    methods = []
    methods.append(("Standard", naiveMultiplication))
    methods.append(("Strassen", Strassen))
    methods.append(("Laderman", Laderman))
    return methods

# empty()
# a = sp.Matrix([[1,2,3,4],[4,5,6,6],[7,8,9,2],[7,6,9,4]]) # Strassen's
# b = sp.Matrix([[1,2,3,4],[7,6,9,4],[7,8,9,2],[4,5,6,6]]) # Strassen's

# a = sp.Matrix([[1,2,3],[4,5,6],[4,6,6],[1,5,3],[7,2,6]])
# b = sp.Matrix([[3,4,5],[6,7,8],[6,4,2]])

# a = sp.Matrix([[1,3,4],[4,5,6],[7,8,2]]) # Strassen's
# b = sp.Matrix([[1,3,4],[6,9,4],[7,8,9]]) # Strassen's

# a = sp.Matrix([[1,2,3],[3,4,5]])
# b = sp.Matrix([[3,4],[1,2],[3,5]])

# a = sp.Matrix([])
# b = sp.Matrix([])
# x = Strassen(a, b)

# a = sp.Matrix([4])
# b = sp.Matrix([4])

# a = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])
# b = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])

# x = Laderman(a, b)
# sp.pprint(x.calc())
# x.latex2img()
# sp.pprint(a*b)