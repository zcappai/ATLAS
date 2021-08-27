import sympy as sp
import text2image
import compare_text2image
import saver
from single_image import single_view

# Standard Method
class naiveMultiplication:
    # Constructor takes left and right matrices as argument
    def __init__(self, leftmatrix, rightmatrix):
        self.leftmatrix = leftmatrix
        self.rightmatrix = rightmatrix
        self.saved = []

    # Calculates the resultant matrix
    def calc(self):
        original = "L="+sp.latex(self.leftmatrix)+" \\times "+"R="+sp.latex(self.rightmatrix)
        self.saved.append((saver.names, original))
        saver.names += 1
        # Generates empty resultant matrix
        res = sp.Matrix([[0 for x in range(self.rightmatrix.cols)] for y in range (self.leftmatrix.rows)])
        # Iterates through each element of resultant matrix
        for i in range(self.leftmatrix.rows):
            for j in range(self.rightmatrix.cols):
                self.saved.append((saver.names, "\\text{The resultant matrix so far is}$$$$"+sp.latex(sp.Matrix(res))))
                saver.names += 1
                # Adding product of 2 elements to resultant matrix
                for x in range(self.leftmatrix.cols):
                    res[i, j] += (self.leftmatrix.row(i).col(x)[0] * self.rightmatrix.row(x).col(j)[0])
                    self.saved.append((saver.names, "L_{"+str(i+1)+str(x+1)+"} \\times R_{"+str(x+1)+str(j+1)+"} ="+sp.latex(self.leftmatrix.row(i).col(x)[0])
                    +"\\times"+sp.latex(self.rightmatrix.row(x).col(j)[0])+"="+sp.latex(self.leftmatrix.row(i).col(x)[0] * self.rightmatrix.row(x).col(j)[0])))
                    saver.names += 1
                    self.saved.append((saver.names, "\\text{This is added to }a_{"+str(i+1)+str(j+1)+"}\\text{ in the resultant matrix}"))
                    saver.names += 1
                self.saved.append((saver.names, original))
                saver.names += 1
        self.saved.append((saver.names, "\\text{The final matrix is}$$$$"+sp.latex(res)))
        saver.names += 1
        self.saved.append(single_view(self.saved))
        return res

    # Adds steps from instance variable list to shared list
    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved

    # Converts the matrices and expressions to images for single method
    def latex2img(self):
        saver.names = 0
        for i in saver.saved:
            text2image.convertLatex(i[1], i[0])

    # Converts the matrices and expressions to images for method comparison
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.convertLatex(i[1], i[0], "Standard")

