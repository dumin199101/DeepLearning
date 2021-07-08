# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/8 11:06
# 文件名称: 001
# 开发工具: PyCharm


# ---功能描述
"""
数组的形状
"""

import numpy as np

t1 = np.arange(12)
print(t1)
print(t1.shape)
t2 = t1.reshape((3, 4))
print(t2)
# t1未发生改变
print(t1)

t3 = np.array([[1, 2, 3], [7, 8, 9]])
print(t3)
# 展开：多维变一维
t4 = t2.flatten()
print(t4)