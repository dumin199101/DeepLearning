# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/12 15:16
# 文件名称：page3.py
# 开发工具：PyCharm

# 路由提取参数与自定义路由转换器
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

@app.route("/goods/<int:goods_id>")
def goods(goods_id):
    return "Get goods_id is %d !" % goods_id

# 默认路由转换器为字符串规则
@app.route("/books/<book_id>")
def books(book_id):
    return "Get book_id is %s" % book_id

# 自定义转换器
class RegexConverter(BaseConverter):
    def __init__(self,url_map,regex):
        super(RegexConverter,self).__init__(url_map)
        self.regex = regex

    # def to_python(self, value): # 路由转换器被调用时被触发
    #     pass
    #
    # def to_url(self, value):  # url_for函数调用时被触发
    #     pass


# 将自定义转换器添加到flask应用
app.url_map.converters["re"] = RegexConverter

@app.route("/send/<re(r'1[34578]\d{9}'):tel>")
def send(tel):
    return "Get telephone is %s" % tel

if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)
