# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/8 14:25
# 文件名称: 003
# 开发工具: PyCharm


# ---功能描述
"""
numpy数据类型：ndarray
numpy数组创建
"""
import numpy as np
import random

t1 = np.arange(4, 10, 2, dtype="i")
print(t1)
print(type(t1))
print(t1.dtype)

t2 = np.array([round(random.random(), 2) for i in range(10)])
print(t2)

t3 = np.array([1, 0, 1, 0, 1, 1], dtype="bool_")
print(t3)

