# 统计电影分类情况(Genre)
import pandas as pd
from matplotlib import pyplot as plt

data_path = "../../../DataAnalysis-master/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv"
data = pd.DataFrame(pd.read_csv(data_path))

lab = data.loc[:, "Genre"].str.split(",").tolist()
print(lab)
lable_list = lab.str.split(",").tolist()  # [[],[],[]]# .tolist()：Pandas 中的一个方法，将原对象变为 <class 'list'>
print(lable_list)