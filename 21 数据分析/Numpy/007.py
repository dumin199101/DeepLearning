# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/9 12:01
# 文件名称: 007
# 开发工具: PyCharm


# ---功能描述
"""
数组拼接
随机数
"""
import numpy as np

t1 = np.arange(10).reshape(2, 5)
t2 = np.arange(10, 20).reshape(2, 5)

t3 = np.vstack((t1, t2))
print(t3)
t4 = np.hstack((t1, t2))
print(t4)

# 整数
t5 = np.random.randint(10, 20, (3, 4))
print(t5)
# 小数
t6 = np.random.uniform(1, 5, (3, 4))
print(t6)
# 0-1
t7 = np.random.rand(3, 4)
print(t7)
# 标准正态
t8 = np.random.randn(3, 4)
print(t8)

# 值为0
t9 = np.zeros((3,2),dtype="int32")
print(t9)

# 值为1
t10 = np.ones((3,4),dtype="bool_")
print(t10)

# 深拷贝:不会相互影响
t11 = np.arange(10).reshape(2,5)
t12 = np.copy(t11)
t11[1,1] = 100
print(t11)
print(t12)