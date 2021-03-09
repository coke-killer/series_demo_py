# __author__: "yudongyue"
# date: 2021/3/8
import numpy_4 as np

print('生成指定类型的数组：设置dtype属性')
x = np.array([1, 2, 6, 3], dtype=np.int64)
print(x.dtype)
x = np.array([1, 2, 3], dtype=np.float64)
print(x.dtype)
print('使用astype复制数组，并转变类型')
x = np.array([1, 2.3, 6, 3], dtype=np.float64)
print(x.dtype)
print(x.astype(np.int))
print(x.astype(np.float))
print('将字符串转换为数值元素')
x = np.array(['1.', '2.6', '3.'], dtype=np.str)
y = x.astype(np.float)
print(x)
print(y)
print('使用其他数组的数据类型作为参数')
x = np.array([1., 2.6, 3.], dtype=np.float)
y = np.arange(3, dtype=np.int)
print(y)
print(y.astype(x.dtype))
