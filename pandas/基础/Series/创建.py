import string

import pandas as pd

# 创建方式一：
a = pd.Series([1, 3, 4, 7, 23, 56])
print(a)
print(" " * 50)
a1 = pd.Series([2, 3, 4, 7, 23, 56], index=list("abcdef"))
print(a1)
print("*" * 50)

# 创建方式二：通过字典创建
temp_b = {"name": "xiaohong", "age": 30, "tel": 10086}
b = pd.Series(temp_b)
print(b)
print(" " * 50)
b1 = {string.ascii_uppercase}  # 返回26大写字母
print(b1)
print(" " * 50)
b2 = pd.Series(a1, index=list(string.ascii_lowercase[1:8]))  # 经过我多次的实验，只有索引相同才会保留后面的数值
print(b2)
print("*" * 50)

