import sympy as sp
from determinant import naiveDeterminant, Sarrus, LU
from multiplication import naiveMultiplication, Strassen, Laderman
from inverse import CayleyHamilton, naiveInverse
from solving import GaussianElimination, CramersRule, Cholesky
from eigenvalue import Eigenvalue
from eigenvector import Eigenvector

## Solving Systems of Linear Equations - Cholesky Decomposition ##

# test1 = sp.Matrix([])
# test2 = sp.Matrix([[7,28]])
# test3 = sp.Matrix([[3,1,19],[1,1,8]])
# test4 = sp.Matrix([[8,1,4],[1,1,3]])
# test5 = sp.Matrix([[2,-1,0,3],[-1,2,-1,4],[0,-1,2,5]])
# test6 = sp.Matrix([[25,15,-5,6],[15,18,0,16],[-5,0,11,22]])
# test7 = sp.Matrix([[7,2,7,5],[2,5,2,6],[7,2,9,12]])
# test8 = sp.Matrix([[1,1/2,1/3,1/4,2],[1/2,1/3,1/4,1/5,3],[1/3,1/4,1/5,1/6,4],[1/4,1/5,1/6,1/7,5]])
# test9 = sp.Matrix([[1,1,1,1,0],[1,2,3,4,3],[1,3,6,10,4],[1,4,10,20,5]])
# test10 = sp.Matrix([[5,7,6,5,6],[7,10,8,7,4],[6,8,10,9,12],[5,7,9,10,8]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     results = list(sp.linsolve(tests[i]))
#     print("Test {} Expected Result".format(i+1))
#     expected = []
#     try:
#         for j in results[0]:
#             expected.append(j.evalf())
#     except:
#         pass
#     sp.pprint(expected)
#     actual = Cholesky(tests[i])
#     if actual.check() == True:
#         ans = actual.calc()[0]
#         print("Test {} Actual Result".format(i+1))
#         sp.pprint(ans)
#         if expected == ans:
#             print("Test {} Passed!".format(i+1))
#             passed += 1
#     else:
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Matrix Multiplication - Laderman Method ##

# test1 = (sp.Matrix([[7,8,5],[10,8,9],[0,3,2]]),sp.Matrix([[9,1,9],[0,7,9],[7,1,6]]))
# test2 = (sp.Matrix([[4,0,10],[8,9,1],[7,4,1]]),sp.Matrix([[1,1,1],[0,6,1],[0,4,5]]))
# test3 = (sp.Matrix([[7,7,9],[1,3,9],[10,0,0]]),sp.Matrix([[6,1,10],[9,3,9],[0,0,6]]))
# test4 = (sp.Matrix([[7,5,10],[5,4,4],[6,8,5]]),sp.Matrix([[2,3,1],[3,1,9],[7,9,5]]))
# test5 = (sp.Matrix([[37,26,38],[17,5,4],[6,8,23]]),sp.Matrix([[9,47,1],[24,14,7],[27,19,28]]))
# test6 = (sp.Matrix([[19,39,31],[16,0,9],[29,36,40]]),sp.Matrix([[19,39,31],[16,0,9],[29,36,40]]))
# test7 = (sp.Matrix([[40,31,38],[32,0,2],[45,8,36]]),sp.Matrix([[27,43,18],[12,14,15],[33,41,22]]))
# test8 = (sp.Matrix([[12,3,30],[18,23,22],[28,40,11]]),sp.Matrix([[35,13,0],[22,4,7],[33,9,3]]))
# test9 = (sp.Matrix([[17,35,27],[21,32,38],[7,4,38]]),sp.Matrix([[16,43,49],[37,30,30],[47,6,12]]))
# test10 = (sp.Matrix([[35,29,11],[47,25,3],[26,19,37]]),sp.Matrix([[45,47,24],[40,49,50],[49,1,1]]))

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     expected = tests[i][0]*tests[i][1]
#     print("Test {} Expected Result".format(i+1))
#     sp.pprint(expected)
#     try:
#         actual = Laderman(tests[i][0], tests[i][1]).calc()
#         print("Test {} Actual Result".format(i+1))
#         sp.pprint(actual)
#         if expected == actual:
#             print("Test {} Passed!".format(i+1))
#             passed += 1
#     except:
#         print("Error occurred!")
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Solving Systems of Linear Equations - Cramer's Rule ##

