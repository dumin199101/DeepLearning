# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/11/1 12:17
# 文件名称：page1
# 开发工具：PyCharm

# 机器学习教程【字典特征数据抽取】
# sparse矩阵,ndarray二维数组
# one-hot编码

from sklearn.feature_extraction import DictVectorizer

def dictvec():
    """
    :return:
    """
    dictvect = DictVectorizer(sparse=False)
    data = dictvect.fit_transform([{"city":"北京","temperature":100},{"city":"上海","temperature":60},{"city":"深圳","temperature":40}])
    print(dictvect.get_feature_names())
    print(dictvect.inverse_transform(data))
    print(data)
    return None

if __name__ == '__main__':
    dictvec()


