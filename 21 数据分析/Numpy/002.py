# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/8 11:25
# 文件名称: 002
# 开发工具: PyCharm


# ---功能描述
"""
数组的计算
"""
import numpy as np

t1 = np.arange(10).reshape(2, 5)
print(t1)

t2 = t1 + 2
print(t2)

t3 = np.arange(5)
print(t3)
t4 = t1 + t3
print(t4)

t5 = np.arange(2).reshape(2,1)
print(t5)
t6 = t1 + t5
print(t6)