# test1 = sp.Matrix([])
# test2 = sp.Matrix([[7,28]])
# test3 = sp.Matrix([[3,2,19],[1,1,8]])
# test4 = sp.Matrix([[2,-1,4],[6,-3,3]])
# test5 = sp.Matrix([[-4,10,6],[2,-5,3]])
# test6 = sp.Matrix([[2,5,2,-38],[3,-2,4,17],[-6,1,-7,-12]])
# test7 = sp.Matrix([[3,0,-9,33],[7,-4,-1,-15],[4,6,5,-6]])
# test8 = sp.Matrix([[1,2,3,4,0],[7,14,20,27,0],[5,10,16,19,-2],[3,5,6,13,5]])
# test9 = sp.Matrix([[1,2,1,-1,5],[3/2,1,2,2,8],[4,4,3,4,22],[2/5,0,1/5,1,3]])
# test10 = sp.Matrix([[4,1,2,-3,5,-16],[-3,3,-1,4,-2,20],[-1,2,5,1,3,-4],[5,4,3,-1,2,-10],[1,-2,3,-4,5,3]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     results = list(sp.linsolve(tests[i]))
#     print("Test {} Expected Result".format(i+1))
#     expected = []
#     try:
#         for j in results[0]:
#             expected.append(j)
#     except:
#         pass
#     sp.pprint(expected)
#     actual = CramersRule(tests[i]).calc()
#     print("Test {} Actual Result".format(i+1))
#     sp.pprint(actual)
#     if expected == actual:
#         print("Test {} Passed!".format(i+1))
#         passed += 1
#     else:
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Inverse - Cayley-Hamilton Theorem ##

# test1 = sp.Matrix([])
# test2 = sp.Matrix([0])
# test3 = sp.Matrix([8])
# test4 = sp.Matrix([[2,6],[10,3]])
# test5 = sp.Matrix([[1,2],[2,4]])
# test6 = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])
# test7 = sp.Matrix([[4,2,5],[14,15,7],[23,2,1]])
# test8 = sp.Matrix([[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]])
# test9 = sp.Matrix([[-2,7,0,6,-2],[1,-1,3,2,2],[3,4,0,5,3],[2,5,-4,-2,2],[0,3,-1,1,-4]])
# test10 = sp.Matrix([[0,0,0,0,-2],[1,-1,3,2,2],[0,0,0,0,3],[2,5,0,-2,2],[0,3,-1,1,-4]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     try:
#         expected = tests[i].inv()
#         print("Test {} Expected Result".format(i+1))
#         sp.pprint(expected)
#         try:
#             actual = CayleyHamilton(tests[i]).calc()
#             print("Test {} Actual Result".format(i+1))
#             sp.pprint(actual)
#             if expected == actual:
#                 print("Test {} Passed!".format(i+1))
#                 passed += 1
#         except:
#             print("Error occurred!")
#             print("Test {} Failed!".format(i+1))
#     except:
#         print("No inverse exists!")
#         check = CayleyHamilton(tests[i]).check()[0]
#         if check == False:
#             print("Test {} Passed!".format(i+1))
#             passed += 1
#         elif check == True:
#             print("Test {} Failed!".format(i+1))       
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Determinant - LU Decomposition ##

# test1 = sp.Matrix([4])
# test2 = sp.Matrix([])
# test3 = sp.Matrix([[3,4],[6,5]])
# test4 = sp.Matrix([[3,4],[0,0]])
# test5 = sp.Matrix([[4.5,3.6],[7.2,8.1]])
# test6 = sp.Matrix([[3,4,7],[6,5,1],[9,4,7]])
# test7 = sp.Matrix([[0,0,0],[0,0,0],[0,0,0]])
# test8 = sp.Matrix([[9,8,3,3],[8,2,6,3],[4,3,3,1],[5,7,9,2]])
# test9 = sp.Matrix([[9,8,3,3,4],[8,2,6,3,1],[4,3,3,1,10],[5,7,9,2,7],[4,5,2,12,5]])
# test10 = sp.Matrix([[9,8,3,3,4],[8,2,6,3,1],[4,0,0,1,0],[5,7,9,2,7],[4,0,2,0,5]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     expected = tests[i].det()
#     print("Test {} Expected Result".format(i+1), expected)
#     try:
#         actual = LU(tests[i]).calc()
#         print("Test {} Actual Result".format(i+1), actual)
#         if expected == actual:
#             print("Test {} Passed!".format(i+1))
#             passed += 1
#     except:
#         print("Error occurred!")
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Determinant - Sarrus' Method ##

