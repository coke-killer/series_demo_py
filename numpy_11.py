# __author__: "yudongyue"
# date: 2021/3/9
import numpy as np

print('ndarray 去重及集合计算')
x = np.array([[1, 6, 2], [6, 1, 3], [1, 5, 2]])
print(np.unique(x))  # [1 2 3 5 6]
y = np.array([1, 6, 5])
print(np.in1d(x, y))  # 得到x是否包含于y的布尔数组

print(np.setdiff1d(x, y))  # 集合的差，元素在X中不在y中
print(np.intersect1d(x, y)) # 存在一个数组不存贼两个数组中的元素
