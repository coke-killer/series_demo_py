# __author__: "yudongyue"
# date: 2021/3/8
import numpy_4 as np

# 矢量运算
print('ndarray数组与标量/数组的运算')
x = np.array([1, 2, 3])
print(x * 2)  # [0 2 4]
print(x > 2)  # [False False  True]
y = np.array([3, 4, 5])
print(x + y)  # [4 6 8]
print(x > y)  # [False False False]
