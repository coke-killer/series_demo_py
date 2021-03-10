# __author__: "yudongyue"
# date: 2021/3/9
import numpy as np

print('一元ufunc示例')
x = np.arange(6)
print(x)
print(np.square(x))
x = np.array([1, 5, 1.6, 1.7, 1.8])
y, z = np.modf(x)
print(y)  # [0.  0.  0.6 0.7 0.8]
print(z)  # [1. 5. 1. 1. 1.]
print('二元ufunc示例')
x = np.array([[1, 4], [6, 7]])
y = np.array([[2, 3], [5, 8]])
print(np.maximum(x, y))
print(np.minimum(x, y))
