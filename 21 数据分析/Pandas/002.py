# coding=utf-8
# 开发人员：烈焰
# 开发时间: 2021/7/9 17:53
# 文件名称: 002
# 开发工具: PyCharm


# ---功能描述
"""
Pandas之DataFrame
底层数据结构：ndarray
"""

import pandas as pd

dict1 = {"name":["zhangsan","lisi"],"age":[22,33],"city":["tianjin","shanghai"]}

p1 = pd.DataFrame(dict1)

print(p1)

print("*" * 100)

list2 = [{"name":"sunyue","age":40,"city":"shenyang"},{"name":"wangwei","age":20,"city":"jinan"},{"name":"malong","age":30,"city":"tianjin"}]
p2 = pd.DataFrame(list2)
print(p2)