# test1 = sp.Matrix([[3,4,7],[6,5,1],[9,4,7]])
# test2 = sp.Matrix([[0,0,0],[0,0,0],[0,0,0]])
# test3 = sp.Matrix([[1,-2,3],[-4,-5,-6],[7,-8,9]])
# test4 = sp.Matrix([[-2,-1,0],[6,1,-7],[4,-4,6]])
# test5 = sp.Matrix([[0,5,-6],[7,6,-3],[1,2,8]])
# test6 = sp.Matrix([[2,1,-1],[0,2,-2],[3,4,-1]])
# test7 = sp.Matrix([[1,2,1],[2,3,1],[3,4,2]])
# test8 = sp.Matrix([[-4,-4,4],[-1,0,1],[-7,-6,7]])
# test9 = sp.Matrix([[5,2,1],[0,1,1],[1,3,1]])
# test10 = sp.Matrix([[0.28,-0.96,0],[0.96,0.28,0],[0,0,1]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     expected = tests[i].det()
#     print("Test {} Expected Result".format(i+1), expected)
#     try:
#         actual = Sarrus(tests[i]).calc()
#         print("Test {} Actual Result".format(i+1), actual)
#         if expected == actual:
#             print("Test {} Passed!".format(i+1))
#             passed += 1
#     except:
#         print("Error occurred!")
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Eigenvectors - Standard Method ##

# test1 = sp.Matrix([0])
# test2 = sp.Matrix([[0,0],[0,0]])
# test3 = sp.Matrix([[6,-1],[2,3]])
# test4 = sp.Matrix([[2,0,0],[1,2,1],[-1,0,1]])
# test5 = sp.Matrix([[1,2,1],[6,-1,0],[-1,-2,-1]])
# test6 = sp.Matrix([[4/5,-3/5,0],[3/5,4/5,0],[1,2,2]])
# test7 = sp.Matrix([[4,-6,-7],[-2,3,2],[2,-6,-5]])
# test8 = sp.Matrix([[2,-1,-1,0],[-1,3,-1,-1],[-1,-1,3,-1],[0,-1,-1,2]])
# test9 = sp.Matrix([[1,2,1,0,0],[2,1,2,0,0],[1,1,2,0,0],[0,0,0,0,2],[0,0,0,2,0]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9]
# passed = 0

# mat = test9

# results = mat.eigenvects()
# for i in results:
#     sp.pprint(i[2])
# print()
# actual = Eigenvector(mat).calc()
# for i in actual:
#     sp.pprint(i[1])
#     print()

## Eigenvalues - Standard Method ##

# test1 = sp.Matrix([0])
# test2 = sp.Matrix([[0,0],[0,0]])
# test3 = sp.Matrix([[6,-1],[2,3]])
# test4 = sp.Matrix([[2,0,0],[1,2,1],[-1,0,1]])
# test5 = sp.Matrix([[1,2,1],[6,-1,0],[-1,-2,-1]])
# test6 = sp.Matrix([[4/5, -3/5, 0],[3/5, 4/5, 0],[1, 2, 2]])
# test7 = sp.Matrix([[4,-6,-7],[-2,3,2],[2,-6,-5]])
# test8 = sp.Matrix([[2,-1,-1,0],[-1,3,-1,-1],[-1,-1,3,-1],[0,-1,-1,2]])
# test9 = sp.Matrix([[1,2,1,0,0],[2,1,2,0,0],[1,1,2,0,0],[0,0,0,0,2],[0,0,0,2,0]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9]
# passed = 0

# for i in range(len(tests)):
#     results = tests[i].eigenvals()
#     print("Test {} Expected Result".format(i+1))
#     expected = []
#     for k in results.items():
#         solution = k[0]
#         amount = k[1]
#         while amount > 0:
#             expected.append(solution)
#             amount -= 1
#     try:
#         expected.sort()
#     except:
#         pass
#     print(expected)
#     actual = Eigenvalue(tests[i]).calc()
#     print("Test {} Actual Result".format(i+1))
#     try:
#         actual.sort()
#     except:
#         pass
#     print(actual)
#     if expected == actual:
#         print("Test {} Passed!".format(i+1))
#         passed += 1
#     else:
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Solving Systems of Linear Equations - Gaussian Elimination ##

