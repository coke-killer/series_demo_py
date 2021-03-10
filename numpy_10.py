# __author__: "yudongyue"
# date: 2021/3/9
import numpy as np

print('数组的常用统计方法')
x = np.array([[1, 2], [3, 4], [1, 2]])
print(x.mean())
print(x.mean(axis=0))  # 列
print(x.mean(axis=1))  # 行
print(x.sum())
print(x.sum(axis=0))
print(x.sum(axis=1))
print(x.max())
print(x.cumsum())  # 所有元素累计和[ 1  3  6 10 11 13]
print(x.cumprod())  # 所有元素累计积[ 1  2  6 24 24 48]
#  用于布尔数组的统计方法
x = np.array([[True, False], [True, False]])
print(x.sum())
print(x.sum(axis=1))
print(x.any(axis=0))
print(x.all(axis=0))
print('sort排序')
x = np.array([[1, 3, 2], [4, 5, 6], [1, 5, 2]])
x.sort(axis=1)
print(x)
