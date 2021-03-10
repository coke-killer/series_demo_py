# __author__: "yudongyue"
# date: 2021/3/9
import numpy as np
import numpy.linalg as nla

print('矩阵点×')
x = np.array([[1, 2], [3, 4]])
y = np.array([[1, 3], [2, 4]])
print(x.dot(y))
print('矩阵求逆')
x = np.array([[1, 1], [1, 2]])
y = nla.inv(x)
print(y)  # 矩阵求逆运（若矩阵真的存在）
print(x.dot(y))  # 单位矩阵 [[1. 0.] [0. 1.]]
print(nla.det(x))  # 求行列式
