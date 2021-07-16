# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/16 11:19
# 文件名称: 005
# 开发工具: PyCharm


# ---功能描述
"""
数据清洗
"""
import pandas as pd

pd1 = pd.read_csv("nba.csv")
# 判断是否为空值
print(pd1["College"].isnull())
# 删除空值
pd2 = pd1.dropna()
print(pd2)
# 替换空值
print("*" * 100)
pd3 = pd1["College"].fillna("College is None")
print(pd3)
# 删除重复数据
pd4 = pd1.drop_duplicates()
print(pd4)
