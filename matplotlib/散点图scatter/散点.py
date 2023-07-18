# 假设通过爬虫你获取到了北京2016年3.10月份每天白天的最高气温（分别位于列表.b)，那么此时
# 如何寻找出气温和随时间（天）变化的某种规律？
# a =[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
# b=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

from matplotlib import pyplot as plt

x_3 = range(1, 32)
x_10 = range(51, 82)
y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22,
       23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12,
        13, 6]

plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(x_3, y_3, label="March")
plt.scatter(x_10, y_10, label="October")

x__3 = ["March {}".format(i) for i in range(1, 32)]
x__10 = ["October {}".format(i) for i in range(1, 32)]
plt.xticks((list(x_3) + list(x_10))[::2], (x__3 + x__10)[::2], rotation=25)  # xticks(x轴(应该是列表), x轴对应写法(在这里时字符串), 旋转 )
plt.xlabel("Month")

plt.yticks(range(min(y_3) & min(y_10), max(y_3) & max(y_10) + 1))
plt.ylabel("Temperature")
plt.title("The highest daytime temperature in Beijing in March and October 2016")

plt.legend()

plt.show()

# 在Matplotlib中，xticks()函数可以接受多种类型的参数作为X轴刻度的值。下面是一些可接受的参数类型：
    # 列表或数组：该列表或数组包含要在X轴上显示的刻度值。
    # 整数范围：使用range()或np.arrange()函数生成的整数序列。
    # 时间戳：如果X轴表示时间，则可以使用时间戳作为刻度值。
    # Datetime对象：也可以直接使用Python的datetime对象作为X轴刻度值。
    # 字符串：可以将字符串用作X轴刻度值。
# 需要注意的是，无论使用哪种类型的参数，都应当确保它们是可以被解释为数字类型的。如果传递的参数不能被解释为数字类型，xticks()函数将会抛出一个异常。
