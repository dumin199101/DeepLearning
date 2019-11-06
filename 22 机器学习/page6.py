# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/11/6 14:44
# 文件名称：page6
# 开发工具：PyCharm

# 数据降维：
# 1.特征选择
# 2.主成分分析
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

def var():
    """
    特征选择：删除低方差的特征
    :return:
    """
    var = VarianceThreshold(threshold=0.0)
    data = var.fit_transform([[1,2,4],[2,2,4],[3,3,4]])
    print(data)

def pca():
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([[1,2,4,3],[2,2,4,2],[3,3,4,2]])
    print(data)



if __name__ == '__main__':
    var()
    pca()


