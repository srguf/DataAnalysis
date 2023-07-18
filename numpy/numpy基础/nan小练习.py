# 把数组中的nan变为那列的平均值
import numpy as np


# shape:返回行列。 shape[0]:返回行数   shape[1]:返回列数
# t1.shape[1] 返回4   range(t1.shape[1]) = range(4) 返回0-3
def find_nan(t):
    for i in range(t.shape[1]):
        t_v = t[:, i]  # t_v: vertically
        # np.count_nonzero():返回值为非0的元素量
        no_zero = np.count_nonzero(t_v != t_v)
        if no_zero != 0:
            t_arr = t_v[t_v == t_v]
            t_v[np.isnan(t_v)] = t_arr.mean()


if __name__ == '__main__':
    t1 = np.arange(24).reshape((4, 6)).astype("float")
    t1[1, 2:] = np.nan
    print(t1)

    find_nan(t1)
    print(t1)
