# __author__: "yudongyue"
# date: 2021/3/31
import numpy as np
import pandas as pd

# numpy创建
series_1 = pd.Series(np.array([1, 2, 3, 4, 5]), name='a', index=['a', 'b', 'v', 'f', 'r'])
# 列表创建
series_2 = pd.Series([1, 2, 3, 4, 5], name='b')
# 字典创建
dic = {"java": 1,
       "python": "h5", "c": 3}
series_3 = pd.Series(dic)
print(series_1)
print(series_2)
print(series_3)
print(" Series索引和切片--显示索引，直接使用方括号 ")
print(series_3["java"])
print("多个索引要放在同一个列表中")
print(series_3[["java", "python"]])
print("推荐使用loc")
print(series_3.loc["java"])
print(series_3.loc[["java", "c"]])
print("推荐使用iloc")
print(series_3.iloc[0])
print("-------------")
print(series_3.iloc[[1, 2]])
print("切片")
print(series_3)
print("------------")
print(series_3.loc['java':'python'])
print("------------")
print(series_3.iloc[0:])