# Strassen's Method
class Strassen:
    # Constructor takes left and right matrices as argument
    def __init__(self, leftmatrix, rightmatrix):
        self.leftmatrix = leftmatrix
        self.rightmatrix = rightmatrix
        self.saved = []

    # Calculates the resultant matrix
    def calc(self):
        # Stores dimensions of resultant matrix
        final_rows = self.leftmatrix.rows
        final_cols = self.rightmatrix.cols
        original = "L="+sp.latex(self.leftmatrix)+" \\times "+"R="+sp.latex(self.rightmatrix)
        self.saved.append((saver.names, original))
        saver.names += 1
        # Dealing with empty matrix
        if self.leftmatrix.rows == 0 or self.rightmatrix.rows == 0:
            self.saved.append((saver.names, "\\text{Multiplying any matrix by an empty matrix}$$$$\\text{results in an empty matrix}"))
            saver.names += 1
            self.saved.append(single_view(self.saved))
            return sp.Matrix([])
        self.saved.append((saver.names, "\\text{Padding is added in the form of a row or column}$$$$\\text{of zeros to matrices with odd dimensions.}"
        +"$$$$\\text{Therefore, a matrix with an odd number of rows}$$$$\\text{(and/or columns) would get a row (and/or column)}$$$$\\text{of zeros to ensure even dimensions.}"))
        saver.names += 1
        # Dynamic padding
        # Adding row of 0s to left matrix
        if self.leftmatrix.rows % 2 == 1:
            self.leftmatrix = self.leftmatrix.col_join(sp.zeros(1, self.leftmatrix.cols))
            self.saved.append((saver.names, "\\text{The left matrix is padded with a row}$$$$\\text{of zeroes for an even number of rows}$$$$"+sp.latex(self.leftmatrix)))
            saver.names += 1
        # Adding column of 0s to left matrix
        if self.leftmatrix.cols % 2 == 1:
            self.leftmatrix = self.leftmatrix.row_join(sp.zeros(self.leftmatrix.rows, 1))
            self.saved.append((saver.names, "\\text{The left matrix is padded with a column}$$$$\\text{of zeroes for an even number of columns}$$$$"+sp.latex(self.leftmatrix)))
            saver.names += 1
        # Adding row of 0s to right matrix
        if self.rightmatrix.rows % 2 == 1:
            self.rightmatrix = self.rightmatrix.col_join(sp.zeros(1, self.rightmatrix.cols))
            self.saved.append((saver.names, "\\text{The right matrix is padded with a row}$$$$\\text{of zeroes for an even number of rows}$$$$"+sp.latex(self.rightmatrix)))
            saver.names += 1
        # Adding column of 0s to right matrix
        if self.rightmatrix.cols % 2 == 1:
            self.rightmatrix = self.rightmatrix.row_join(sp.zeros(self.rightmatrix.rows, 1))
            self.saved.append((saver.names, "\\text{The right matrix is padded with a column}$$$$\\text{of zeroes for an even number of columns}$$$$"+sp.latex(self.rightmatrix)))
            saver.names += 1

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
        self.saved.append((saver.names, """\\text{The left matrix is split into 4 equally-sized submatrices}$$$$a_{11}="""
        +sp.latex(a11)+", a_{12}="+sp.latex(a12)+", a_{21}="+sp.latex(a21)+", a_{22}="+sp.latex(a22)))
        saver.names += 1

        # Right matrix
        b11 = self.rightmatrix[:r_row_half, :r_col_half] # top-left
        b12 = self.rightmatrix[:r_row_half, r_col_half:] # top-right
        b21 = self.rightmatrix[r_row_half:, :r_col_half] # bottom-left
        b22 = self.rightmatrix[r_row_half:, r_col_half:] # bottom-right
        self.saved.append((saver.names, """\\text{The right matrix is split into 4 equally-sized submatrices}$$$$b_{11}="""
        +sp.latex(b11)+", b_{12}="+sp.latex(b12)+", b_{21}="+sp.latex(b21)+", b_{22}="+sp.latex(b22)))
        saver.names += 1

        # Multiplying submatrices if one has dimension equal to 1
        if l_row_half == 1 or l_col_half == 1 or r_row_half == 1 or r_col_half == 1:
            self.saved.append((saver.names, "\\text{A dimension of the submatrices is 1, so}"
            +"$$$$\\text{the submatrices will be multiplied using}$$$$\\text{the standard method of matrix multiplication}"))
            saver.names += 1
            m1 = naiveMultiplication((a11 + a22), (b11 + b22)).calc()
            self.saved.append((saver.names, "m_1=(a_{11}+a_{22})(b_{11}+b_{22})$$$$=("+sp.latex(a11)+"+"+sp.latex(a22)+")("+sp.latex(b11)+"+"+sp.latex(b22)+")$$$$="+sp.latex(m1)))
            saver.names += 1
            m2 = naiveMultiplication((a21 + a22), b11).calc()
            self.saved.append((saver.names, "m_2=(a_{21}+a_{22})b_{11}$$$$=("+sp.latex(a21)+"+"+sp.latex(a22)+")"+sp.latex(b11)+"$$$$="+sp.latex(m2)))
            saver.names += 1
            m3 = naiveMultiplication(a11, (b12 - b22)).calc()
            self.saved.append((saver.names, "m_3=a_{11}(b_{12}-b_{22})$$$$="+sp.latex(a11)+"("+sp.latex(b12)+"+"+sp.latex(-b22)+")$$$$="+sp.latex(m3)))
            saver.names += 1
            m4 = naiveMultiplication(a22, (b21 - b11)).calc()
            self.saved.append((saver.names, "m_4=a_{22}(b_{21}-b_{11})$$$$="+sp.latex(a22)+"("+sp.latex(b21)+"+"+sp.latex(-b11)+")$$$$="+sp.latex(m4)))
            saver.names += 1
            m5 = naiveMultiplication((a11 + a12), b22).calc()
            self.saved.append((saver.names, "m_5=(a_{11}+a_{12})b_{22}$$$$=("+sp.latex(a11)+"+"+sp.latex(a12)+")"+sp.latex(b22)+"$$$$="+sp.latex(m5)))
            saver.names += 1
            m6 = naiveMultiplication((a21 - a11), (b11 + b12)).calc()
            self.saved.append((saver.names, "m_6=(a_{21}-a_{11})(b_{11}+b_{12})$$$$=("+sp.latex(a21)+"+"+sp.latex(-a11)+")("+sp.latex(b11)+"+"+sp.latex(b12)+")$$$$="+sp.latex(m6)))
            saver.names += 1
            m7 = naiveMultiplication((a12 - a22), (b21 + b22)).calc()
            self.saved.append((saver.names, "m_7=(a_{12}-a_{22})(b_{21}+b_{22})$$$$=("+sp.latex(a12)+"+"+sp.latex(-a22)+")("+sp.latex(b21)+"+"+sp.latex(b22)+")$$$$="+sp.latex(m7)))
            saver.names += 1
        # Otherwise, Strassen's called recursively
        else:
            self.saved.append((saver.names, "\\text{None of the submatrices have a dimension of 1,}$$$$\\text{therefore Strassen's method is applied once again}"
            +"$$$$\\text{to each of these submatrices. But the steps of}$$$$\\text{the recursion will NOT be shown as the process}$$$$\\text{is identical to that which is shown here.}"))
            saver.names += 1
            self.saved.append((saver.names, "m_1=(a_{11}+a_{22})(b_{11}+b_{22})$$$$=("
            +sp.latex(a11)+"+"+sp.latex(a22)+")("+sp.latex(b11)+"+"+sp.latex(b22)+")$$$$="+sp.latex(a11+a22)+"*"+sp.latex(b11+b22)))
            saver.names += 1
            mat1 = Strassen((a11 + a22), (b11 + b22))
            m1 = mat1.calc()
            self.saved.append((saver.names, "m_1="+sp.latex(m1)))
            saver.names += 1
            self.saved.append((saver.names, "m_2=(a_{21}+a_{22})b_{11}$$$$=("+sp.latex(a21)+"+"+sp.latex(a22)+")"+sp.latex(b11)+"$$$$="+sp.latex(a21+a22)+"*"+sp.latex(b11)))
            saver.names += 1
            mat2 = Strassen((a21 + a22), b11)
            m2 = mat2.calc()
            self.saved.append((saver.names, "m_2="+sp.latex(m2)))
            saver.names += 1
            self.saved.append((saver.names, "m_3=a_{11}(b_{12}-b_{22})$$$$="+sp.latex(a11)+"("+sp.latex(b12)+"+"+sp.latex(-b22)+")$$$$="+sp.latex(a11)+"*"+sp.latex(b12-b22)))
            saver.names += 1
            mat3 = Strassen(a11, (b12 - b22))
            m3 = mat3.calc()
            self.saved.append((saver.names, "m_3="+sp.latex(m3)))
            saver.names += 1
            self.saved.append((saver.names, "m_4=a_{22}(b_{21}-b_{11})$$$$="+sp.latex(a22)+"("+sp.latex(b21)+"+"+sp.latex(-b11)+")$$$$="+sp.latex(a22)+"*"+sp.latex(b21-b11)))
            saver.names += 1
            mat4 = Strassen(a22, (b21 - b11))
            m4 = mat4.calc()
            self.saved.append((saver.names, "m_4="+sp.latex(m4)))
            saver.names += 1
            self.saved.append((saver.names, "m_5=(a_{11}+a_{12})b_{22}$$$$=("+sp.latex(a11)+"+"+sp.latex(a12)+")"+sp.latex(b22)+"$$$$="+sp.latex(a11+a12)+"*"+sp.latex(b22)))
            saver.names += 1
            mat5 = Strassen((a11 + a12), b22)
            m5 = mat5.calc()
            self.saved.append((saver.names, "m_5="+sp.latex(m5)))
            saver.names += 1
            self.saved.append((saver.names, "m_6=(a_{21}-a_{11})(b_{11}+b_{12})$$$$=("
            +sp.latex(a21)+"+"+sp.latex(-a11)+")("+sp.latex(b11)+"+"+sp.latex(b12)+")$$$$="+sp.latex(a21-a11)+"*"+sp.latex(b11+b12)))
            saver.names += 1
            mat6 = Strassen((a21 - a11), (b11 + b12))
            m6 = mat6.calc()
            self.saved.append((saver.names, "m_6="+sp.latex(m6)))
            saver.names += 1
            self.saved.append((saver.names, "m_7=(a_{12}-a_{22})(b_{21}+b_{22})$$$$=("
            +sp.latex(a12)+"+"+sp.latex(-a22)+")("+sp.latex(b21)+"+"+sp.latex(b22)+")$$$$="+sp.latex(a12-a22)+"*"+sp.latex(b21+b22)))
            saver.names += 1
            mat7 = Strassen((a12 - a22), (b21 + b22))
            m7 = mat7.calc()
            self.saved.append((saver.names, "m_7="+sp.latex(m7)))
            saver.names += 1
        self.saved.append((saver.names, "\\text{Therefore, the results of multiplications are}$$$$m_1="
        +sp.latex(m1)+",m_2="+sp.latex(m2)+",m_3="+sp.latex(m3)+"$$$$m_4="+sp.latex(m4)+",m_5="+sp.latex(m5)
        +",m_6="+sp.latex(m6)+",$$$$m_7="+sp.latex(m7)))
        saver.names += 1

        # Calculating final matrix elements
        c11 = m1 + m4 - m5 + m7
        c12 = m3 + m5
        c21 = m2 + m4
        c22 = m1 - m2 + m3 + m6
        self.saved.append((saver.names, "\\text{These submatrices can be added and subtracted}$$$$\\text{to produce the elements of the final matrix}$$$$c_{11}=m_1 + m_4 - m_5 + m_7="
        +sp.latex(c11)+"$$$$c_{12}=m_3 + m_5="+sp.latex(c12)+"$$$$c_{21}=m_2 + m_4="+sp.latex(c21)+"$$$$c_{22}=m_1 - m_2 + m_3 + m_6="+sp.latex(c22)))
        saver.names += 1

        # Joining submatrices to form final matrices
        top_half = c11.row_join(c12)
        bottom_half = c21.row_join(c22)
        final_matrix = top_half.col_join(bottom_half)
        self.saved.append((saver.names, "\\text{These can be joined together to produce}$$$$"+sp.latex(final_matrix)))
        saver.names += 1

        # Removing dynamic padding
        if final_matrix.cols != final_cols:
            final_matrix.col_del(final_matrix.cols - 1)
            self.saved.append((saver.names, "\\text{Since there is dynamic padding}$$$$\\text{in the form of a column of zeros,}$$$$\\text{this removed to give}$$$$"+sp.latex(final_matrix)))
            saver.names += 1
        if final_matrix.rows != final_rows:
            final_matrix.row_del(final_matrix.rows - 1)
            self.saved.append((saver.names, "\\text{Since there is dynamic padding}$$$$\\text{in the form of a row of zeros,}$$$$\\text{this removed to give}$$$$"+sp.latex(final_matrix)))
            saver.names += 1
        self.saved.append((saver.names, "\\text{Therefore, the resultant matrix is}$$$$"+sp.latex(final_matrix)))
        saver.names += 1
        self.saved.append(single_view(self.saved))
        return final_matrix

    # Adds steps from instance variable list to shared list
    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved

    # Converts the matrices and expressions to images for single method
    def latex2img(self):
        for i in saver.saved:
            text2image.convertLatex(i[1], i[0])

    # Converts the matrices and expressions to images for method comparison
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.convertLatex(i[1], i[0], "Strassen")

