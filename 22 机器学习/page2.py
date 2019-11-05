# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/11/1 12:42
# 文件名称：page2
# 开发工具：PyCharm

# 机器学习教程【文本特征数据抽取】：英文
from sklearn.feature_extraction.text import CountVectorizer

def countvec():
    """
    :return:
    """
    countvec = CountVectorizer()
    data = countvec.fit_transform(["i love python","i dislike python"])
    print(countvec.get_feature_names())
    # print(data)
    # 转换为数组形式
    print(data.toarray())

if __name__ == '__main__':
    countvec()