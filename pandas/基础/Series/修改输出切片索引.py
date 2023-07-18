import string
import pandas as pd

a1 = pd.Series([2, 3, 4, 7, 23, 56], index=list("abcdef"))
b2 = pd.Series(a1, index=list(string.ascii_lowercase[1:8]))  # 经过我多次的实验，只有索引相同才会保留后面的数值
# 修改和输出其数据类型
b2 = b2.astype(float)
print(b2)
print(b2["f"])  # 通过索引
print(b2[4])  # 通过位置
print(" " * 50)
print(b2.index)
print("Value({})".format(b2.values))  # 这里只是为了和上面保持一致...
print("*" * 50)

# 切片和索引
print(b2[:5])  # 连续的
print(b2[[1, 4, 6]])  # 非连续
print(b2[["b", "d", "f"]])  # 通过索引的方式
print("*" * 50)

# 一些方法：
print(b2.where(b2 > 10, 10))  # where(a > 10, 10)当a values > 10时，替换为10

# b2.max()
# b2.min()