# test1 = sp.Matrix([])
# test2 = sp.Matrix([[7,28]])
# test3 = sp.Matrix([[3,2,19],[1,1,8]])
# test4 = sp.Matrix([[2,-1,4],[6,-3,3]])
# test5 = sp.Matrix([[-4,10,6],[2,-5,3]])
# test6 = sp.Matrix([[2,5,2,-38],[3,-2,4,17],[-6,1,-7,-12]])
# test7 = sp.Matrix([[3,0,-9,33],[7,-4,-1,-15],[4,6,5,-6]])
# test8 = sp.Matrix([[1,2,3,4,0],[7,14,20,27,0],[5,10,16,19,-2],[3,5,6,13,5]])
# test9 = sp.Matrix([[1,2,1,-1,5],[3/2,1,2,2,8],[4,4,3,4,22],[2/5,0,1/5,1,3]])
# test10 = sp.Matrix([[4,1,2,-3,5,-16],[-3,3,-1,4,-2,20],[-1,2,5,1,3,-4],[5,4,3,-1,2,-10],[1,-2,3,-4,5,3]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     results = list(sp.linsolve(tests[i]))
#     print("Test {} Expected Result".format(i+1))
#     expected = []
#     try:
#         for j in results[0]:
#             expected.append(j)
#     except:
#         pass
#     sp.pprint(expected)
#     actual = GaussianElimination(tests[i]).calc()[1]
#     print("Test {} Actual Result".format(i+1))
#     sp.pprint(actual)
#     if expected == actual:
#         print("Test {} Passed!".format(i+1))
#         passed += 1
#     else:
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Inverse - Standard Method ##

# test1 = sp.Matrix([])
# test2 = sp.Matrix([0])
# test3 = sp.Matrix([8])
# test4 = sp.Matrix([[2,6],[10,3]])
# test5 = sp.Matrix([[1,2],[2,4]])
# test6 = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])
# test7 = sp.Matrix([[4,2,5],[14,15,7],[23,2,1]])
# test8 = sp.Matrix([[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]])
# test9 = sp.Matrix([[-2,7,0,6,-2],[1,-1,3,2,2],[3,4,0,5,3],[2,5,-4,-2,2],[0,3,-1,1,-4]])
# test10 = sp.Matrix([[0,0,0,0,-2],[1,-1,3,2,2],[0,0,0,0,3],[2,5,0,-2,2],[0,3,-1,1,-4]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     try:
#         expected = tests[i].inv()
#         print("Test {} Expected Result".format(i+1))
#         sp.pprint(expected)
#         try:
#             actual = naiveInverse(tests[i]).calc()
#             print("Test {} Actual Result".format(i+1))
#             sp.pprint(actual)
#             if expected == actual:
#                 print("Test {} Passed!".format(i+1))
#                 passed += 1
#         except:
#             print("Error occurred!")
#             print("Test {} Failed!".format(i+1))
#     except:
#         print("No inverse exists!")
#         check = naiveInverse(tests[i]).check()[0]
#         if check == False:
#             print("Test {} Passed!".format(i+1))
#             passed += 1
#         elif check == True:
#             print("Test {} Failed!".format(i+1))       
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Matrix Multiplication - Standard Method ##

