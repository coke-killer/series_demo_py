# __author__: "yudongyue"
# date: 2021/3/9
import numpy as np

"""
ndarray  数组的转置和轴对换
"""
k = np.arange(9)  # [0,1,....8]
m = k.reshape((3, 3))  # 改变数组的shape 复制生成2维的，每个维度长度为3的数组
print(m)
print('转置矩阵 T属性 mT[x][y]=m[y][x]')
print(m.T)
#  计算矩阵的内积 xTx
print(np.dot(m, m.T))  # numpy.dot点乘
# 高维数组的轴对象
k = np.arange(8).reshape((2, 2, 2))
print(k)
print(k[1][0][0])
# 轴变换，transpote 参数:由轴编号组成的元组
m = k.transpose((1, 0, 2))  # m[y][x][z] = k[x][y][z]
print(m)
print(m[0][1][0])
# 轴交换 swapaxes (axes：轴)，参数:一对轴编号
m = k.swapaxes(0, 1)  # 将第一个轴和第二个轴交换 m[y][x][z] = k[x][y][z]
print(m)  # [[[0 1],[4 5]],[[2 3],[6 7]]]
print(m[0][1][0])
#  使用轴交换进行数组矩阵转置
m = np.arange(9).reshape((3, 3))
print(m)
print(m.swapaxes(1, 0))
