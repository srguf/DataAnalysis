# 创建数组
import random

import numpy as np

# 使用numpy生成nbarray类型
t1 = np.array([2, 3, 4, 5, 6, 7, 8, 9])  # 方式一
print(t1)
print(type(t1))  # 显示存储格式

t2 = np.array(range(2, 10))  # 方式二
print(t2)
print(type(t2))  # 显示存储格式

t3 = np.arange(2, 10)  # 方式三
print(t3)
t3 = np.arange(2, 10, 2)
print(t3)
print(type(t3))  # 显示存储格式
print("*" * 50)

# numpy所存放数据的类型
print(t1.dtype)  # 显示数据格式
print(t3.dtype)
t4 = np.arange(2, 10, 2, dtype=float)  # 指定
print(t4.dtype)
t5 = np.array(range(10), dtype="int8")  # 指定
print(t5.dtype)
t5 = t5.astype("int16")  # 修改
print(t5.dtype)
print("*" * 50)

# 取固定位数的小数
t6 = np.array([random.random() for i in range(10)])
print(t6)
print(t6.dtype)
t6 = np.round(t6, 2)  # 设定小数取值
print(t6)
print("*" * 50)

# 数组的形状
print(t6.shape)  # 查看
t7 = np.array([[1, 2, 3], [4, 5, 6]])
print(t7)
print(t7.shape)
t7 = np.array(range(12))
print(t7)
print(t7.shape)
t7 = t7.reshape((1, 12))  # 修改格式 注：多了个中括号
print(t7)
print(t7.shape)
t7 = t7.flatten()  # 数组展平函数
print(t7)
#在NumPy中，reshape()函数的参数是一个元组（tuple），用于指定新数组的形状。当元组中只有一个元素时，需要在元素后面加一个逗号，
# 以表示这是一个元组而不是一个普通的数值。
t7 = t7.reshape((3, 4))  # 修改格式 注：先行后列
print(t7)
print(t7.shape)
t7 = t7.reshape((4, 3))  # 修改格式
print(t7)
print(t7.shape)
print(t7.transpose())  # 数组的转置
print(t7.T)  # 数组的转置
print("*" * 50)

# 数组的计算
t8 = np.array(range(100, 124)).reshape((4, 6))
print(t8)
t9 = np.array(range(100, 106))
print(t9)
print(t8 - t9)  # 总结：对应位置相减（行列(维度)数至少有一个相同）