# test1 = (sp.Matrix([]),sp.Matrix([]))
# test2 = (sp.Matrix([9]),sp.Matrix([3]))
# test3 = (sp.Matrix([[4,7],[5,9]]),sp.Matrix([[2,9],[6,3]]))
# test4 = (sp.Matrix([[-1],[4],[4]]),sp.Matrix([[0,-2]]))
# test5 = (sp.Matrix([[0,3,5],[5,5,2]]),sp.Matrix([[3,4],[3,-2],[4,-2]]))
# test6 = (sp.Matrix([[1,0],[-1,5]]),sp.Matrix([[1,0,2],[4,5,4]]))
# test7 = (sp.Matrix([[1,0,3,9],[-1,5,4,3],[4,7,7,2],[4,6,12,19]]),sp.Matrix([[4,6,2,7],[3,6,7,3],[3,6,6,22],[6,7,8,13]]))
# test8 = (sp.Matrix([[4,2,5],[4,5,6],[8,4,1],[2,4,10]]),sp.Matrix([[7,2,1,5],[6,2,6,5],[12,12,15,1]]))
# test9 = (sp.Matrix([[5],[6],[2],[6],[9]]),sp.Matrix([[4,2,9,15,16]]))
# test10 = (sp.Matrix([[0,2,0],[1,0,0]]),sp.Matrix([[8,0],[0,3],[0,2]]))

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     expected = tests[i][0]*tests[i][1]
#     print("Test {} Expected Result".format(i+1))
#     sp.pprint(expected)
#     try:
#         actual = naiveMultiplication(tests[i][0], tests[i][1]).calc()
#         print("Test {} Actual Result".format(i+1))
#         sp.pprint(actual)
#         if expected == actual:
#             print("Test {} Passed!".format(i+1))
#             passed += 1
#     except:
#         print("Error occurred!")
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Matrix Multiplication - Strassen's Method ##

# test1 = (sp.Matrix([]),sp.Matrix([]))
# test2 = (sp.Matrix([9]),sp.Matrix([3]))
# test3 = (sp.Matrix([[4,7],[5,9]]),sp.Matrix([[2,9],[6,3]]))
# test4 = (sp.Matrix([[-1],[4],[4]]),sp.Matrix([[0,-2]]))
# test5 = (sp.Matrix([[0,3,5],[5,5,2]]),sp.Matrix([[3,4],[3,-2],[4,-2]]))
# test6 = (sp.Matrix([[1,0],[-1,5]]),sp.Matrix([[1,0,2],[4,5,4]]))
# test7 = (sp.Matrix([[1,0,3,9],[-1,5,4,3],[4,7,7,2],[4,6,12,19]]),sp.Matrix([[4,6,2,7],[3,6,7,3],[3,6,6,22],[6,7,8,13]]))
# test8 = (sp.Matrix([[4,2,5],[4,5,6],[8,4,1],[2,4,10]]),sp.Matrix([[7,2,1,5],[6,2,6,5],[12,12,15,1]]))
# test9 = (sp.Matrix([[5],[6],[2],[6],[9]]),sp.Matrix([[4,2,9,15,16]]))
# test10 = (sp.Matrix([[0,2,0],[1,0,0]]),sp.Matrix([[8,0],[0,3],[0,2]]))

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     expected = tests[i][0]*tests[i][1]
#     print("Test {} Expected Result".format(i+1))
#     sp.pprint(expected)
#     try:
#         actual = Strassen(tests[i][0], tests[i][1]).calc()
#         print("Test {} Actual Result".format(i+1))
#         sp.pprint(actual)
#         if expected == actual:
#             print("Test {} Passed!".format(i+1))
#             passed += 1
#     except:
#         print("Error occurred!")
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))

## Determinant - Standard Method ##

# test1 = sp.Matrix([4])
# test2 = sp.Matrix([])
# test3 = sp.Matrix([[3,4],[6,5]])
# test4 = sp.Matrix([[3,4],[0,0]])
# test5 = sp.Matrix([[4.5,3.6],[7.2,8.1]])
# test6 = sp.Matrix([[3,4,7],[6,5,1],[9,4,7]])
# test7 = sp.Matrix([[0,0,0],[0,0,0],[0,0,0]])
# test8 = sp.Matrix([[9,8,3,3],[8,2,6,3],[4,3,3,1],[5,7,9,2]])
# test9 = sp.Matrix([[9,8,3,3,4],[8,2,6,3,1],[4,3,3,1,10],[5,7,9,2,7],[4,5,2,12,5]])
# test10 = sp.Matrix([[9,8,3,3,4],[8,2,6,3,1],[4,0,0,1,0],[5,7,9,2,7],[4,0,2,0,5]])

# tests = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
# passed = 0

# for i in range(len(tests)):
#     expected = tests[i].det()
#     print("Test {} Expected Result".format(i+1), expected)
#     try:
#         actual = naiveDeterminant(tests[i]).calc()
#         print("Test {} Actual Result".format(i+1), actual)
#         if expected == actual:
#             print("Test {} Passed!".format(i+1))
#             passed += 1
#     except:
#         print("Error occurred!")
#         print("Test {} Failed!".format(i+1))
#     print()

# print("{}/{} tests passed!".format(passed, len(tests)))