# # print(10.0**20)
# # print(1+10.0**20)
# # print((1+10.0**20)-10.0**20)
# # print(1+(10.0**20-10.0**20))

########## Determinant ##########
# empty()
# a = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])
# a = sp.Matrix([[3,4,7],[6,5,1],[9,4,7]])
# a = sp.Matrix([[2,6,3,5],[3,5,6,4],[2,4,3,5],[3,5,7,4]])
# a = sp.Matrix([[0,0,0],[0,0,0],[0,0,0]])
# det = naiveDeterminant(a)
# print(det.calc())
# det.addSaved(True)
# det.latex2img()

########## Matrix Multiplication ##########
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
# x.addSaved(True)
# x.latex2img()
# sp.pprint(a*b)

########## Inverse ##########
# empty()
# a = sp.Matrix([[2,6,3,5],[3,5,6,4],[2,4,3,5],[3,5,7,4]])
# a = sp.Matrix([[1,2,3],[4,5,6],[7,2,9]])
# a = sp.Matrix([8])
# sp.pprint(a)
# inverse = CayleyHamilton(a)
# print(inverse.check())
# sp.pprint(inverse.calc())
# inverse.latex2img()

# a = sp.Matrix([[2,6,5],[3,14,1],[4,5,7]])
# a = sp.Matrix([])
# a = sp.Matrix([8])
# sp.pprint(a)
# inverse = naiveInverse(a)
# print(inverse.check())
# sp.pprint(inverse.calc())
# inverse.latex2img()