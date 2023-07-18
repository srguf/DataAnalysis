import string
import pandas as pd
import numpy as np


"""
知识总结：
pd.DataFrame(,index=,columns=)
pd.DataFrame() 字典转
b1.shape  b1.dtypes  b1.index  b1.columns  b1.values  b1.ndim
"""


#创建
a = pd.DataFrame(np.array(range(12)).reshape((3, 4)))
print(a)
print("*" * 50)
# DataFrame既有行索引又有列索引
# 行索引：index, 0轴, axis=0
# 列索引：columns, 1轴, axis=1
a = pd.DataFrame(np.array(range(12)).reshape((3, 4)), index=list("xyz"), columns=list(string.ascii_lowercase[-4:]))
#index= ,columns= 传入的需要是一个list()
print(a)
print("*" * 50)

# 字典转
b = {"name": ["小明", "小刚"], "age": [20, 32], "tel": [10006, 10010]}
b = pd.DataFrame(b)
print(b)
print(" " * 50)
b1 = [{"name": "小王", "age": 23, "tell": 10023}, {"name": "小李", "tell": 10023},
      {"name": "小刚", "age": 23}]
b1 = pd.DataFrame(b1)
print(b1)
print("*" * 50)

# 查询
print(b1.shape)  # 形状
print(" " * 50)
print(b1.dtypes)  # 列数据类型
print(" " * 50)
print(b1.index)  # 行索引
print(" " * 50)
print(b1.columns)  # 列索引
print(" " * 50)
print(b1.values)  # 值
print(" " * 50)
print(b1.ndim)  # 表示数据的维度

