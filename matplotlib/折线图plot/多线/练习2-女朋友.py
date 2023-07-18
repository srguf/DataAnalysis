# 你在30岁时，统计了你和你同桌从11-30岁每年交的女友数量a 绘制折线图
# a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1] 要求：y个数，x岁数
# b = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
from matplotlib import pyplot as plt

x = range(11, 31)
y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y1, label="Me", color="orange", linestyle="--")
plt.plot(x, y2, label="Deskmate", color="cyan", linestyle="-.")

x1 = ["{} years old".format(i) for i in x]
plt.xticks(x, x1, rotation=15)
plt.xlabel("age")
plt.yticks(range(min(y1), max(y1) + 1))
plt.ylabel("number")
plt.title("The number of girlfriend you make each year")

# 网格化   alpha:透明度
plt.grid(alpha=0.4, linestyle=":")

#添加图例
plt.legend()

plt.show()
