# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/8 15:48
# 文件名称: 005
# 开发工具: PyCharm


# ---功能描述
"""
numpy数组索引
"""

import numpy as np

t1 = np.loadtxt("demo.csv", delimiter=",", dtype="int64")
print(t1)
# 读取第一行数据
print(t1[0])
# 读取连续多行数据
print(t1[1:3])
# 读取不连续多行数据
print(t1[[1, 3, 5]])
# 读取第一列数据
print(t1[:, 0])
# 读取连续多列
print(t1[:, 0:3])
# 读取不连续多列
print(t1[:, [1, 3]])
# 读取某一行某一列
print(t1[1, 2])
# 读取某行某列的多个值
print(t1[[2, 3], [0, 1]])

print("*" * 100)

# 三元运算符
print(np.where(t1 < 1000, 10, 20))
# 小于100的替换为100，大于200的替换为200
t2 = t1.clip(100, 200)
print(t2)
