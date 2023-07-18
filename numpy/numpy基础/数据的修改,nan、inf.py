import numpy as np

t1 = np.array(range(24)).reshape((4, 6))
print(t1)
print("*" * 50)

# 判断
print("判断")
print(t1 < 10)
print("*" * 50)

# 修改(方括号象征索引和切片)
print("修改(方括号象征索引和切片)")
t1[t1 < 10] = 3
print(t1)
print(" " * 50)
t1[t1 > 20] = 20
print(t1)
print(" " * 50)
t1 = np.where(t1 <= 3, 0, 10)  # 三元运算符：小于3变0，其余为10
print(t1)
print("*" * 50)
t2 = np.array(range(24)).reshape((4, 6))
print(t2)
print(" " * 50)
t2 = t2.clip(10, 15)  # 剪枝操作：将小于10的变为10，大于15的变为15
print(t2)
print("*" * 50)
# np.vstack() ->竖直拼接vertically
# np.hstack() ->水平拼接 horizontally

# 复制
print("复制")
a = np.array(range(0, 4)).reshape(2, 2)
print(a)
print(" " * 50)
b = a  # a,b同指向
c = a[:]  # 视图(view)的操作，一种切片。会创建新的对象c，但是c的数据完全由a保管
c = np.vstack((c, np.zeros([1, 2])))
print(c)
print(" " * 50)
print(a)
d = a.copy()  # 复制，互不影响
print("*" * 50)

# 行列相加
print("行列相加")
a = np.array(range(0, 4)).reshape(2, 2)
print(a)
print(" " * 50)
print(np.sum(a, axis=0))  # 行相加
print(" " * 50)
print(a.sum(axis=1))  # 列相加
print(" " * 50)
print(np.sum(a))  # 相加
print("*" * 50)
# 均值：a.mean(a,axis=None)
# 中值：np.median(a,axis=None)
# t.max(...) /  t.min(...)
# 极值：np.ptp(a,axis=None) 最大值最小值差
# 标准差：t.std(...)

# nan = not a number
e = np.nan
print(e)
print(np.nan != np.nan)
print(" " * 50)
# np.isnan(t_v) 寻找nan
# np.count_nonzero():返回值为非0的元素数量
# np.nonzero():返回值为非0的元素  ？？？猜测

# inf = infinity, -inf = 负无穷
