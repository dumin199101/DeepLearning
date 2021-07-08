# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/8 15:14
# 文件名称: 004
# 开发工具: PyCharm


# ---功能描述
"""
Numpy读取csv
"""

import numpy as np

t1 = np.loadtxt("demo.csv",dtype="int32",delimiter=",")
print(t1)
t2 = np.loadtxt("demo.csv",dtype="int32",delimiter=",",unpack=True)
print(t2)

print(t1.transpose())
print(t1.T)