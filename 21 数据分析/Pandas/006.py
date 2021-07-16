# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/16 15:03
# 文件名称: 006
# 开发工具: PyCharm


# ---功能描述
"""
分组聚合
"""
import pandas as pd

pd1 = pd.read_csv("nba.csv")
# print(pd1.to_string())
# 按照球队进行分组
g1 = pd1.groupby(by=["Team","Position"])
for groupname, grouplist in g1:
    print(groupname, grouplist["Team"].count(), grouplist["Salary"].sum(), grouplist["Weight"].median(),
          grouplist["Age"].mean())

