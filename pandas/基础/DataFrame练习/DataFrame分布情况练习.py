import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Rating Runtime 的分布情况

data_path = "../../../DataAnalysis-master/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv"
data = pd.DataFrame(pd.read_csv(data_path))
# print(data.info())

y = data.loc[:, "Rating"].values  # series类型
# y = data.loc[:, "Runtime (Minutes)"].values
# y = data.loc[:, "Rating"].tolist  # 效果和。values差不多，但返回数据类型不一样，后续用到的方法也会不同例如max
# print(y)
# print(type(y))
# print(y.max())
# print(type(y.max()))

distance = 0.4
# distance = 5
bins = np.arange(y.min(), y.max(), distance)  # 在这里我用一个序列将平时的整数bins替换，用来对齐数据
# print(type(bins))
# print(y.max() - y.min())

plt.figure(figsize=(20, 8), dpi=80)
plt.hist(y, bins)

plt.xticks(np.arange(y.min(), y.max() + distance, distance))
# plt.xticks(range(y.min(), y.max() + distance, distance))  # range组距不能是float  np.arange()可以。返回值为：numpy.ndarray

plt.grid(alpha=0.3)
plt.show()

# bins是指直方图中柱状条的数量，也就是要将数据分成几个区间。默认情况下，plt.hist()函数会将数据分成10个等宽的区间，并绘制相应的柱状图。
# 这种默认的设置通常适用于大多数数据集，但如果需要更详细地探索数据分布，则可以通过调整bins参数来生成更细或更粗的柱状图。
# bins参数的取值有以下几种形式：
#   整数：表示将数据分成的区间的数量，例如bins=20表示将数据分成20个等宽的区间；
#   序列：表示指定每个区间的范围，例如bins=[0, 10, 20, 30, 40]表示将数据分为4个区间，分别是[0,10)、[10,20)、[20,30)和[30,40)；
#   字符串：表示使用一种特殊的方式指定区间，例如bins='auto'（自动确定区间）或bins='sqrt'（根据数据量的平方根确定区间）。
