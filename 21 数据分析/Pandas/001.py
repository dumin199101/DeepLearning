# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/9 16:10
# 文件名称: 001
# 开发工具: PyCharm


# ---功能描述
"""
Pandas之Series
"""

import pandas as pd
import numpy as np

p1 = pd.Series(np.arange(10, 20))
print(p1)

stu1 = {"name": "lisi", "age": 22, "city": "beijing"}
p2 = pd.Series(stu1)
print(p2)
