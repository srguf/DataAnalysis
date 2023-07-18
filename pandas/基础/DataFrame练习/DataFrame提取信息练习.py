import pandas as pd

# 请找出这些电影的平均分，导演人数等信息。

data_path = "../../../DataAnalysis-master/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv"
data = pd.DataFrame(pd.read_csv(data_path))
# pd.set_option('display.max_columns', None)
print(data.info())
print("*" * 50)
# print(data.head(1))

# 平均分
score = data.loc[:, "Rating"].mean()
print("平均分 = {}".format(score))
print("*" * 50)

# 导演人数
dir_member = len(data.loc[:, "Director"].unique())
# member = len(set(data.loc[:, "Director"]))  # set()：可以接受一个可迭代对象作为参数，如列表、元组、字符串等，并将其转换为一个无重复的集合
print("导演人数：{}".format(dir_member))

# 演员人数
act_member = len(data.loc[:, "Actors"].unique())
print("演员人数：{}".format(act_member))