# Laderman Method
class Laderman:
    # Constructor takes left and right matrices as argument
    def __init__(self, leftmatrix, rightmatrix):
        self.leftmatrix = leftmatrix
        self.rightmatrix = rightmatrix
        self.saved = []

    # Calculates the resultant matrix
    def calc(self):
        original = "L="+sp.latex(self.leftmatrix)+" \\times "+"R="+sp.latex(self.rightmatrix)
        self.saved.append((saver.names, original))
        saver.names += 1
        # Dealing with non 3 x 3 matrices
        if self.leftmatrix.cols != 3 or self.leftmatrix.rows != 3 or self.rightmatrix.cols != 3 or self.rightmatrix.rows != 3:
            self.saved.append((saver.names, "\\text{Laderman method only multiplies 3x3}$$$$\\text{matrices, so it is not compatible}"))
            saver.names += 1
            self.saved.append(single_view(self.saved))
            return []
        # Dealing with 3 x 3 matrices
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

            # 23 Multiplications
            self.saved.append((saver.names, "\\text{Now, the following multiplications are calculated}"))
            saver.names += 1
            m1 = (a11 + a12 + a13 - a21 - a22 - a32 - a33) * b22
            self.saved.append((saver.names, "m_{1} = (a_{11} + a_{12} + a_{13} - a_{21} - a_{22} - a_{32} - a_{33}) \\times b_{22}$$$$"+
            "=("+sp.latex(a11)+"+"+sp.latex(a12)+"+"+sp.latex(a13)+"+"+sp.latex(-a21)+"+"+sp.latex(-a22)+"+"+sp.latex(-a32)+"+"+sp.latex(-a33)+")"+sp.latex(b22)+"$$$$="+sp.latex(m1)))
            saver.names += 1
            m2 = (a11 - a21) * (-b12 + b22)
            self.saved.append((saver.names, "m_{2} = (a_{11} - a_{21}) \\times (-b_{12} + b_{22})$$$$"+
            "=("+sp.latex(a11)+"+"+sp.latex(-a21)+")("+sp.latex(-b12)+"+"+sp.latex(b22)+")$$$$="+sp.latex(m2)))
            saver.names += 1
            m3 = a22 * (-b11 + b12 + b21 - b22 - b23 - b31 + b33)
            self.saved.append((saver.names, "m_{3} = a_{22} \\times (-b_{11} + b_{12} + b_{21} - b_{22} - b_{23} - b_{31} + b_{33})$$$$"+
            "="+sp.latex(a22)+"("+sp.latex(-b11)+"+"+sp.latex(b12)+"+"+sp.latex(b21)+"+"+sp.latex(-b22)+"+"+sp.latex(-b23)+"+"+sp.latex(-b31)+"+"+sp.latex(b33)+")$$$$="+sp.latex(m3)))
            saver.names += 1
            m4 = (-a11 + a21 + a22) * (b11 - b12 + b22)
            self.saved.append((saver.names, "m_{4} = (-a_{11} + a_{21} + a_{22}) \\times (b_{11} - b_{12} + b_{22})$$$$"+
            "=("+sp.latex(-a11)+"+"+sp.latex(a21)+"+"+sp.latex(a22)+")("+sp.latex(b11)+"+"+sp.latex(-b12)+"+"+sp.latex(b22)+")$$$$="+sp.latex(m4)))
            saver.names += 1
            m5 = (a21 + a22) * (-b11 + b12)
            self.saved.append((saver.names, "m_{5} = (a_{21} + a_{22}) \\times (-b_{11} + b_{12})$$$$=("+
            sp.latex(a21)+"+"+sp.latex(a22)+")("+sp.latex(-b11)+"+"+sp.latex(b12)+")$$$$="+sp.latex(m5)))
            saver.names += 1
            m6 = a11 * b11
            self.saved.append((saver.names, "m_{6} = a_{11} \\times b_{11}$$$$="+sp.latex(a11)+"\\times"+sp.latex(b11)+"$$$$="+sp.latex(m6)))
            saver.names += 1
            m7 = (-a11 + a31 + a32) * (b11 - b13 + b23)
            self.saved.append((saver.names, "m_{7} = (-a_{11} + a_{31} + a_{32}) \\times (b_{11} - b_{13} + b_{23})$$$$=("+
            sp.latex(-a11)+"+"+sp.latex(a31)+"+"+sp.latex(a32)+")("+sp.latex(b11)+"+"+sp.latex(-b13)+"+"+sp.latex(b23)+")$$$$="+sp.latex(m7)))
            saver.names += 1
            m8 = (-a11 + a31) * (b13 - b23)
            self.saved.append((saver.names, "m_{8} = (-a_{11} + a_{31}) \\times (b_{13} - b_{23})$$$$=("+
            sp.latex(-a11)+"+"+sp.latex(a31)+")("+sp.latex(b13)+"+"+sp.latex(-b23)+")$$$$="+sp.latex(m8)))
            saver.names += 1
            m9 = (a31 + a32) * (-b11 + b13)
            self.saved.append((saver.names, "m_{9} = (a_{31} + a_{32}) \\times (-b_{11} + b_{13})$$$$=("+
            sp.latex(a31)+"+"+sp.latex(a32)+")("+sp.latex(-b11)+"+"+sp.latex(b13)+")$$$$="+sp.latex(m9)))
            saver.names += 1
            m10 = (a11 + a12 + a13 - a22 - a23 - a31 - a32) * b23
            self.saved.append((saver.names, "m_{10} = (a_{11} + a_{12} + a_{13} - a_{22} - a_{23} - a_{31} - a_{32}) \\times b_{23}$$$$"+
            "=("+sp.latex(a11)+"+"+sp.latex(a12)+"+"+sp.latex(a13)+"+"+sp.latex(-a22)+"+"+sp.latex(-a23)+"+"+sp.latex(-a31)+"+"+sp.latex(-a32)+")"+sp.latex(b23)+"$$$$="+sp.latex(m10)))
            saver.names += 1
            m11 = a32 * (-b11 + b13 + b21 - b22 - b23 - b31 + b32)
            self.saved.append((saver.names, "m_{11} = a_{32} \\times (-b_{11} + b_{13} + b_{21} - b_{22} - b_{23} - b_{31} + b_{32})$$$$"+
            "="+sp.latex(a32)+"("+sp.latex(-b11)+"+"+sp.latex(b13)+"+"+sp.latex(b21)+"+"+sp.latex(-b22)+"+"+sp.latex(-b23)+"+"+sp.latex(-b31)+"+"+sp.latex(b32)+")$$$$="+sp.latex(m11)))
            saver.names += 1
            m12 = (-a13 + a32 + a33) * (b22 + b31 - b32)
            self.saved.append((saver.names, "m_{12} = (-a_{13} + a_{32} + a_{33}) \\times (b_{22} + b_{31} - b_{32})$$$$=("+
            sp.latex(-a13)+"+"+sp.latex(a32)+"+"+sp.latex(a33)+")("+sp.latex(b22)+"+"+sp.latex(b31)+"+"+sp.latex(-b32)+")$$$$="+sp.latex(m12)))
            saver.names += 1
            m13 = (a13 - a33) * (b22 - b32)
            self.saved.append((saver.names, "m_{13} = (a_{13} - a_{33}) \\times (b_{22} - b_{32})$$$$=("+
            sp.latex(a13)+"+"+sp.latex(-a33)+")("+sp.latex(b22)+"+"+sp.latex(-b32)+")$$$$="+sp.latex(m13)))
            saver.names += 1
            m14 = a13 * b31
            self.saved.append((saver.names, "m_{14} = a_{13} \\times b_{31}$$$$="+sp.latex(a13)+"\\times"+sp.latex(b31)+"$$$$="+sp.latex(m14)))
            saver.names += 1
            m15 = (a32 + a33) * (-b31 + b32)
            self.saved.append((saver.names, "m_{15} = (a_{32} + a_{33}) \\times (-b_{31} + b_{32})$$$$=("+
            sp.latex(a32)+"+"+sp.latex(a33)+")("+sp.latex(-b31)+"+"+sp.latex(b32)+")$$$$="+sp.latex(m15)))
            saver.names += 1
            m16 = (-a13 + a22 + a23) * (b23 + b31 - b33)
            self.saved.append((saver.names, "m_{16} = (-a_{13} + a_{22} + a_{23}) \\times (b_{23} + b_{31} - b_{33})$$$$=("+
            sp.latex(-a13)+"+"+sp.latex(a22)+"+"+sp.latex(a23)+")("+sp.latex(b23)+"+"+sp.latex(b31)+"+"+sp.latex(-b33)+")$$$$="+sp.latex(m16)))
            saver.names += 1
            m17 = (a13 - a23) * (b23 - b33)
            self.saved.append((saver.names, "m_{17} = (a_{13} - a_{23}) \\times (b_{23} - b_{33})$$$$=("+
            sp.latex(a13)+"+"+sp.latex(-a23)+")("+sp.latex(b23)+"+"+sp.latex(-b33)+")$$$$="+sp.latex(m17)))
            saver.names += 1
            m18 = (a22 + a23) * (-b31 + b33)
            self.saved.append((saver.names, "m_{18} = (a_{22} + a_{23}) \\times (-b_{31} + b_{33})$$$$=("+
            sp.latex(a22)+"+"+sp.latex(a23)+")("+sp.latex(-b31)+"+"+sp.latex(b33)+")$$$$="+sp.latex(m18)))
            saver.names += 1
            m19 = a12 * b21
            self.saved.append((saver.names, "m_{19} = a_{12} \\times b_{21}$$$$="+sp.latex(a12)+"\\times"+sp.latex(b21)+"$$$$="+sp.latex(m19)))
            saver.names += 1
            m20 = a23 * b32
            self.saved.append((saver.names, "m_{20} = a_{23} \\times b_{32}$$$$="+sp.latex(a23)+"\\times"+sp.latex(b32)+"$$$$="+sp.latex(m20)))
            saver.names += 1
            m21 = a21 * b13
            self.saved.append((saver.names, "m_{21} = a_{21} \\times b_{13}$$$$="+sp.latex(a21)+"\\times"+sp.latex(b13)+"$$$$="+sp.latex(m21)))
            saver.names += 1
            m22 = a31 * b12
            self.saved.append((saver.names, "m_{22} = a_{31} \\times b_{12}$$$$="+sp.latex(a31)+"\\times"+sp.latex(b12)+"$$$$="+sp.latex(m22)))
            saver.names += 1
            m23 = a33 * b33
            self.saved.append((saver.names, "m_{23} = a_{33} \\times b_{33}$$$$="+sp.latex(a33)+"\\times"+sp.latex(b33)+"$$$$="+sp.latex(m23)))
            saver.names += 1

            # Calculating resultant matrix elements
            self.saved.append((saver.names, "\\text{Then, the values can be summed in the following ways}"))
            saver.names += 1
            C11 = m6 + m14 + m19
            self.saved.append((saver.names, "C_{11} = m_{6} + m_{14} + m_{19}$$$$="
            +sp.latex(m6)+"+"+sp.latex(m14)+"+"+sp.latex(m19)+"$$$$="+sp.latex(C11)))
            saver.names += 1
            C12 = m1 + m4 + m5 + m6 + m12 + m14 + m15
            self.saved.append((saver.names, "C_{12} = m_{1} + m_{4} + m_{5} + m_{6} + m_{12} + m_{14} + m_{15}$$$$="
            +sp.latex(m1)+"+"+sp.latex(m4)+"+"+sp.latex(m5)+"+"+sp.latex(m6)+"+"+sp.latex(m12)+"+"+sp.latex(m14)+"+"+sp.latex(m15)+"$$$$="+sp.latex(C12)))
            saver.names += 1
            C13 = m6 + m7 + m9 + m10 + m14 + m16 + m18
            self.saved.append((saver.names, "C_{13} = m_{6} + m_{7} + m_{9} + m_{10} + m_{14} + m_{16} + m_{18}$$$$="
            +sp.latex(m6)+"+"+sp.latex(m7)+"+"+sp.latex(m9)+"+"+sp.latex(m10)+"+"+sp.latex(m14)+"+"+sp.latex(m16)+"+"+sp.latex(m18)+"$$$$="+sp.latex(C13)))
            saver.names += 1
            C21 = m2 + m3 + m4 + m6 + m14 + m16 + m17
            self.saved.append((saver.names, "C_{21} = m_{2} + m_{3} + m_{4} + m_{6} + m_{14} + m_{16} + m_{17}$$$$="
            +sp.latex(m2)+"+"+sp.latex(m3)+"+"+sp.latex(m4)+"+"+sp.latex(m6)+"+"+sp.latex(m14)+"+"+sp.latex(m16)+"+"+sp.latex(m17)+"$$$$="+sp.latex(C21)))
            saver.names += 1
            C22 = m2 + m4 + m5 + m6 + m20
            self.saved.append((saver.names, "C_{22} = m_{2} + m_{4} + m_{5} + m_{6} + m_{20}$$$$="
            +sp.latex(m2)+"+"+sp.latex(m4)+"+"+sp.latex(m5)+"+"+sp.latex(m6)+"+"+sp.latex(m20)+"$$$$="+sp.latex(C22)))
            saver.names += 1
            C23 = m14 + m16 + m17 + m18 + m21
            self.saved.append((saver.names, "C_{23} = m_{14} + m_{16} + m_{17} + m_{18} + m_{21}$$$$="
            +sp.latex(m14)+"+"+sp.latex(m16)+"+"+sp.latex(m17)+"+"+sp.latex(m18)+"+"+sp.latex(m21)+"$$$$="+sp.latex(C23)))
            saver.names += 1
            C31 = m6 + m7 + m8 + m11 + m12 + m13 + m14
            self.saved.append((saver.names, "C_{31} = m_{6} + m_{7} + m_{8} + m_{11} + m_{12} + m_{13} + m_{14}$$$$="
            +sp.latex(m6)+"+"+sp.latex(m7)+"+"+sp.latex(m8)+"+"+sp.latex(m11)+"+"+sp.latex(m12)+"+"+sp.latex(m13)+"+"+sp.latex(m14)+"$$$$="+sp.latex(C31)))
            saver.names += 1
            C32 = m12 + m13 + m14 + m15 + m22
            self.saved.append((saver.names, "C_{32} = m_{12} + m_{13} + m_{14} + m_{15} + m_{22}$$$$="
            +sp.latex(m12)+"+"+sp.latex(m13)+"+"+sp.latex(m14)+"+"+sp.latex(m15)+"+"+sp.latex(m22)+"$$$$="+sp.latex(C32)))
            saver.names += 1
            C33 = m6 + m7 + m8 + m9 + m23
            self.saved.append((saver.names, "C_{33} = m_{6} + m_{7} + m_{8} + m_{9} + m_{23}$$$$="
            +sp.latex(m6)+"+"+sp.latex(m7)+"+"+sp.latex(m8)+"+"+sp.latex(m9)+"+"+sp.latex(m23)+"$$$$="+sp.latex(C33)))
            saver.names += 1

            # Constructing resultant matrix
            C = [C11,C12,C13,C21,C22,C23,C31,C32,C33]
            final_matrix = sp.Matrix(self.leftmatrix.rows, self.leftmatrix.rows, C)
            self.saved.append((saver.names, "\\text{Therefore, the resultant matrix is}$$$$"+sp.latex(final_matrix)))
            saver.names += 1
            self.saved.append(single_view(self.saved))
            return final_matrix

    # Adds steps from instance variable list to shared list
    def addSaved(self, check):
        if check == True:
            saver.saved += self.saved

    # Converts the matrices and expressions to images for single method
    def latex2img(self):
        for i in saver.saved:
            text2image.convertLatex(i[1], i[0])

    # Converts the matrices and expressions to images for method comparison
    def compare_latex2img(self):
        for i in self.saved:
            compare_text2image.convertLatex(i[1], i[0], "Laderman")

# Stores method class and name for subfolder
def getMethods():
    methods = []
    methods.append(("Standard", naiveMultiplication))
    methods.append(("Strassen", Strassen))
    methods.append(("Laderman", Laderman))
    return methods