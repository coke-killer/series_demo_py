# __author__: "yudongyue"
# date: 2021/3/9
import numpy as np

"""
ndarray数组的布尔索引和花式索引
"""
print('ndarray的布尔索引')
# 布尔型数组的长度必须跟被索引的轴的长度一致
x = np.array([3, 2, 3, 1, 3, 0])
y = np.array([True, False, True, True, False, False])
print(x[y])  # [3 3 1]
print(x[y == False])  # [2 3 0]
print(x >= 3)  # [ True False  True False  True False]
print(x[~(x >= 3)])  # [2 1 0]
print((x == 2) | (x == 1))  # [False  True False  True False False]
print(x[(x == 2) | (x == 1)])  # [2 1]
x[(x == 2) | (x == 1)] = 0
print(x)
