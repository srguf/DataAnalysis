# 如果列表a表示10点到12点每分钟的气温，如何绘制折线图观察每分钟气温的变化情况？
import random
from matplotlib import pyplot as plt

# 在 Python 中，方括号 [...] 用于列表推导式或者创建列表
x = range(120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)

a = list(x)
b_labels = ["10:{}".format(i) for i in range(0, 60)]
b_labels += ["11:{}".format(i - 60) for i in range(60, 120)]
#一对一替换（数目必须相同）
plt.xticks(a[::5], b_labels[::5])
plt.yticks(range(min(y), max(y) + 1))

#添加描述信息
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Changes in temperature per minute")

plt.show()
