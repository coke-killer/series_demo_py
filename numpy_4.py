# __author__: "yudongyue"
# date: 2021/3/8
# ndarray 数组的基本索引和切片
# 多维数组的索引
"""
arr[r1:r2,c1:c2]
arr[1,1] 等价arr[1][1]
[:] 代表某个维度的数据
"""
import numpy as np

print('ndarray的基本索引')
x = np.array([[1, 2], [3, 4], [5, 6]])
print(x[0])  # [1 2]
print(x[0][1])  # 2 普通python数组的索引
print(x[0, 1])  # 2 同上
x = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
print(x.ndim)
print(x[0])  # [[1 2][3 4][5 6][7 8]]
y = x[0].copy()  # 生成一个副本
z = x[0]  # 未生成一个副本
print(y)
print('==============')
print(y[0, 0])  # 1
y[0, 0] = 0
z[0, 0] = -1
print(y)
print(x[0])
print(z)
