# # print(10.0**20)
# # print(1+10.0**20)
# # print((1+10.0**20)-10.0**20)
# # print(1+(10.0**20-10.0**20))

import sympy as sp
from string import ascii_lowercase
from text2image import formula_as_file
import math
from pprint import pprint

# def cholesky(A):
#     """Performs a Cholesky decomposition of A, which must 
#     be a symmetric and positive definite matrix. The function
#     returns the lower variant triangular matrix, L."""
#     # n = len(A)
#     n = A.rows

#     # Create zero matrix for L
#     L = sp.Matrix(n, n, [0]*n*n)
#     # L = [[0.0] * n for i in range(n)]

#     # Perform the Cholesky decomposition
#     for i in range(n):
#         for k in range(i+1):
#             tmp_sum = sum(L.row(i).col(j)[0] * L.row(k).col(j)[0] for j in range(k))
            
#             if (i == k): # Diagonal elements
#                 # LaTeX: l_{kk} = \sqrt{ a_{kk} - \sum^{k-1}_{j=1} l^2_{kj}}
#                 L[i, k] = math.sqrt(A.row(i).col(i)[0] - tmp_sum)
#             else:
#                 # LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{k-1}_{j=1} l_{ij} l_{kj} \right)
#                 L[i, k] = (1.0 / L.row(k).col(k)[0] * (A.row(i).col(k)[0] - tmp_sum))

#     # Forward substitution
#     L = L.col_insert(n+1, A.col(-1))
#     x = [0 for i in range(n)]
#     for i in range(0, n):
#         x[i] = L.row(i).col(n)[0] / L.row(i).col(i)[0]
#         if x[i] == sp.nan: #####################################################
#             x[i] = 1
#         for k in range(i + 1, n):
#             L[k, n] -= L.row(k).col(i)[0] * x[i]
#         L[i, n] = x[i]

#     # Transposed matrix
#     L.col_del(-1)
#     L = L.T
#     L = L.col_insert(n+1,sp.Matrix(n, 1, x))

#     # Back substitution
#     x = [0 for i in range(n)]
#     for i in range(n - 1, -1, -1):
#         x[i] = sp.N(L.row(i).col(n)[0] / L.row(i).col(i)[0], 10)
#         if x[i] == sp.nan: #####################################################
#             x[i] = 1
#         L[i, i] = 1
#         L[i, n] = x[i]
#         for k in range(i - 1, -1, -1):
#             L[k, n] -= L.row(k).col(i)[0] * x[i]
#             L[k, i] = 0
#     return x


# x = sp.Matrix([[6,15,55,76],[15,55,225,295],[55,225,979,1259]])

# sp.pprint(cholesky(x))