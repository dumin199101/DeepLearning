# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/16 10:01
# 文件名称: 003
# 开发工具: PyCharm


# ---功能描述
"""
pandas 读取外部数据
"""

import pandas as pd

df1 = pd.read_csv("nba.csv")
# 输出前五行跟后五行，其余用省略号代替
print(df1)
print("*" * 100)
# 输出所有
print(df1.to_string())
print("*" * 100)
# 读取前十行
print(df1.head(10).to_string())
print("*" * 100)
# 读取后十行
print(df1.tail(10))
print("*" * 100)
# 读取信息
print(df1.info())
print(df1.describe())
print("*" * 100)
# 读取属性
print(df1.index)
print(df1.columns)
print(df1.values)
print(df1.ndim)
print(df1.dtypes)
print(df1.shape)
# 排序
print("*" * 100)
df1 = df1.sort_values(by="Salary",ascending=False)
print(df1)
