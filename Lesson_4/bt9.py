# import numpy as np
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# tich = a.dot(b)
# print(tich)
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],[4,5,6],[7,8,9]]
c = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3) :
    for j in range(3) :
        dot = 0
        for k in range(3) :
            dot += a[i][k]*b[k][j]
        c[i][j] = dot
print(c)

