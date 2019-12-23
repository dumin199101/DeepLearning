# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/20 16:08
# 文件名称：page18
# 开发工具：PyCharm

# 蓝图解决flask项目分层问题
# 导包时使用绝对路径
# 外层的templates优先级要大于内层的templates优先级

from flask import Flask
from books import app_book
from cart import app_order

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

app.register_blueprint(app_book,url_prefix='/books')
app.register_blueprint(app_order,url_prefix='/orders')

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"



if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)