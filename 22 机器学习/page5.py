# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/11/5 14:34
# 文件名称：page5
# 开发工具：PyCharm

# 数据特征预处理
# 针对数字型数据，标准缩放
# 1.归一化（有计算公式【最大值，最小值】）
# 2.标准化（有计算公式【平均值，标准差】->方差）
# 3.缺失值处理


from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
import numpy as np

def mm():
    """
    归一化
    :return:
    """
    mm = MinMaxScaler()
    data = mm.fit_transform([[1,4,7],[6,9,2],[10,8,9]])
    print(data)

def std():
    """
    标准化
    :return:
    """
    std = StandardScaler()
    data = std.fit_transform([[1,4,7],[6,9,2],[10,8,9]])
    print(data)

def im():
    """
    缺失值处理
    :return:
    """
    im = Imputer(missing_values="NaN",strategy="mean",axis=0)
    data = im.fit_transform([[1,np.nan,7],[6,9,2],[10,8,9]])
    print(data)

if __name__ == '__main__':
    im()



