# __author__: "yudongyue"
# date: 2021/3/8
import numpy as np

print('使列表生成一维数组')
data = [1, 2, 3, 4, 5]
n = np.array(data)
print(n)  # 打印数组
print(n.dtype)  # 打印数组元素类型
print('使列表生成二维数组')
data_1 = [[1, 2], [3, 4]]
c = np.asarray(data_1)
print(c)  # 打印数组
print(c.ndim)  # 打印数组维度
print(c.shape)  # 打印数组形状
print(c.dtype)  # 打印数组类型
print('使用zero/ones/empty创建数组：根据形状shape来创建')
x = np.zeros(6)  # 创建一维长度为6的，元素都是0的一维数组
print(x)
x = np.zeros((2, 3))  # 创建两行三列的数组 都是0的数组
print(x)
print(x.ndim)
x = np.ones(6)
print(x)
x = np.ones((2, 3))
print(x)
x = np.empty((2, 3))  # 创建两行散列 ，未初始化的二维数组
print(x)
print('使用arrange生成连续元素')
print(np.arange(6))  # [0 1 2 3 4 5]
print(np.arange(0, 6, 2))  # [0 2 4]
