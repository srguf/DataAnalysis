import numpy as np

us_file_path = "C:/MyCodeData/DataAnalysis/DataAnalysis-master/DataAnalysis-master/day03/code/youtube_video_data" \
               "/US_video_data_numbers.csv "

# delimiter:界定符
# dtype:数据格式
# unpack:是否转置(True/False)
t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=False)

print(t1)
print("*" * 50)

# 取行
print(t1[2])
print("*" * 50)

# 取连续的多行(切片操作)
print(t1[2:])
print("*" * 50)

print(t1[2:5])  # 切片3到5
print("*" * 50)

print(t1[2:10])
print(" " * 50)
print(t1[2:11:2])  # 2到10间隔1
print(" " * 50)
print(t1[[2, 8, 10]])  # 2行8行和10行
print("*" * 50)

# 取列
# print(t1[:, 0])  所有行的第0列
print(t1[2:11, 0])  # 取第2行到10行的所有第一列(:的本质还是切片，只不过这次加上了维度
print(" " * 50)
print(t1[[2, 8, 10], 0])  # 个人认为是切片的变形

print("*" * 50)
print(t1[:, [1, 3]])  # 所有行的第一列和第三列
print("*" * 50)

#取单行单列
t11 = t1[[2], [3]]
print(t11)
print(type(t11))  # <class 'numpy.ndarray'>
print(t11.dtype)
t111 = t1[2, 3]
print(t111)
print(type(t111))  # <class 'numpy.int32'>
print(t111.dtype)
print("*" * 50)

#取多个不相邻的点(注意：不是交点！不是交点！是坐标！)
print(t1[0:4, :])
print(" " * 50)
print(t1[[0, 3], [0, 2]])  # 1,3行与1,2列的 (0,0)(4,3)
print(" " * 50)
print(t1[[0, 1, 3], [0, 1,  2]])
print("*" * 50)

#取多行多列
print(t1[2:5, ])
print(" " * 50)
print(t1[2:5, 1:4])  # 3到5，2到4
