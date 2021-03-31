# __author__: "yudongyue"
# date: 2021/3/8
import numpy as np

o = [1, 2, '3', '4']
c = (1, 2, 'a', 'h',)
v = {
    'sa': [],
    's': 1,
    's2': 2,
    'c': 'c'
}

c = np.array([1, 2, 3, '1'])
print(c)
print(c.ndim)
print(c.shape)
print(c.dtype)
