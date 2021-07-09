# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/9 10:42
# 文件名称: 006
# 开发工具: PyCharm


# ---功能描述
"""
Numpy中的Nan
Nan:数据类型float
np.nan != np.nan
np.count_nonzero()
np.isnan()
"""

import numpy as np

t1 = np.arange(20).reshape(4, 5).astype("float")
# 设置nan
t1[2, [1, 3]] = np.nan
print(t1)
for i in range(t1.shape[1]):
    # 选出含有nan的列
    temp_col = t1[:, i]
    print(temp_col != temp_col)
    count = np.count_nonzero(temp_col != temp_col)
    # print(count)
    if count > 0:
        temp_none_nan = temp_col[temp_col == temp_col]
        temp_col[np.isnan(temp_col)] = int(temp_none_nan.mean())
print(t1)