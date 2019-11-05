# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/11/5 14:29
# 文件名称：page4
# 开发工具：PyCharm

# tf:词频： term frequency
# idf:逆文档频率：inverse document frequency log(总文档数/该词出现的文档数量)
# 词语重要性程度：tf * idf

from sklearn.feature_extraction.text import TfidfVectorizer
import jieba

def cutword():
    c1 = jieba.cut("今天是个好天气，我想出去爬山，但是我找不到跟我一块儿去的人，所以我就打电话给我的朋友。")
    c2 = jieba.cut("今天我打算在家写作业，但是接到我朋友的电话，他告诉我一块儿去爬山，我很高兴就一块儿去了。")
    # 转换为列表
    c1 = list(c1)
    c2 = list(c2)
    print(c1,c2)
    # 转换为字符串
    c1 = " ".join(c1)
    c2 = " ".join(c2)
    print(c1,c2)
    return c1,c2

def tfidfvec():
    cv = TfidfVectorizer()
    c1,c2 = cutword()
    data = cv.fit_transform([c1,c2])
    print(cv.get_feature_names())
    print(data.toarray())


if __name__ == '__main__':
    tfidfvec()
