# __author__: "yudongyue"
# date: 2021/3/8
import numpy as np

print("ndarray 的切片")
x = np.array([1, 2, 3, 4, 5])
print(x[1:3])  # [2,3] 左闭右开
print(x[:3])  # [1,2,3]
print(x[1:])  # [2,3,4,5]
print(x[0:4:2])  # [1,3]
x = np.array([[1, 2], [3, 4], [5, 6]])
print(x)
print(x[:2])  # [[1,2],[3,4]]
print(x[:2, :1])  # [[1][3]]
x[:2, :1] = 0  # 用标量赋值
print(x)  # [[0 2][0 4][5 6]]
x[:2, :1] = [[8], [6]]  # 用数组赋值
print(x)  # [[8 2] [6 4][5 6]]
