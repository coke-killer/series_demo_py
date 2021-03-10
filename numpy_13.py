# __author__: "yudongyue"
# date: 2021/3/9
import numpy as np
import numpy.random as npr

print('numpy.random随机数生成')
x = npr.randint(0, 2, size=100000)  # 抛硬币
print((x > 0).sum())
print(npr.normal(size=(2, 2)))  # 正态分布随机数数组 shape=(2,2)
