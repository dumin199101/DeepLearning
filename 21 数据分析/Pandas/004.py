# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/16 10:36
# 文件名称: 004
# 开发工具: PyCharm


# ---功能描述
"""
DataFrame的索引：loc属性·
"""
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("WXYZ"))
print(df1.loc["b":"c"])
print(df1.loc[["a", "b"], ["W", "Z"]])
print(df1.loc[:, ["W", "Z"]])
print(df1.loc[:, "X":])
