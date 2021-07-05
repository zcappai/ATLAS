# # print(10.0**20)
# # print(1+10.0**20)
# # print((1+10.0**20)-10.0**20)
# # print(1+(10.0**20-10.0**20))

import sympy as sp
from string import ascii_lowercase
from text2image import formula_as_file

a = "R_1"
formula_as_file(a, 1)

# def gauss(A):
#     n = len(A)

#     for i in range(0, n):
#         # Search for maximum in this column
#         maxEl = abs(A[i][i])
#         maxRow = i
#         for k in range(i + 1, n):
#             if abs(A[k][i]) > maxEl:
#                 maxEl = abs(A[k][i])
#                 maxRow = k

#         # Swap maximum row with current row (column by column)
#         for k in range(i, n + 1):
#             tmp = A[maxRow][k]
#             A[maxRow][k] = A[i][k]
#             A[i][k] = tmp

#         # Make all rows below this one 0 in current column
#         for k in range(i + 1, n):
#             c = -A[k][i] / A[i][i]
#             for j in range(i, n + 1):
#                 if i == j:
#                     A[k][j] = 0
#                 else:
#                     A[k][j] += c * A[i][j]

#     # Solve equation Ax=b for an upper triangular matrix A
#     x = [0 for i in range(n)]
#     for i in range(n - 1, -1, -1):
#         x[i] = A[i][n] / A[i][i]
#         for k in range(i - 1, -1, -1):
#             A[k][n] -= A[k][i] * x[i]
#     return x


# A = [[0,0,0],[0,0,0]]
# print(A)

# # Calculate solution
# x = gauss(A)

# # Print result
# print(x)

# x = sp.Matrix([[1,0,1],[0,0,0],[0,0,0]])
# sp.pprint(x)
# atoms = list(ascii_lowercase)
# vars = sp.Matrix(3,1,atoms[:3])
# sp.pprint(vars)
# prod = x*vars
# solution = sp.solve(prod[0])[0]
# for key, value in solution.items():
#     vars = vars.subs(key, value)
# sp.pprint(vars)
# free = list(vars.free_symbols)
# print(free)
# eigenvectors = []
# for i in range(len(free)):
#     curr = free[i]
#     rem = free[:i] + free[i+1:]
#     temp = vars.subs(curr, 1)
#     for j in rem:
#         temp = temp.subs(j, 0)
#     eigenvectors.append(temp)
# sp.pprint(eigenvectors)

# x = sp.Matrix([[-2,-1,-1,0],[0,-1,-1,-2],[0,0,0,0],[0,0,0,0]])
# sp.pprint(x)
# atoms = list(ascii_lowercase)
# vars = sp.Matrix(4,1,atoms[:4])
# sp.pprint(vars)
# prod = x*vars
# sp.pprint(prod)
# solutions = []
# for i in prod:
#     solutions.append(sp.solve(i))
# print(solutions)
# for i in solutions:
#     print(i)
#     try:
#         for key, value in i[0].items():
#             sp.pprint(vars)
#             vars = vars.subs(key, value)
#             sp.pprint(vars)
#             print()
#     except:
#         pass
# print()
# sp.pprint(vars)
# free = list(vars.free_symbols)
# print(free)
# eigenvectors = []
# for i in range(len(free)):
#     curr = free[i]
#     rem = free[:i] + free[i+1:]
#     temp = vars.subs(curr, 1)
#     for j in rem:
#         temp = temp.subs(j, 0)
#     eigenvectors.append(temp)
# sp.pprint(eigenvectors)

# x = sp.Matrix([[0,0],[0,0]])
# sp.pprint(x)
# atoms = list(ascii_lowercase)
# vars = sp.Matrix(2,1,atoms[:2])
# sp.pprint(vars)
# prod = x*vars
# sp.pprint(prod)
# solutions = []
# for i in prod:
#     solutions.append(sp.solve(i))
# print(solutions)
# for i in solutions:
#     print(i)
#     try:
#         for key, value in i[0].items():
#             sp.pprint(vars)
#             vars = vars.subs(key, value)
#             sp.pprint(vars)
#             print()
#     except:
#         pass
# print()
# sp.pprint(vars)
# free = list(vars.free_symbols)
# print(free)
# eigenvectors = []
# for i in range(len(free)):
#     curr = free[i]
#     rem = free[:i] + free[i+1:]
#     temp = vars.subs(curr, 1)
#     for j in rem:
#         temp = temp.subs(j, 0)
#     eigenvectors.append(temp)
# sp.pprint(eigenvectors)