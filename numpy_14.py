# __author__: "yudongyue"
# date: 2021/3/9
import numpy as np

print('数组重塑')
x = np.arange(0, 6)
print(x)
print(x.reshape(2, 3))
print(x)
print(x.reshape(2, 3).reshape(3, 2))
print(x)
y = np.array([[1, 1, 1], [1, 1, 1]])
x = x.reshape(y.shape)
print(x)
print(x.flatten())
print(x.flatten()[0])
print(x)
print(x.ravel())
print(x.ravel()[0])
print('维度大小自动推导')
arr = np.arange(15)
print(arr.reshape((3, -1)))  # 3行
