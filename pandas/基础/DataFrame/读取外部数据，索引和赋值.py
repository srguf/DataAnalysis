import numpy as np
import pandas as pd


"""
知识总结：
pd.DataFrame(pd.read_csv("路径"))
pd.set_option(,)
data.head()  data.tail()  data.info()  data.describe()
data.sort_values(by=,ascending=)
单独索引固定的列的方法
data_sort.loc[]
赋值方式
"""


GBvideos = pd.read_csv(
    "C:/MyCodeData/DataAnalysis/DataAnalysis-master/DataAnalysis-master/day03/code/youtube_video_data/GBvideos.csv")
# print(GBvideos)
# print("*" * 50)

data = pd.DataFrame(GBvideos, columns=["channel_title", "views", "likes", "dislikes", "comment_total"])

#  这个表达式是不正确的。问题在于，在选取多列数据时，需要将这些列名作为一个 list 来传递，而您的代码中使用了多个单独的 list
# data = data[["channel_title"], ["views"], ["likes"], ["dislikes"], ["comment_total"]]
# data = data[["channel_title", "views", "likes", "dislikes", "comment_total"]]  # 第一个中括号索引，第二个是列表

# 显示全部行或列
pd.set_option('display.max_columns', None)  # 将 None 作为参数传递给 max_columns 参数时，表示不限制列的数量
# pd.set_option('display.max_rows', None)

# print(data)

# 筛选显示
print("*" * 25 + "(head)" + "*" * 25)
print(data.head())  # 显示头部几行，默认5行
print("*" * 25 + "(tail)" + "*" * 25)
print(data.tail())  # 显示末尾几行，默认5行
print("*" * 25 + "(info)" + "*" * 25)
print(data.info())  # 有关data的详细信息
print("*" * 25 + "(describe)" + "*" * 25)
print(data.describe())  # 快速综合统计结果
print()

# 找出播放量最多的前十个channel
print("*" * 25 + "(找出播放量最多的前十个channel)" + "*" * 25)
data_sort = data.sort_values(by="views", ascending=False)
# data_sort = data_sort.head(5)
print(data_sort[:5])
print()

# 单独索引固定的列
print("*" * 25 + "(单独索引固定的列)" + "*" * 25)
print(data_sort[["channel_title", "views"]][:5])  # 第一个为索引，第二个为切片，两个功能
print()

# a.loc[]:通过标签索引数据
print("*" * 25 + "(data_sort.loc)" + "*" * 25)
print(data_sort.loc[572, "channel_title"])
print(data_sort.loc[572, :])  # 取行
print(" " * 50)
print(data_sort.loc[[572, 110], :])  # 取行
print(" " * 50)
print(data_sort.loc[592:110, ["channel_title", "views"]])
# print(data_sort.loc[:, "channel_title"])  # 取列
# print(data_sort.iloc[572, "channel_title"])
print()

# 赋值
print("*" * 25 + "(赋值)" + "*" * 25)
data_sort.iloc[:2, 1] = np.nan
print(data_sort.iloc[:5, :2])
print(" " * 50)
data_sort.loc[572, "channel_title"] = np.nan
print(pd.notnull(data_sort["channel_title"].head()))
