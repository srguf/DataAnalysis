# 英国和美国各自youtube1000的数据结合之前的ma绘制出各自评论数量的直方图

import numpy as np
from matplotlib import pyplot as plt


#数据的导入
uk_file_path = "C:/MyCodeData/DataAnalysis/DataAnalysis-master/DataAnalysis-master/day03/code/youtube_video_data" \
               "/GB_video_data_numbers.csv "
us_file_path = "C:/MyCodeData/DataAnalysis/DataAnalysis-master/DataAnalysis-master/day03/code/youtube_video_data" \
               "/GB_video_data_numbers.csv "

uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")
us = np.loadtxt(uk_file_path, delimiter=",", dtype="int")


#数据的处理
all_data = np.vstack((us, uk))  # 拼接
all_data = all_data[:, -1]  # 选出评论列
all_data = all_data[all_data <= 5000]  # 筛选出5000以下的评论

print(all_data)


#绘图
plt.figure(figsize=(18, 8), dpi=80)

distance = 100
bin_num = (max(all_data) - min(all_data)) // distance
plt.hist(all_data, bin_num)

# plt.xticks(list(range(max(all_data)))[::500])
# plt.yticks(range(min(all_data), max(all_data) + 1))
plt.ylabel("The number of people")
plt.xlabel("The number of comments")
plt.title("The comments of us and uk")

plt.grid(alpha=0.3)

plt.show()
