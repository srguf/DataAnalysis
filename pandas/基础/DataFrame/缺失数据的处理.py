import pandas as pd
import numpy as np


"""
知识总结：
a.iloc[,]  a.loc[]
a1.dropna(axis=,how=,inplace=)
a2.fillna()
a.mean()  a.median() 
np.nan
"""


a = pd.DataFrame(np.array(range(12)).reshape((3, 4)))
a.iloc[1:3, 0:2] = np.nan
print(a)
print("*" * 50)

# 处理方式一：去除nan所在的行列
a1 = a.copy()
a1.dropna(axis=0, how="any")  # axis=0 行   how="any" 任何有nan的都去掉  how="all" 所有都是nan才满足条件
print(a1)
print(" " * 50)
print(a1.dropna(axis=0, how="any"))
print(" " * 50)
a1.dropna(axis=0, how="any", inplace=True)  # inplace=True  替换原有a1
print(a1)
print("*" * 50)

# 处理方式二：填充数据a.fillna(a.mean()), a.dillna(a.median()), a.fillna(0)  a.median()：中值
a2 = a  # 注：这个只是索引
print(a2)
print(" " * 50)
print(a2.fillna(100))
print(" " * 50)
a3 = a2.fillna(a2.iloc[:, :2].mean())  # mean():得到指定位置的中位数
print(a3)
print("*" * 50)

# 处理为0的数据
a3[a3 == 0] = np.nan  # a3寻找a3 = 0的索引
print(a3)
