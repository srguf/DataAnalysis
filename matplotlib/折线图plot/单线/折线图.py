from matplotlib import pyplot as plt

# 题目：某月气温变化表

# 知识点总结：
# 1.x,y的输入
# 2.绘制  plt.plot()
# 3.设置图片大小 plt.figure()
# 4，保存到本地 plt.savefig()
# 5.描述信息 xlabel() ylable() title()
# 6.调整x，y的间距 xticks(),yticks()
# 7.线条的样式 linestyle=
# 8.标记出特殊的点
# 9.添加水印

# 设置图片大小
plt.figure(figsize=(16, 8), dpi=80)

# 左闭右开
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 传入x，y通过plot绘制出折线图
plt.plot(x, y)

# 设置x，y轴的刻度
# plt.xticks(x)
# plt.xticks(range(2, 25))
num = []
for i in range(2, 25):
    num.append(i)
    num.append(i + 0.5)
# plt.xticks(num[::3])

num = [i / 2 for i in range(4, 50)]
plt.xticks(num)
plt.yticks(range(min(y), max(y) + 1))

# 保存
# plt.savefig("./SaveDate/p1.png")

# 输出
plt.show()

# 关于range：
# 在 Python 3 中，range() 函数返回的对象并不是列表，而是一个类型为 range 的可迭代对象（iterable），
# 它按需生成指定范围内的整数。这种方式称为“惰性求值”（lazy evaluation），它可以节省空间和时间。

# 因为 range 对象并不是列表，所以它并不占用与列表相同的内存空间。
# 相反，它只需要存储 start、stop 和 step 这三个参数，以及根据这些参数生成整数序列的算法。

# 当使用 range 对象时，Python 会根据需要逐个生成序列中的元素，而不是一次性生成所有元素并存储在内存中。

# 如果您需要将 range 对象转换为列表，可以使用 list() 函数将其转换为列表
