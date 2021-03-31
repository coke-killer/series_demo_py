# __author__: "yudongyue"
# date: 2021/3/31
import pandas as pd

dic = {"java": 1,
       "python": "h5", "c": 3}
series = pd.Series(dic)
print("series  追加")
series['html'] = 4
print(series)
print(type(series.index))
